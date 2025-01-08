from django.urls import path
from blogapp import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('', views.UserRegister.as_view(), name="register"),
    path('login/', views.Login, name="login"),
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name="blog/password_reset.html"),name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name="blog/password_reset_done.html"),name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="blog/password_reset_confirm.html"),name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="blog/password_reset_complete.html"),name="password_reset_complete"),
    path('base/',views.index,name="base"),
    path('createprofile',views.createProfile,name="profile"),
    path('profileview/<int:pk>/',views.ProfileView,name="profileview"),
    path('update_profile/<int:pk>/', views.UpdateProfile, name='update_profile'),
    path('create_post/',views.createPost,name="create_post"),
    path('post_view/<int:post_id>/',views.PostView,name="view_post"),
    path('post_update/<int:post_id>/',views.PostUpdate,name="post_update"),
    path('post_delete/<int:post_id>/',views.PostDelete,name="post_delete"),
    path('bloglist',views.blogs,name="bloglist"),
    path('add_comment/<int:post_id>/', views.add_comment, name="add_comment"),
    path('logout/',views.Logout,name="logout")


]
