from django.urls import path
from .views import profile, about_me, gallery, contact_me,reply_contacts


urlpatterns = [
    path('profile/<str:pk>/', profile, name='profile'),
    path('about-me/<str:pk>/', about_me, name='about-me'),
    path('contact/', contact_me, name='contact'),
    path('reply-contact/<str:pk>/', reply_contacts, name='reply-contact'),
    path('gallery/', gallery, name='gallery'),
]
