from django.contrib.auth import get_user_model

from phonenumber_field.serializerfields import PhoneNumberField
from rest_framework import serializers

class SignUpSerializer(serializers.Serializer):
    first_name = serializers.CharField(max_length=100)
    last_name = serializers.CharField(max_length=100)
    phone_number = PhoneNumberField()
    password = serializers.CharField()

    def create(self, validated_data):
        return get_user_model().objects.create(**validated_data)

class VerifySMSCodeSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()
    code = serializers.IntegerField()

class ForgotPasswordSerializer(serializers.Serializer):
    phone_number = PhoneNumberField()

class ResetPasswordSerializer(serializers.Serializer):
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    guid = serializers.UUIDField()

    def validate(self, attrs):
        password = attrs["password"]
        confirm_password = attrs["confirm_password"]
        if password != confirm_password:
            raise serializers.ValidationError("passwords do not match")
        return attrs

class UserPasswordUpdateSerializer(serializers.Serializer):
    current_password = serializers.CharField()
    new_password = serializers.CharField()
    confirm_password = serializers.CharField()

    def validate(self, attrs):
        new_password = attrs["new_password"]
        confirm_password = attrs["confirm_password"]
        if new_password != confirm_password:
            raise serializers.ValidationError("passwords do not match")
        return attrs

class UserProfileSerializer(serializers.Serializer):
    phone_number = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)