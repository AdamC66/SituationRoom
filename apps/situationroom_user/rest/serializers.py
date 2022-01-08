from apps.situationroom_user.models import SituationRoomUser
from rest_framework import serializers
from situationroom import settings
from knox.models import AuthToken
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationRoomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "code",
            "company",
            "avatar",
        ]

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationRoomUser
        fields = [
            "first_name",
            "last_name",
            "email",
            "code",
            "company",
            "avatar",
            "address_line_1",
            "address_line_2",
            "address_city",
            "address_state",
            "address_zip",
            "address_country",
            "address_phone",
        ]

class TokenSerializer(serializers.ModelSerializer):
    auth_token = serializers.CharField(source="token_key")

    class Meta:
        model = AuthToken
        fields = ("auth_token",)

class CreateUserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=30, required=True)
    password = serializers.CharField(max_length=30, required=True)
    confirm_password = serializers.CharField(max_length=30, required=True)
    email = serializers.EmailField(max_length=255, required=True)

    def validate(self, attrs):
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")
        if len(password) < 5 or len(confirm_password) < 5:
            raise serializers.ValidationError({"password": "Password must be at least 6 characters long"})
        if password != confirm_password:
            raise serializers.ValidationError({"confirm_password": "Passwords must match"})
            
        return super().validate(attrs)