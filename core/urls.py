"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_username/', check_username, name='check_username'),
    path('login/', sign_in, name='login'),
    path('saveProfileInfo/', saveProfileInfo, name='saveProfileInfo'),
    path('check_old_password/', check_old_password, name='check_old_password'),
    path('guest_login/', guest_login, name='guest_login'),
    path('logout/', sign_out, name='logout'),
    path('changePassword/', changePassword, name='changePassword'),
    path('register/', sign_up, name='register'),
    path("__reload__/", include("django_browser_reload.urls")),
    path('', home, name="home"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)