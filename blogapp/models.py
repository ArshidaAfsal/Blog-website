from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.


class ProfileUser(models.Model):

    username = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    first_name = models.CharField(max_length=200,null=True)
    last_name = models.CharField(max_length=200,null=True)
    email = models.EmailField(null=True)
    profile_pic = models.ImageField(upload_to="media",null=True)
    contact_number = models.CharField(max_length=15,null=True)
    password1 = models.CharField(max_length=15)
    password2 = models.CharField(max_length=15)



class Post(models.Model):

    title = models.CharField(max_length=200)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="media",null=True)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author.username}'




