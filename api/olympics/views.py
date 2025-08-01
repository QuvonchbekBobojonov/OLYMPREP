from rest_framework.generics import ListAPIView

from apps.main.models import *
from api.olympics.serializers import OlympicsSerializer, OlympicsCategorySerializer, MentorSerializer


class OlympicListAPIView(ListAPIView):
    serializer_class = OlympicsSerializer
    queryset = Olympics.objects.all()


class OlympicsCategoryListAPIView(ListAPIView):
    serializer_class = OlympicsCategorySerializer
    queryset = OlympicsCategory.objects.all()


class MentorListAPIView(ListAPIView):
    serializer_class = MentorSerializer
    queryset = Mentor.objects.all()
