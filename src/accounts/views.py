import base64
import json
import random
import uuid
import requests

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.cache import cache
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.generics import UpdateAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken, TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.models import User
from accounts.serializers import (
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    SignUpSerializer,
    UserProfileSerializer,
    #UserListSerializer,
    UserPasswordUpdateSerializer,
    VerifySMSCodeSerializer,
)


def generate_code():
    return random.randint(100000, 999999)


def generate_uuid():
        return uuid.uuid4()


def set_cache(key, val, ttl=300):
    cache.set(f"{key}", val, timeout=ttl)

def send_sms(phone_number, code):
    phone_number = str(phone_number)
    text_message = f"Arenduy: {code}"
    credentials = (
        settings.SMS_SERVICE_USERNAME + ":" + settings.SMS_SERVICE_PASSWORD
    ).encode("utf-8")
    base64_encoded_credentials = base64.b64encode(credentials).decode("utf-8")

    headers = {
        "Authorization": "Basic " + base64_encoded_credentials,
        "Content-Type": "application/json",
    }
    body = {
        "messages": [
            {
                "recipient": phone_number,
                "message-id": f"ini{phone_number}_{code}",
                "sms": {
                    "originator": "3700",
                    "content": {"text": text_message},
                },
            }
        ]
    }
    body = json.dumps(body)
    return requests.post(settings.SMS_SERVICE_URL, headers=headers, data=body)

class SignUpView(APIView):
    throttle_scope = "sendSMS"
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = SignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_number = data["phone_number"]
        if get_user_model().objects.filter(
            phone_number=phone_number
        ).exists() or cache.get("phone_number"):
            return Response(
                data=f"{phone_number} is taken.",
                status=status.HTTP_409_CONFLICT,
            )
        generated_code = generate_code()
        response = send_sms(phone_number, generated_code)
        if not response.ok:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        data["password"] = make_password(data["password"])
        set_cache(phone_number, data)
        set_cache(f"{phone_number}_code", generated_code)
        return Response(status=status.HTTP_201_CREATED)

class VerifySMSCodeView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = VerifySMSCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_number = data["phone_number"]
        cache_code = cache.get(f"{phone_number}_code")
        if cache_code != data["code"]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        user = User.objects.create(**cache.get(phone_number))
        user.save()
        cache.expire(f"{phone_number}_code", timeout=1)
        cache.expire(phone_number, timeout=1)
        return Response(status=status.HTTP_200_OK)

class LogInSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        attrs = super(LogInSerializer, self).validate(attrs)
        # Custom data you want to include
        attrs.update({'id': self.user.id})
        return attrs

class LogInView(TokenObtainPairView):
    serializer_class = LogInSerializer

class LogOutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except TokenError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(APIView):
    throttle_scope = "sendSMS"
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            instance = get_user_model().objects.get(
                phone_number=data["phone_number"]
            )
        except Exception:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data="No phone number found",
            )
        code = generate_code()
        response = send_sms(instance.phone_number, code)
        if not response.ok:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        set_cache(instance.phone_number, code)
        return Response(status=status.HTTP_200_OK)

class VerifySMSCodeResetPasswordView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = VerifySMSCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        try:
            instance = get_user_model().objects.get(
                phone_number=data["phone_number"]
            )
        except Exception:
            return Response(
                status=status.HTTP_401_UNAUTHORIZED,
                data="No phone number found",
            )
        cache_code = cache.get(instance.phone_number)
        if cache_code != data["code"]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        guid = generate_uuid()
        set_cache(key=guid, val=instance.phone_number)
        return Response(data={"guid": guid}, status=status.HTTP_200_OK)

class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_number = cache.get(data["guid"])
        if phone_number is None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        instance = get_user_model().objects.get(phone_number=phone_number)
        instance.set_password(data["password"])
        instance.save()
        cache.expire(data["guid"], timeout=1)
        return Response(status=status.HTTP_200_OK)

class ChangePhoneNumberView(APIView):
    permission_classes = (IsAuthenticated,)
    throttle_scope = "sendSMS"

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_number = data["phone_number"]
        if get_user_model().objects.filter(
            phone_number=phone_number
        ).exists() or cache.get("phone_number"):
            return Response(
                data=f"{phone_number} is taken.",
                status=status.HTTP_409_CONFLICT,
            )
        generated_code = generate_code()
        response = send_sms(phone_number, generated_code)
        if not response.ok:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        set_cache(phone_number, phone_number)
        set_cache(f"{phone_number}_code", generated_code)
        return Response(status=status.HTTP_201_CREATED)

class VerifySMSCodeChangePhoneNumberView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = VerifySMSCodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        phone_number = data["phone_number"]
        cache_code = cache.get(f"{phone_number}_code")
        if cache_code != data["code"]:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        instance = get_user_model().objects.get(guid=request.user.guid)
        instance.phone_number = cache.get(phone_number)
        instance.save()
        cache.expire(f"{phone_number}_code", timeout=1)
        return Response(status=status.HTTP_200_OK)

class UserPasswordUpdateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = UserPasswordUpdateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        if not request.user.check_password(data["current_password"]):
            return Response(
                data={
                    "detail": "user password do not"
                    " match with current password"
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        request.user.set_password(data["new_password"])
        request.user.save()
        return Response(status=status.HTTP_200_OK)

class UserProfileAPIView(RetrieveAPIView):
    http_method_names = ["get"]
    permission_classes = (IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get_object(self):
        return User.objects.filter(guid=self.request.user.guid)

class UserProfileUpdateView(UpdateAPIView):
    http_method_names = ["put"]
    serializer_class = UserProfileSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

    def perform_update(self, serializer):
        serializer.instance.update_profile(serializer.validated_data)