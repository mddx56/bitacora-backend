from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ["id", "name", "permissions"]


"""
    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
"""
