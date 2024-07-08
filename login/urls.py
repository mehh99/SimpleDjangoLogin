# urls.py dalam aplikasi login atau aplikasi yang sesuai

from django.urls import path
from login import views

app_name = 'auth'  # Atur namespace sesuai kebutuhan aplikasi Anda

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),  # URL untuk halaman login
    path('register/', views.register, name='register'),  # URL untuk halaman registrasi
    path('logout/', views.logout_view, name='logout'),  # URL untuk proses logout
    
]
