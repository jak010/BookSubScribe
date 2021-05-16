from django.conf.urls import url

from .views import (
    session,
    register,
    BookInfo,
    company
)

urlpatterns = [
    url(r'token$', session.ObtainToken.as_view()),
    url(r'register$', register.Register.as_view()),
    url(r'profile$', BookInfo.Profile.as_view()),

    ## Dummy Data Create - Publish Company
    url(r"data/company/create$", company.CompanyRegister.as_view())
]
