"""greenhousebackend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from greenhousebackend.views.auth import register_user, check_user
from greenhousebackend.views.user import UserView
from rest_framework import routers
from greenhousebackend.views.tag import TagView


router = routers.DefaultRouter(trailing_slash=False)
router.register(r'tags', TagView, 'tag')
router.register(r'users', UserView, 'user')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('checkuser', check_user, name='checkuser'),
    path('register', register_user),
    path('', include(router.urls)),
    
]
