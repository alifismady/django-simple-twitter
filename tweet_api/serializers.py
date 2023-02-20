from rest_framework import serializers
from tweet_api.models import TweetModel

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TweetModel
        fields = '__all__'