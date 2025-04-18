from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response


from .serializers import UserSerializer
from django.contrib.auth.models import User
# is a permission class that checks if the user is authenticated
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
# Middleware for authentication, they intercept the request and check if the user is authenticated
from rest_framework.authentication import (
    BasicAuthentication,
    SessionAuthentication,
    TokenAuthentication,
)

# JWTAuthentication is a class that provides authentication using JSON Web Tokens

from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # This part is for authentication and permission classes that are used to check if the user is authenticated and has permission to access the view
    # authentication_classes = [BasicAuthentication, SessionAuthentication, TokenAuthentication]
    # authentication_classes = [TokenAuthentication]
    # 
    authentication_classes = [JWTAuthentication]
    # This part is for permission classes that are used to check if the user is authenticated and has permission to access the view using JWT
    permission_classes = [IsAuthenticated]

class LoginView(APIView):
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            context = {
                'status': True,
                'content': {'username': user.username,
                            'fullname': user.first_name + ' ' + user.last_name,
                            'token': str(refresh.access_token),
                            }
            }
        else:
            context = {
                'status': False,
                'content': 'Invalid credentials'
            }
        return Response(context)
