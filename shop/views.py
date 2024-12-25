# from models import Product
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product
from math import ceil
# Create your views here.
def index(request):
    products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n // 4) - (n // 4))
    # print(products)
    
    allProds = []
    catProds = Product.objects.values('category','id')
    cats = {item['category'] for item in catProds}
    
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n//4) - (n//4))
        allProds.append([prod,range(1,nSlides),nSlides])
        
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides), 'product':products}

    # allProds = [[products,range(1,nSlides),nSlides],
    #             [products,range(1,nSlides),nSlides]]
    params = {'allProds':allProds}
    return render(request,"shop/index.html",params)


def about(request):
    return render(request,"shop/about.html")

def tracker(request):
    return HttpResponse("This is tracker")

def search(request):
    return HttpResponse("This is search")

def productView(request):
    return HttpResponse("This is productview")

def checkout(request):
    return HttpResponse("This is checkout")

