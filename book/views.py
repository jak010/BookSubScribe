from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers.AuthSerializers import UserLoginSerializer


# from rest_framework_jwt.js


class ObtainToken(APIView):

    def post(self, request):
        serializer = UserLoginSerializer()
        if (token := serializer.validate(data=request.data)) is not None:
            return Response({"access-token": token})
        return Response({"msg": "msg"})
