from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Tweet
from .forms import TweetForm, TweetEditForm

@method_decorator(login_required, name='dispatch')
class Home(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        tweet_form = TweetForm()
        return render(request, 'tweet/home.html', {
            'tweets': tweets,
            'tweet_form': tweet_form
        })
    
    def post(self, request):
        tweet_form = TweetForm(request.POST)
        if tweet_form.is_valid():
            tweet = tweet_form.save(commit=False)
            tweet.author = request.user
            tweet.save()
            messages.success(request, 'Tweet posted successfully!')
            return redirect('tweet:home')
        else:
            tweets = Tweet.objects.all()
            return render(request, 'tweet/home.html', {
                'tweets': tweets,
                'tweet_form': tweet_form
            })

class TweetListView(View):
    def get(self, request):
        tweets = Tweet.objects.all()
        return render(request, 'tweet/tweet_list.html', {'tweets': tweets})

@login_required
def edit_tweet(request, tweet_id):
    """Edit a tweet - only author or admin can edit"""
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Check if user is author or admin
    if not (request.user == tweet.author or request.user.is_staff):
        messages.error(request, 'You do not have permission to edit this tweet!')
        return redirect('tweet:home')
    
    if request.method == 'POST':
        form = TweetEditForm(request.POST, instance=tweet)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tweet updated successfully!')
            return redirect('tweet:home')
    else:
        form = TweetEditForm(instance=tweet)
    
    return render(request, 'tweet/edit_tweet.html', {
        'form': form,
        'tweet': tweet
    })

@login_required
def delete_tweet(request, tweet_id):
    """Delete a tweet - only author or admin can delete"""
    tweet = get_object_or_404(Tweet, id=tweet_id)
    
    # Check if user is author or admin
    if not (request.user == tweet.author or request.user.is_staff):
        messages.error(request, 'You do not have permission to delete this tweet!')
        return redirect('tweet:home')
    
    if request.method == 'POST':
        tweet.delete()
        messages.success(request, 'Tweet deleted successfully!')
        return redirect('tweet:home')
    
    return render(request, 'tweet/delete_tweet.html', {'tweet': tweet})

def logout_view(request):
    """Force logout and redirect to login page"""
    logout(request)
    messages.info(request, 'You have been logged out.')
    return redirect('tweet:login')

# Create your views here.
