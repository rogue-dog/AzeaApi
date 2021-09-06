
from django.db import models
from django.core.validators import validate_comma_separated_integer_list

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=250)
    email = models.CharField(max_length=250)

    name = models.CharField(max_length=250)

    password = models.CharField(max_length=250)

    def __str__(self):
        return self.username


class UserVerification (models.Model):

    email = models.CharField(max_length=250, primary_key=True)
    otp = models.CharField(max_length=250)


class Post(models.Model):
    file = models.FileField()
    uploader_id = models.CharField(max_length=100)
    category = models.CharField(max_length=10)
    likes = models.CharField(null=True, validators=[
                             validate_comma_separated_integer_list], default="", max_length=10000)
    comments = models.JSONField(default='{  }')
    timestamp = models.CharField(max_length=30)
