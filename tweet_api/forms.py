from django import forms

from .models import TweetModel

MAX_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = TweetModel
        fields = "__all__"
    
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > MAX_LENGTH:
            raise forms.ValidationError("Tweet too long")
        return content