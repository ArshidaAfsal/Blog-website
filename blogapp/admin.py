from django.contrib import admin
from .models import ProfileUser,Post,Comment

# Register your models here.

admin.site.register(ProfileUser)
admin.site.register(Post)
admin.site.register(Comment)