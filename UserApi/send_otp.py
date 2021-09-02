from validate_email import validate_email
from django.core.mail import message, send_mail
from .models import User, UserVerification
import random


def verify_email(email):
    v = validate_email(email, verify=True)
    if(v):
        if(User.objects.filter(email=email).exists()):
            return "Old"
        else:
            otp = str(random.randint(1000, 9999))
            message = "Your OTP for Email Verification is "+otp
            try:
                send_mail("Email Verification - Azea", message,
                          "azeaapp@gmail.com", [email])

                if(UserVerification.objects.filter(email=email).exists()):
                    User.objects.filter(email=email).delete()

                userV = UserVerification(email=email, otp=otp)
                userV.save()
                return "New"

            except:
                return ("Error")
    return "Invalid Email"


def check_otp(email, otp):
    if(UserVerification.objects.filter(email=email, otp=otp).exists()):
        return "Right"
    return "Wrong"
