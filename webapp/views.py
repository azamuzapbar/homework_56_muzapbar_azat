from django.shortcuts import render, get_object_or_404
from .models import Product

def product_list(request):
    products = Product.objects.filter(remainder__gt=0).order_by('category', 'title')
    context = {
        'products': products
    }
    return render(request, 'main.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {
        'product': product
    }
    return render(request, 'product_detail.html', context=context)