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
