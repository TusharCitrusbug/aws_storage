from django.urls import path
from apk.views import *

urlpatterns = [
    path('', index,name="index"),

]