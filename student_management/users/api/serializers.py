from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "name", "url"]

        extra_kwargs = {
            "url": {"view_name": "api:user-detail", "lookup_field": "username"}
        }


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "password" : {"write_only" : True},
        }

    def validate(self, data):
        validated_data = data
        password = validated_data.get("password", "")
        if not password:
            raise serializers.ValidationError({"password" : "Password is required"})
        
        password2 = validated_data.get("password2", "")
        if not password2:
            raise serializers.ValidationError({"password2" : "Password is required"})

        if password != password2:
            raise serializers.ValidationError({"password" : "Password and Confirm password does not match"})
        return validated_data

    def validate_email(self, value):
        mail_exist = User.objects.filter(email=value).exists()
        if mail_exist:
            raise serializers.ValidationError("Email already exist.")
        return value

    def save(self):
        validated_data = self.validated_data
        account = User(email = validated_data["email"], username = validated_data["username"])
        account.set_password(validated_data["password"])
        account.save()
        return account
