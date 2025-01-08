from django.contrib.auth.forms import UserCreationForm
from .models import ProfileUser,Post,Comment
from django import forms
from django.contrib.auth.models import User



class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['username','email','password1','password2']



class LoginForm(forms.Form):

    username = forms.CharField()
    password = forms.CharField()



class ProfileForm(forms.ModelForm):

    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)


    class Meta:
        model = ProfileUser
        fields = '__all__'




class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','image','content']



class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['comments']