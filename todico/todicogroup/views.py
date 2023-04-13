from django.shortcuts import render
from .models import Product, Category
# Create your views here.



def index(request):
    product_object = Product.objects.all()
    return render(request, 'shop/index.html',{'product_object': product_object} )  


def detail(request, myid):
    product_object =Product.objects.get(id = myid)
    return render(request, 'detail.html', {'product_object': product_object})


def product(request, jyid):
    product_object =Product.objects.filter(id = jyid)
    return render(request, 'detail.html', {'product_object': product_object})


def card(request, fyid):
    card_object =Product.objects.filter(id = fyid)
    return render(request, 'card.html', {'card_object': card_object})




