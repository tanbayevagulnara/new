from django.urls import path
from . import views

app_name = 'my_app'

urlpatterns = [
    path('email/', views.first),
    path('home/', views.home, name='home'),
    path('register/', views.register_request, name='register'),
    path('login/', views.login_request, name='login'),
    path('', views.main, name='main'),
]
