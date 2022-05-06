from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    images=Media.objects.all()
    for image in images:
        print(image)
    return render(request,'index.html',{'images':images})