from django.shortcuts import render
from django.http import JsonResponse
from . import helpers

# Create your views here.
GMAP_API_KEY = 'AIzaSyAQhPH9EijO6ENbBIDsYyuclePHJjeO6K4'

def index(request):
    return render(request,'index.html',{'key':GMAP_API_KEY})

def getcrds(request,name):
    #name = request.GET['name']
    print(name)
    try:
        d = helpers.get_data(list(name),10)
        coordinates = { i:d[i] for i in range(len(d)) }
        return JsonResponse(coordinates)
    except:
        return JsonResponse({})