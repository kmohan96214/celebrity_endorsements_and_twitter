from django.shortcuts import render
from django.http import JsonResponse,HttpResponseRedirect
from . import helpers
from django.urls import reverse
# Create your views here.
GMAP_API_KEY = 'YOUR GMAP API KEY HERE'

def home(request):
    return render(request,'home.html')

def index(request):
    return render(request,'index.html',{'key':GMAP_API_KEY})

def getcrds(request,name):
    #name = request.GET['name']
    try:
        d = helpers.get_old(name,10)
        #d2 = helpers.get_data(list(name),10)
        coordinates = { i:d[i] for i in range(len(d)) }
        return JsonResponse(coordinates)
    except:
        return JsonResponse({})

def sentiment(request):
    return render(request,'index.html',{'key':GMAP_API_KEY})

def redirect_home(request):
    return HttpResponseRedirect(reverse('home'))

def redirect_index(request):
    return HttpResponseRedirect(reverse('index'))
