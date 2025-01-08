from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from pyexpat.errors import messages
from blogapp.models import ProfileUser,Post,Comment
from blogapp.forms import PostForm,CommentForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def ProfileView(request,pk):

    profile=ProfileUser.objects.get(pk=pk)

    posts=Post.objects.filter(author=profile.username).order_by('-date_posted')

    return render(request,"admin/profile_view.html",{"profile":profile,"posts":posts})




def ProfileDelete(request,pk):

    profile=ProfileUser.objects.get(pk=pk)

    if request.method=='POST':
        send_mail(
            subject="Your Profile Account Has been Deleted",
            message=(f" Dear {profile.first_name} {profile.last_name},\n \n" "Your profile has been deleted by the admin." " If you have any questions, Please contact support."),
            from_email="arshidafsalk@gmail.com",
            recipient_list=[profile.email],
            fail_silently=False,
        )
        profile.username.delete()
        profile.delete()

        messages.success(request, f"The profile of {profile.username} has been successfully deleted.")
        return redirect('admin_bloglist')

    return render(request,"admin/profile_confirm_delete.html",{'profile':profile})





def Bloglist(request):

    posts=Post.objects.all()

    return render(request,"admin/bloglist.html",{"posts":posts})




def PostView(request,post_id):

    post=Post.objects.get(id=post_id)

    return render(request,"admin/post_detailview.html",{"post":post})





def PostDelete(request,post_id):

    post=Post.objects.get(id=post_id,author=request.user)

    if request.method=='POST':
        post.delete()
        return redirect('admin_bloglist')

    return render(request,"admin/post_confirm_delete.html",{'post':post})