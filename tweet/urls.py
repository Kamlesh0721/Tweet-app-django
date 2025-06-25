from django.urls import path
from django.contrib.auth import views as auth_views
from tweet import views

app_name = 'tweet'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tweet/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='tweet/logout.html'), name='logout'),
    path('force-logout/', views.force_logout, name='force_logout'),
]
