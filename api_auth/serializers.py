from rest_framework import serializers
# import users models
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password':{'write_only':True}}

    def create (self, validated_data):
        user = User(
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(TokenObtainPairSerializer):
    @classmethod
    # classmethod is a decorator that allows you to define a method that can be called on the class itself, rather than on an instance of the class
    def get_token(cls,user):
        token = super().get_token(user)
        # add custom claims
        token['username'] = user.username
        token['fullname'] = user.first_name + ' ' + user.last_name

        return token