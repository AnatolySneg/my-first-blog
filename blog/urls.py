from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_list),
    path('post/<int:post_pk>/', views.post_detail),
    path('post/new/', views.post_new),
    # re_path(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    # re_path(r'^post/new/$', views.post_new),
]
