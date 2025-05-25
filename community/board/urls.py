from django.urls import path
from . import views

urlpatterns = [
  path('', views.post_list),
  path('post/create/', views.post_create),
  path('post/detail/<int:pk>/', views.post_detail),
  path('post/update/<int:pk>/', views.post_update),
  path('post/delete/<int:pk>/', views.post_delete),
  path('comment/create/<int:post_id>/', views.comment_create),
  path('comment/list/<int:post_id>/', views.comment_list),

]