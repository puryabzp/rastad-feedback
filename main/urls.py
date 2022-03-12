from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.contrib.auth import authenticate, login
admin.autodiscover()
handler404 = 'userprofile.views.error_404'
urlpatterns = [
    path('xviv/', admin.site.urls),
    path('', include('userprofile.urls')),
    path('course/', include('bootcamp.urls')),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) 
