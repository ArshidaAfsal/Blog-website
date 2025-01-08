
from django.urls import path
from adminapp import views


urlpatterns = [

    path('admin_blolist/',views.Bloglist,name="admin_bloglist"),
    path('postdetail/<int:post_id>/',views.PostView,name="admin_postview"),
    path('deleteview/<int:post_id>/',views.PostDelete,name="admin_postdelete"),
    path('profileView/<int:pk>/',views.ProfileView,name="profile_view"),
    path('profiledelete/<int:pk>/',views.ProfileDelete,name="profile_delete")


]