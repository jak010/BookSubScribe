from rest_framework.exceptions import APIException


class AlreadyExistCompanyName(APIException):
    status_code = 400
    default_detail = "AlreadyExistCompanyName"
    default_code = "AlreadyExistCompanyName"
