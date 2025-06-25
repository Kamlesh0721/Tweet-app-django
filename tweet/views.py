from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from .models import Tweet

class Home(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'tweet/home.html', {'tweets': tweets})
    
    def post(self, request):
        if not request.user.is_authenticated:
            messages.error(request, 'You must be logged in to post a tweet!')
            return redirect('tweet:login')
        content = request.POST.get('tweet_content', '').strip()
        
        if not content:
            messages.error(request, 'Tweet content cannot be empty!')
            return redirect('tweet:home')
        
        if len(content) > 280:
            messages.error(request, 'Tweet cannot exceed 280 characters!')
            return redirect('tweet:home')
        
        Tweet.objects.create(
            content=content,
            author=request.user
        )
        messages.success(request, 'Tweet posted successfully!')
        return redirect('tweet:home')

class TweetListView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

def force_logout(request):
    """Force logout and redirect to login page"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('tweet:login')

# Create your views here.
