from django.urls import path

from .views import OlympicsCategoryListAPIView, OlympicListAPIView, MentorListAPIView
urlpatterns = [
    path('category/list/', OlympicsCategoryListAPIView.as_view()),
    path('list/', OlympicListAPIView.as_view()),
    path('mentor/list/', MentorListAPIView.as_view()),
]