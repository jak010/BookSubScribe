from django.db import models
from django.contrib.auth.models import AbstractBaseUser


# Create your models here.

class User(AbstractBaseUser):
    # 앞에는 DB에 저장되는 값
    # 뒤에는 페이지나 폼에서 표시하는 값
    DEFINE_USER_TYPE = (
        ("Publisher", "Publisher"),
        ("Subscriber", "Subscriber")
    )

    email = models.EmailField(max_length=50, verbose_name="User Email", unique=True)
    uuid = models.UUIDField(max_length=32, editable=False, verbose_name="User UUID")
    type = models.CharField(max_length=20, choices=DEFINE_USER_TYPE, default=DEFINE_USER_TYPE[1][1])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
