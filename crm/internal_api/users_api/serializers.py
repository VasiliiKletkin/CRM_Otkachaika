from django.contrib.auth.models import User
from rest_framework import serializers
from users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'last_name', 'first_name']

class ProfileSerializer(serializers.ModelSerializer):
 class Meta:
        model = Profile
        fields = ('__all__')
