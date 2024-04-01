from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('index',views.index,),
    path('cart',views.cart,name='cart'),
    path('contact',views.contact,name='contact'),
    path('detail',views.detail,name='detail'),
    path('shop',views.shop,name='shop'),
    path('chekcout',views.checkout,name='checkout')
]