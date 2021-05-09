from rest_framework.exceptions import APIException


class EmptyValueException(APIException):
    status_code = 400
    default_detail = "Empty Value"
    default_code = "Bad Request"


class InvalidCredential(APIException):
    status_code = 400
    default_detail = "Invalid Credential"
    default_code = "Bad Request"


class AuthenticationNotFoundException(APIException):
    status_code = 400
    default_detail = "Invalid ID or Password"
    default_code = "NotFound"
