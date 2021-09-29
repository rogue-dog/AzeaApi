"""AzeaApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from UserApi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check/email', views.checkEmailAndSendOTP.as_view()),
    path('check/otp', views.CheckOTP.as_view()),
    path('create/acc', views.LoginAndSignUp.as_view()),
    path('log/in', views.LoginAndSignUp.as_view()),
    path('check/username', views.checkUsername.as_view()),
    path('post/create', views.PostCreationAndRetrieve.as_view()),
    path('contact', views.ContactUs.as_view())
]
