from django.views.generic import ListView
from django.shortcuts import render
from .models import Product  

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'
    context_object_name = 'products'

def home(request):
    return render(request, 'index.html')

def product_list(request):
    products = Product.objects.all() 
    return render(request, 'product_list.html', {'products': products})
