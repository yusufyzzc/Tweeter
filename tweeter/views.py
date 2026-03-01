from sqlite3 import IntegrityError

from django.shortcuts import redirect, render, get_object_or_404
from .models import Like, Tweet
from . import forms
from django.urls import reverse, reverse_lazy 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.


def list_tweets(request):
    all_tweets = Tweet.objects.all().order_by('-created_at')
    tweet_dict = {'tweets': all_tweets}
    return render(request, 'tweeter/listtweet.html', context=tweet_dict)

@login_required(login_url='/login')
def add_tweet(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        content = request.POST.get('content')
        new_tweet = Tweet(nickname=nickname, content=content)
        new_tweet.save()
    return render(request, 'tweeter/addtweet.html')

def add_tweet_with_form(request):
    if request.method == 'POST':
        form = forms.AddTweetForm(request.POST)
        if form.is_valid():
            nickname = form.cleaned_data['nickname_input']
            content = form.cleaned_data['content_input']
            new_tweet = Tweet(nickname=nickname, content=content)
            new_tweet.save()
    else:
        form = forms.AddTweetForm()
    
    return render(request, 'tweeter/addtweetwithform.html', {'form': form})

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
    
def like_tweet(request, pk):
    tweet = get_object_or_404(Tweet, pk=pk)
    tweet.likes += 1
    tweet.save()
    return redirect("tweeter:list_tweets")

@login_required
def toggle_like(request, pk):
    if request.method != "POST":
        return redirect("tweeter:list_tweets")

    tweet = get_object_or_404(Tweet, pk=pk)

    like = Like.objects.filter(user=request.user, tweet=tweet).first()
    if like:
        # UNLIKE
        like.delete()
        if tweet.likes > 0:
            tweet.likes -= 1
            tweet.save(update_fields=["likes"])
    else:
        # LIKE
        try:
            Like.objects.create(user=request.user, tweet=tweet)
            tweet.likes += 1
            tweet.save(update_fields=["likes"])
        except IntegrityError:
            pass

    return redirect("tweeter:list_tweets")

def list_tweets(request):
    tweets = Tweet.objects.order_by("-created_at")

    liked_ids = set()
    if request.user.is_authenticated:
        liked_ids = set(
            Like.objects.filter(user=request.user).values_list("tweet_id", flat=True)
        )

    return render(request, "tweeter/listtweet.html", {
        "tweets": tweets,
        "liked_ids": liked_ids,
    })