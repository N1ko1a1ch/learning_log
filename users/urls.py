"""Определяет схемы URL для приложения users."""
from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # Страницы входа и выхода (встроенные представления Django)
    path('', include('django.contrib.auth.urls')),
    # Страница регистрации
    path('register/', views.register, name='register'),
]
