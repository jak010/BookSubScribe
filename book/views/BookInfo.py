from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication




class Profile(APIView):
    authentication_classes = (JSONWebTokenAuthentication,)

    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)
