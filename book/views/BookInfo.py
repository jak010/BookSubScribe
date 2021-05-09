from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.authentication import CustomJSONWebTokenAuthentication

from django.contrib.auth import get_user_model

User = get_user_model()

class Profile(APIView):
    authentication_classes = (CustomJSONWebTokenAuthentication,)

    def get(self, request):
        content = {"message": "Hello World"}
        # from pprint import pprint
        # pprint(dir(request.session))

        profile = User.objects.get(email=request.user)
        print(profile.password)
        return Response(content)
