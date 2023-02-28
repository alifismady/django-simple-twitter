from django.urls import path

from tweet_api.views import home_view,tweet_detail_view,tweet_list_view,tweet_create_view,delete_tweet,update_tweet,profile_view,tweet_user_view,delete_tweet_user,update_tweet_user

app_name = 'tweet_api'

urlpatterns = [
    path('',home_view,name='home_view'),
    path('tweet/',tweet_list_view,name="list_tweet"),
    path('create-tweet/',tweet_create_view,name='tweet_create'),
    path('tweet/<int:tweet_id>',tweet_detail_view, name="tweet_detail"),
    path('delete/<int:tweet_id>',delete_tweet,name="delete_tweet"),
    path('update/<int:tweet_id>',update_tweet,name="update_tweet"),
    path('profile/',profile_view,name="profile_view"),
    path('profile/tweet/',tweet_user_view,name="tweet_user"),
    path('profile/delete/<int:tweet_id>',delete_tweet_user,name="delete_tweet_user"),
    path('profile/update/<int:tweet_id>',update_tweet_user,name="update_tweet_user"),
]