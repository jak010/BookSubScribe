from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .manager import UserManger

# 앞에는 DB에 저장되는 값
# 뒤에는 페이지나 폼에서 표시하는 값
class TypeDefine(object):
    USER_TYPES = (
        ("Publisher", "Publisher"),
        ("Subscriber", "Subscriber")
    )


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, verbose_name="User Email", unique=True)
    uuid = models.UUIDField(max_length=32, editable=False, verbose_name="User UUID")
    type = models.CharField(max_length=20, choices=TypeDefine.USER_TYPES, default=None)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManger()

    def __str__(self):
        return self.email

# class SubscriberManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=TypeDefine.USER_TYPES[1][1])
#
#
# class Subscriber(User):
#     objects = SubscriberManager()
#
#     class Meta:
#         proxy = True
#
#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.type = TypeDefine.USER_TYPES[1][1]
#         return super().save(*args, **kwargs)
#
#
# class SubscriberAttribute(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     pub_name = models.CharField(max_length=50, verbose_name="Publisher Name")
#     create_time = models.DateTimeField(auto_now_add=True)  # 레코드 생성 시 시간 자동 저장
#     modify_time = models.DateTimeField(auto_now=True)  # 레코드 갱신 시 현재 시간 저장
