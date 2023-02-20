from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from .models import TweetModel
from .forms import TweetForm

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    form = TweetForm()
    context={
        'form':form
    }
    return render(request,"pages/home.html",context)

def tweet_list_view(request):
    query = TweetModel.objects.all()
    tweet_list = [{"id":tweet.id,"content":tweet.content, "dateCreated":tweet.dateCreated} for tweet in query]
    data = {
        "response":tweet_list,
    }
    return JsonResponse(data)

def tweet_create_view(request):
    form = TweetForm(request.POST or None)
    print(next_url, "-> next url")
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        return redirect("/")
        form = TweetForm()
    context={
        'form':form,
    }
    return render(request,"pages/home.html",context)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    print(args,kwargs)
    data = {
        "id": tweet_id,
        
        
    }
    status = 200
    try:
        obj = TweetModel.objects.get(id=tweet_id)
        data["content"] = obj.content
    except:
        data["message"] = "Not Found"
        status = 404

    return JsonResponse(data,status=status)
