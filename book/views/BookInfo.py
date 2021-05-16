from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.authentication import CustomJSONWebTokenAuthentication

from django.contrib.auth import get_user_model
from faker import Faker
from ..models import Book

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


class BookManager(APIView):

    def post(self):
        """ 이 API는 데이터 생성 용으로 만들어 놓은 것
         호출을 받으면 자동으로 생성
        """



