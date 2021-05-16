import uuid
from bpm import settings
from django.db import models

User = settings.AUTH_USER_MODEL


class PublisherProfile(models.Model):
    """
    ## Publisher User Create Example
    pub_user = Publisher.objects.create(email="pub@test.com")
    PublisherAttribute.objects.create(user=pub_user, pub_name="pub_test")
    """
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    pub_name = models.CharField(max_length=50, verbose_name="Publisher Name")
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)


class PublishCompany(models.Model):
    pub_uuid = models.UUIDField(default=str(uuid.uuid4()), verbose_name="id", primary_key=True)
    pub_company = models.CharField(max_length=15, verbose_name="Publishing Company Name",unique=True)
    pub_descript = models.CharField(max_length=30, verbose_name="Description")


class Book(models.Model):
    pub_uuid = models.UUIDField(default=str(uuid.uuid4()), verbose_name="PublishCompany")
    book_name = models.CharField(max_length=50, verbose_name="Book Name")
