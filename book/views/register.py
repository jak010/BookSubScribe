from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
# from ..models import PublisherProfile
from ..serializers.PublisherSerializer import PublisherProfileSerializer
from exceptions.auth_exception import EmptyValueException

User = get_user_model()


class Register(APIView):

    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        pub_name = request.data.get("pub_name")

        if not (email and password):
            raise EmptyValueException

        if (user := User.objects.create_user(email=email, password=password)) is not None:
            serializer = PublisherProfileSerializer(data={"pub_name": pub_name})
            if serializer.is_valid():
                serializer.create(data={"user": user, "pub_name": pub_name})
            else:
                return Response({"desc": serializer.errors})
        return Response({"desc": "User Success"})
