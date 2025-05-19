"""
URL configuration for community project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from board.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', post_list),
    path('board/post/create/', post_create),
    path('board/post/detail/{post_id}/', post_detail),
    path('board/post/update/{post_id}/', post_update),
    path('board/post/delete/{post_id}/', post_delete),
    path('board/comment/create/{post_id}/', comment_create),
    path('board/comment/list/{post_id}/', comment_list)  
]
