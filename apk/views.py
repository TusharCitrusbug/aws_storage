from django.shortcuts import render
from .models import *
# Create your views here.
def index(request):
    l1=[]
    images=Media.objects.all()
    for image in images:
        print(image.picture)
        l1.append(image.picture)
    return render(request,'index.html',{'images':l1})