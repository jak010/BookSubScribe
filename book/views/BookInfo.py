from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from accounts.authentication import CustomJSONWebTokenAuthentication


class Profile(APIView):
    authentication_classes = (CustomJSONWebTokenAuthentication,)

    def get(self, request):
        content = {"message": "Hello World"}
        return Response(content)
