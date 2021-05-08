from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


# 앞에는 DB에 저장되는 값
# 뒤에는 페이지나 폼에서 표시하는 값
class TypeDefine(object):
    USER_TYPES = (
        ("Publisher", "Publisher"),
        ("Subscriber", "Subscriber")
    )


class UserManger(BaseUserManager):

    def create(self, email=None, password=None):
        if not email:
            raise ValueError("The Email must be set")
        if not password:
            raise ValueError("THe password must be set")

        user = self.model(email=email, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return self

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email must be set")
        if not password:
            raise ValueError("THe password must be set")

        user = self.model(email=email, password=password)
        user.set_password(password)
        print(user.password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return self.create_user(email, password)

    def create_superuser(self, email, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("SuperUser must have is_staff = True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("SuperUser must have is_superuser = True.")
        return self.create_user(email, password, **extra_fields)


# Create your models here.

class User(AbstractBaseUser):
    email = models.EmailField(max_length=50, null=False, blank=False, verbose_name="User Email", unique=True)
    password = models.CharField(max_length=128, verbose_name="User Password")
    type = models.CharField(max_length=20, choices=TypeDefine.USER_TYPES)

    is_superuser = models.BooleanField(default=False)

    objects = UserManger()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']

    def __str__(self):
        return self.email

    is_active = True

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
