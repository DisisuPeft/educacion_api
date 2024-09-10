from django.contrib.auth.models import User
from rest_framework import serializers
# from .models import

class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = User
        fields = ["id", "email", "password", "username"]
        # extra_kwargs = {
        #     "password": {"write_only": True, "min_length": 5},
        # }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("El email ya se encuentra registrado")
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError("Este nombre de usuario ya se encuentra registrado.")
        return value
        # extra_kwargs = {"password": {"max_length": 20, "min_length": 5}}
        #
        # def create(self, validated_data):
        #     user = User.objects.create_user(
        #         email=validated_data["email"],
        #         password=validated_data["password"],
        #         username=validated_data["username"]
        #     )
        #     return user
