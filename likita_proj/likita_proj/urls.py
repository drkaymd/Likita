from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('', include('authy.urls')),
    path('', include('profiles.urls')),
    path('', include('chat.urls')),
    path('verification/', include('verify_email.urls')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
