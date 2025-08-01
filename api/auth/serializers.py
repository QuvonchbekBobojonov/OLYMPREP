from rest_framework import serializers

from apps.users.models import User


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'full_name', 'age', 'school', 'school_class', 'address')
        extra_kwargs = {'password': {'write_only': True}}
