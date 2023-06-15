from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home" ),
    path('blog/', views.blog, name='blog'),
    path('create-post/', views.create_post, name="create-post"),
    path('post/<str:pk>/', views.post, name="post"),
    path('update-post/<str:pk>/', views.update_post, name="update-post"),
    path('liked-post/', views.liked_post, name='liked-post'),
    path('delete-post/<str:pk>/', views.delete_post, name='delete-post'),
    path('replies/<str:pk>/', views.reply_comment, name='replies'),
    
    path('contact-us', views.contact_us, name='contact-us'),
]
