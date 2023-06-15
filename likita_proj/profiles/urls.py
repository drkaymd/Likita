from django.urls import path
from .views import profile, about_me, gallery, contact_me,reply_contacts, subscribe, send_newsletter


urlpatterns = [
    path('profile/<str:pk>/', profile, name='profile'),
    path('about-me/', about_me, name='about-me'),
    path('contact/', contact_me, name='contact'),
    path('reply-contact/<str:pk>/', reply_contacts, name='reply-contact'),
    path('subscribe/', subscribe, name='subscribe'),
    path('send-newsletter/', send_newsletter, name='send-newsletter'),
    path('gallery/', gallery, name='gallery'),
]
