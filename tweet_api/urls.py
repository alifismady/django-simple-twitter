from django.urls import path

from tweet_api.views import home_view,tweet_detail_view

app_name = 'tweet_api'

urlpatterns = [
    path('',home_view,name='home_view'),
    path('tweet/<int:tweet_id>',tweet_detail_view, name="tweet_detail"),
]