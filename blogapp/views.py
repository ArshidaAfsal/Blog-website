from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegistrationForm,LoginForm,ProfileForm,PostForm,CommentForm
from .models import ProfileUser,Post,Comment
from django.views.generic import View,CreateView,FormView,UpdateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.


class UserRegister(CreateView):

    template_name = 'blog/register.html'
    form_class = RegistrationForm
    model = User
    success_url = reverse_lazy("login")





def Login(request):

    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)

            if not ProfileUser.objects.filter(username=user).exists():
                return redirect('profile')

            return redirect('bloglist')

        else:
            messages.error(request,"Invalid username or password")
            return redirect('login')
    return render(request, 'blog/login.html')




def createProfile(request):
    profile=ProfileUser.objects.all()
    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password1=form.cleaned_data.get('password1')
            password2=form.cleaned_data.get('password2')

            if password1 != password2:
                messages.error(request,"Passwords do not match!")
                return render(request,"blog/profile.html",{"form":form,"profile":profile})
            if ProfileUser.objects.filter(username=username).exists():
                messages.error(request,"Username already exists")
                return render(request, "blog/profile.html", {"form": form, "profile": profile})

            form.save()
            messages.success(request,"Profile Created Successfully!")
            return redirect('bloglist')
        else:
            messages.error(request,"Invalid data submitted!")
    else:
        form=ProfileForm()
    return render(request,"blog/profile.html",{"form":form,"profile":profile})


@login_required
def ProfileView(request,pk):

    profile=ProfileUser.objects.get(pk=pk)

    if profile.username != request.user:
        return redirect('')

    posts=Post.objects.filter(author=profile.username).order_by('-date_posted')

    return render(request,"blog/profileview.html",{"profile":profile,"posts":posts})




def UpdateProfile(request,pk):

    profile=ProfileUser.objects.get(pk=pk)

    if request.method=='POST':
        form=ProfileForm(request.POST,request.FILES,instance=profile)

        if form.is_valid():
            form.save()
            return redirect("profileview",pk=pk)
    else:
        form=ProfileForm(instance=profile)
    return render(request,"blog/profile_update.html",{"form":form,"profile":profile})




def index(request):

    return render(request,"blog/base.html")



@login_required
def createPost(request):

    if request.method=='POST':
        form=PostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False) # Dont save to db yet
            post.author=request.user     # set the logged-in user as the author
            post.save()
            return redirect('bloglist')
    else:
        form=PostForm()
    return render(request,"blog/create_post.html",{"form":form})



@login_required
def PostView(request,post_id):

    post=Post.objects.get(id=post_id)

    return render(request,"blog/view_post.html",{"post":post})





def PostUpdate(request,post_id):

    post=Post.objects.get(id=post_id,author=request.user)

    if request.method=='POST':
        form=PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('bloglist')

    else:
        form=PostForm(instance=post)
    return render(request,"blog/post_update.html",{"form":form})




def PostDelete(request,post_id):

    post=Post.objects.get(id=post_id,author=request.user)

    if request.method=='POST':
        post.delete()
        return redirect('bloglist')

    return render(request,"blog/confirm_delete.html",{'post':post})





def add_comment(request,post_id):

    post=Post.objects.get(id=post_id)

    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=form.save(commit=False)
            comment.post=post
            comment.author=request.user
            comment.save()
            return redirect('bloglist')
    else:
        form=CommentForm()
    return render(request,"blog/view_post.html",{"form":form,"post":post})



def blogs(request):
    posts = Post.objects.all()
    posts = Post.objects.filter().order_by('-date_posted')
    return render(request,"blog/bloglist.html", {'posts':posts})





def Logout(request):

    logout(request)
    return redirect('login')

