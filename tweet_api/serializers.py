from rest_framework import serializers
from tweet_api.models import TweetModel

class TweetSerializer(serializers.ModelSerializer):

    def getUsername(self,obj):
        return obj.user.username

    username = serializers.SerializerMethodField("getUsername")

    class Meta:
        def getUsername(self,obj):
            return obj.user.username

        username = serializers.SerializerMethodField("getUsername")
        model = TweetModel
        fields = ('id','content','dateCreated', 'username')
        