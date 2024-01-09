from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    productss = Product.objects.all()
    return render(request,'index.html',{'products' : productss})

def np(request):
    return HttpResponse('New Products')