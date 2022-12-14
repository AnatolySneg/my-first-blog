from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:post_pk>/', views.post_detail),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:post_pk>/edit/', views.post_edit, name='post_edit'),
]
