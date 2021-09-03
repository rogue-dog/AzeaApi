from validate_email import validate_email
from django.core.mail import message, send_mail
from .models import User, UserVerification
import random


def verify_email(email):
    v = validate_email(email)

    if(v):
        if(User.objects.filter(email=email).exists()):
            return ("Old", "existing_user")
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
                return ("New", "new_user")

            except:
                return("Error", "Error")
    return ("Invalid Email", "Error")


def check_otp(email, otp):
    try:
        isexists =UserVerification.objects.filter(email=email, otp=otp).exists()
    except:
        return ("Error","Not Verified")
    if(isexists):
        return ("Right","Email_Verified")
    return ("Wrong","Incorrect_OTP")
