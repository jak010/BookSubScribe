from django.conf.urls import url

from .views import (
    ObtainToken
)

urlpatterns = [
    url(r'token$', ObtainToken.as_view()),
]
