"""situationroom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from apps.situationroom_user.rest.api import LoginView, RegistrationView
from django.conf import settings
from django.conf.urls.static import static
from knox import views as knox_views

from apps.upload.views import image_upload

urlpatterns = [
    path("", image_upload, name="upload"),
    path("auth/login/", LoginView.as_view(), name="knox_login"),
    path("auth/register/", RegistrationView.as_view(), name="knox_register"),
    path("auth/logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("auth/logoutall/", knox_views.LogoutAllView.as_view(), name="knox_logoutall"),
    path("admin/", admin.site.urls),
    path("api/v1/", include("apps.situationroom_user.rest.urls")),
    path("api/v1/", include("apps.team.rest.urls")),
    path("api/v1/", include("apps.player.rest.urls")),
    path("heartbeat/", include("apps.common.rest.urls")),
    path("api/", include("rest_framework.urls")),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
