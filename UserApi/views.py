import re
from rest_framework.response import Response
from UserApi.serializers import UserSerializer
from UserApi.models import User, UserVerification
from django.shortcuts import render
from rest_framework import generics
from .send_otp import check_otp, verify_email
from .jwt_code import encode
from UserApi import jwt_code
# Create your views here.


class checkEmailAndSendOTP(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        email = request.data.get("email")
        message, response = verify_email(email)
        if(message == "Error"):
            status = "failed"
        else:
            status = "success"
        resp = {"message": message, "response":
                response, "status": status}

        return Response(resp)


class CheckOTP(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        email = request.data.get("email")
        otp = request.data.get("otp")
        message = check_otp(email, otp)

        return Response({"message": message})


class LoginAndSignUp(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        name = request.data.get("name")
        email = request.data.get("email")
        password = request.data.get("password")
        username = request.data.get("username")
        user = User(name=name, email=email,
                    password=password, username=username)
        try:
            user.save()
            UserVerification.objects.filter(email=email).delete()

            token = encode({"userid": user.id})
            return Response({"message": "Created", "token": token})
        except:
            return Response({"message": "Error"})

            # LoginAPI

    def get(self, request, *args, **kwargs):

        text = request.data.get("text")
        password = request.data.get("password")
        user = User.objects.filter(email=text, password=password).exists()
        if(user):
            user = User.objects.get(email=text)
            token = encode({"userid": getattr(user, "id")})
            details = {
                "message": "Right",
                "name": getattr(user, "name"),
                "username": getattr(user, "username"),
                "email": text,
                "token": token
            }
            return Response(details)

            # Check For Username
        user1 = User.objects.filter(username=text, password=password).exists()
        if(user1):
            user = User.objects.get(username=text)
            token = encode({"userid": getattr(user, "id")})
            details = {
                "message": "Right",
                "name": getattr(user, "name"),
                "username": text,
                "email": getattr(user, "email"),
                "token": token
            }
            return Response(details)
        return Response({"message": "Wrong"})


class checkUsername(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        message = "Yes"
        if(User.objects.filter(username=request.data.get("username")).exists()):
            message = "No"
        return Response({"message": message})
