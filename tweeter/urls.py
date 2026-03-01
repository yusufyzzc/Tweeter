from django.urls import path
from . import views

app_name = 'tweeter'


urlpatterns = [
    path('', views.list_tweets, name='list_tweets'),      # myurl.com/tweeter/
    path('addtweet/', views.add_tweet, name='add_tweet'), # myurl.com/tweeter/addtweet/
    path('addtweetwithform/', views.add_tweet_with_form, name='add_tweet_with_form'), # myurl.com/tweeter/addtweetwithform/
    path('signup/', views.SignUpView.as_view(), name='signup'), # myurl.com/tweeter/signup/
    path("like/<int:pk>/", views.like_tweet, name="like_tweet"), # myurl.com/tweeter/like/1/ (örneğin 1 id'li tweet'i beğenmek için)
    path("toggle-like/<int:pk>/", views.toggle_like, name="toggle_like"),
]