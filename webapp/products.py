from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from webapp.models import Product
from webapp.form import ProductForm

def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'create_view.html', context={'form': form})
    elif request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.image = form.cleaned_data['image']
            product.save()
            return redirect(reverse('main'))
        else:
            return render(request, 'create_view.html', context={'form': form})


def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'GET':
        form = ProductForm(initial={
            'title': product.title,
            'image': product.image,
            'text': product.text,
            'category': product.category,
            'remainder': product.remainder,
            'cost': product.cost
        })
        return render(request, 'update_view.html', context={'form': form, 'product': product})
    elif request.method == 'POST':
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = form.cleaned_data['title']
            product.image = form.cleaned_data['image']
            product.text = form.cleaned_data['text']
            product.category = form.cleaned_data['category']
            product.remainder = form.cleaned_data['remainder']
            product.cost = form.cleaned_data['cost']
            product.save()
            return redirect(reverse('main'))
        else:
            return render(request, 'update_view.html', context={'form': form, 'product': product})


def delete_product(requst, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(requst, 'confirm.html', context={'product': product})


def confirm(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('main')
