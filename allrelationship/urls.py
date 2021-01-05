"""allrelationship URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp.views import home,show_user_data,show_page_data,show_post_data,show_song_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('user/',show_user_data,name='user'),
    path('page/',show_page_data,name='page'),
    path('post/',show_post_data,name='post'),
    path('song/',show_song_data,name='song'),
]
