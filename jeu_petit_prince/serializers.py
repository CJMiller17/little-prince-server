from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    account_name = UserSerializer(read_only=True)
    
    class Meta:
        model = Profile
        fields = '__all__'