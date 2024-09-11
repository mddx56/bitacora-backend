from rest_framework import serializers
from django.contrib.auth import get_user_model


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        write_only=True, required=True  # , validators=[password_validation]
    )
    password = serializers.CharField(write_only=True, required=True)
