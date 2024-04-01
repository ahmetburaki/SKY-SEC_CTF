from django.shortcuts import render,redirect
from app.models import Product
from django.db.models.functions import Extract
from django.http import HttpResponseServerError
# Create your views here.

def cart(r):
    return render(r,'cart.html')

def checkout(r):
    return render(r,'checkout.html')

def contact(r):
    return render(r,'contact.html')

def detail(r):
    return render(r,'detail.html')

def index(r):
    return render(r,'index.html')

def shop(r):
    try:
        order = r.GET.get('order')
        order_by = r.GET.get("order_by")
        if order_by is None:order_by="year"
        if order is None:order='date'
        if order=="date":
            increasing=True
            products = Product.objects.annotate(year_field=Extract("date",order_by))
            lst_ = []
            for i in products:
                lst_.append({"product":i,"order_by_value":i.year_field})
            lst_ =sorted(lst_,key=lambda d:d["order_by_value"],reverse=increasing)
            i=0
            lst__=[]
            while i<len(products):lst__.append(lst_[i]["product"]);i+=1
            products=lst__
        elif order=="popularity":
            products = Product.objects.order_by("popularity")
            if order_by=="descending":
                products=products.reverse()
        else:
            products=Product.objects.order_by("rating")
            if order_by=="descending":
                products=products.reverse()
        return render(r,'shop.html',{
            "products":products
        })
    except Exception as e:
        return render(r,"shop.html",{
            "products":Product.objects.all()
        })
