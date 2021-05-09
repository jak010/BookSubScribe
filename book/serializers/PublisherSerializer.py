from ..models import PublisherProfile
from django.contrib.auth import get_user_model
from rest_framework import serializers
from exceptions.auth_exception import EmptyValueException

User = get_user_model()


class PublisherProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublisherProfile
        fields = ['pub_name']

    def create(self, data):
        if not data:
            raise EmptyValueException

        user = data.get("user")
        pub_name = data.get("pub_name")

        PublisherProfile.objects.create(user=user, pub_name=pub_name)
