from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name="main"),
    path('error', views.error, name="error"),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.user_update, name='profile'),
]