from rest_framework import serializers

from apps.main.models import Olympics, OlympicsCategory, Mentor

class OlympicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Olympics
        fields = '__all__'


class OlympicsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OlympicsCategory
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
