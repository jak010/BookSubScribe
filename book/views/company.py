from rest_framework.views import APIView
from rest_framework.response import Response
from accounts.authentication import CustomJSONWebTokenAuthentication
from ..models import PublishCompany
from django.contrib.auth import get_user_model
from ..models import Book
from django.db import IntegrityError
from exceptions._company import AlreadyExistCompanyName


class CompanyRegister(APIView):

    def post(self, request, formant=None):
        company_name = request.data.get("company_name")

        try:
            if company_name is not None:
                PublishCompany.objects.create(pub_company=company_name, pub_descript="Test Create")
        except IntegrityError as err:
            raise AlreadyExistCompanyName

        return Response({"status": 200})
