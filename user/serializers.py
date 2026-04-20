"""Serializers for user authentication APIs."""

from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """Public user representation."""

    firstname = serializers.CharField(source="first_name", read_only=True)
    lastname = serializers.CharField(source="last_name", read_only=True)

    class Meta:
        """Serializer metadata."""

        model = get_user_model()
        fields = ("id", "email", "username", "firstname", "lastname")


class RegisterSerializer(serializers.ModelSerializer):
    """Create users while hashing passwords through Django's password stack."""

    password = serializers.CharField(write_only=True, min_length=8)
    firstname = serializers.CharField(source="first_name", required=False, allow_blank=True)
    lastname = serializers.CharField(source="last_name", required=False, allow_blank=True)

    class Meta:
        """Serializer metadata."""

        model = get_user_model()
        fields = ("id", "email", "username", "firstname", "lastname", "password")
        read_only_fields = ("id",)

    def create(self, validated_data):
        """Create a user with a bcrypt hash when bcrypt is the active hasher."""
        password = validated_data.pop("password")
        return self.Meta.model.objects.create_user(password=password, **validated_data)
