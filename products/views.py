from django.shortcuts import render
from django.http import HttpResponse
from .models import Destination

# Create your views here.

def index(request):
    
    dest1 = Destination()
    dest1.productname="New World"
    dest1.price =7000
    dest1.img ='product-1.jpg'
    
    
    
    return render(request,"index.html",{'dest1':dest1})