from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Url

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "password"]


class UrlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields =  ["long_url", "url_code", "date_created"]