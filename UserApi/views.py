import re
from django.http.request import HttpRequest
from rest_framework.response import Response
from UserApi import models
from UserApi.serializers import UserSerializer
from UserApi.models import User, UserVerification, Post
from django.shortcuts import render
from rest_framework import generics
from .send_otp import check_otp, verify_email
from .jwt_code import encode
from UserApi import jwt_code, decode_jwt
# Create your views here.


class checkEmailAndSendOTP(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:
            email = request.headers['email']
            message, response = verify_email(email)
        except:
            message = "Error"
            response = "bad_request"

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
        try:
            email = request.headers['email']
            otp = request.headers['otp']

        except:
            return Response({"message": "Some Error Occurred", "status": "failed", "response": "bad_request"})

        message, verified, status = check_otp(email, otp)

        return Response({"message": message, "status": status, "response": verified})


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
            return Response({"message": "Your Account has been Created", "token": token, "status": "success"})
        except:
            return Response({"message": "Some Error Occurred", "status": "failed"})

            # LoginAPI

    def get(self, request, *args, **kwargs):
        try:

            text = request.headers['text']
            password = request.headers['password']
            user = User.objects.filter(email=text, password=password).exists()
            user1 = User.objects.filter(
                username=text, password=password).exists()
        except:
            resp = {"status": "failed", "message": "Some Error Occurred ",
                    "response": "Bad_Request"}
            return Response(resp)
        if(user):
            user = User.objects.get(email=text)
            token = encode({"userid": getattr(user, "id")})
            details = {"message": "Logging In...",
                       "body":
                       {
                           "name": getattr(user, "name"),
                           "username": text,
                           "email": getattr(user, "email"),
                           "token": token},


                       "status": "success"
                       }
            return Response(details)

            # Check If Username & Password is there.

        if(user1):
            user = User.objects.get(username=text)
            token = encode({"userid": getattr(user, "id")})
            details = {"message": "Logging In...",
                       "body":
                       {
                           "name": getattr(user, "name"),
                           "username": text,
                           "email": getattr(user, "email"),
                           "token": token
                       },


                       "status": "success"
                       }
            return Response(details)
        return Response({"message": "Incorrect Credentials", "status": "success", "response": "Incorrect_Credentials"})

        # Check For Username


class checkUsername(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        message = "Available"
        response = "Valid_Username"
        try:
            isexists = User.objects.filter(
                username=request.headers['username']).exists()
        except:
            return Response({"message": "Error While Fetching Data!", "status": "failed", "response": "Error_while_retrieving_the_data"})

        if(isexists):
            message = "Unavailable"
            response = "Username_Taken"
        return Response({"message": message, "status": "success", "response": response})


# UPLOAD A POST

class PostCreationAndRetrieve(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            id, status = decode_jwt.decode(data['token'])
            if(not status):
                message, status, response = "Some Error Occurred", "failed", "Error"
            file = data['file']
            category = data['category']
            post = Post(uploader_id=id, file=file, category=category)
            post.save()
            message, status, response = "Post Created SUccessfully", "success", "Post_Created"
        except:
            message, status, response = "Some Error Occurred", "failed", "Error"
        return Response({"message": message, "status": status, "response": response})
