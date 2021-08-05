from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers.rating_serializer import CreateRatingSerializer, RatingSerializer
from ..models import Rating


class AddStarRatingView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class RatingCheckView(APIView):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            r = Rating.objects.filter(user=request.user, product=kwargs['product'])
            if r:
                return Response(RatingSerializer(r[0]).data)
            return Response([])
        return Response(status=401)
