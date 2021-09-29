from django.contrib import admin
from .models import Contact, User, UserVerification, Post

# Register your models here.
admin.site.register(User)
admin.site.register(UserVerification)
admin.site.register(Post)
admin.site.register(Contact)
