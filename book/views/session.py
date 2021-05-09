from django.utils import timezone
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_jwt.settings import api_settings

from exceptions import auth_exception

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class ObtainToken(APIView):

    def post(self, request):
        """ JWT 토큰 발급 """
        email = request.data.get("email", None)
        password = request.data.get("password", None)

        # value validation
        if not (email and password):
            raise auth_exception.EmptyValueException

        user = User.objects.get(email=email)

        if check_password(password, user.password):
            payload = jwt_payload_handler(user)
            user.last_login = timezone.now()
            user.save()
        else:
            raise auth_exception.InvalidCredential()

        return Response({
            "access-token": "JWT " + jwt_encode_handler(payload)
        })

