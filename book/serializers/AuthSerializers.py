from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('email', 'password')

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)

        if (email is not None) and (password is not None):
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)

                return token
