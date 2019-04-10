from django.shortcuts import render

# Create your views here.
API_KEY = 'AIzaSyAQhPH9EijO6ENbBIDsYyuclePHJjeO6K4'

def index(request):
    return render(request,'index.html',{'key':API_KEY})
