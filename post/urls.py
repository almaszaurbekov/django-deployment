from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name="post.list"),
    path('details/<uuid:id>', views.post_details, name="post.details"),
    path('create/', views.post_create, name="post.create"),
]