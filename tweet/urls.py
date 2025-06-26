from django.urls import path
from django.contrib.auth import views as auth_views
from tweet import views

app_name = 'tweet'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='tweet/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('tweet/<int:tweet_id>/edit/', views.edit_tweet, name='edit_tweet'),
    path('tweet/<int:tweet_id>/delete/', views.delete_tweet, name='delete_tweet'),
]
