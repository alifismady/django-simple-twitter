from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import TweetModel
from .forms import TweetForm
from .serializers import TweetSerializer

# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")
    form = TweetForm()
    context={
        'form':form
    }
    return render(request,"pages/home.html",context)

@api_view(['GET'])
def tweet_list_view(request):
    query = TweetModel.objects.all()
    serializer = TweetSerializer(query,many=True)
    return Response(serializer.data,status=200)

@api_view(['POST'])
def tweet_create_view(request):
    serializer = TweetSerializer(data=request.POST)
    
    if serializer.is_valid():
        serializer.save()
        return HttpResponseRedirect(redirect_to="/")
        # return Response(serializer.data)
    return Response({})

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
