from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .tasks import createProds
from .models import Products

def addProducts(request):
    exists = False
    if Products.objects.all().exists():
        exists = True
    
    elif request.method == 'POST':
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'The uploaded file is not a csv file.')

        dataset = csv_file.read().decode('UTF-8')
        createProds.delay(dataset)
        return redirect('/dashboard')
    return render(request, 'Products/addProducts.html', {'exists':exists})

def dashboard(request):
    products_list = Products.objects.get_queryset().order_by('productSKU')
    paginator = Paginator(products_list, 15)

    page = request.GET.get('dashboard', 1)
    products = paginator.get_page(page)
    return render(request, 'Products/dashboard.html', {'products': products})

def prodGrid(request):
    products_list = Products.objects.all().order_by('productSKU')

    searchterm = request.GET.get('search')
    searchby = request.GET.get('dropdown')
    if searchby:
        if searchby == "productSKU":
            products_list = products_list.filter(productSKU__icontains=searchterm).order_by('productSKU')
        if searchby == "productDesc":
            products_list = products_list.filter(productDesc__icontains=searchterm).order_by('productSKU')
        if searchby == "productName":
            products_list = products_list.filter(productName__icontains=searchterm).order_by('productSKU')

    paginator = Paginator(products_list, 12)

    page = request.GET.get('products')
    products = paginator.get_page(page)

    return render(request, 'Products/productGrid.html', {'products': products})

def delProducts(request):
    Products.objects.all().delete()
    return redirect('/addProducts')

def productStatus(request,stat):
    if stat == '1':
        products_list = Products.objects.filter(productActive=True).order_by('productSKU')
    elif stat == '0':
        products_list = Products.objects.filter(productActive=False).order_by('productSKU')

    paginator = Paginator(products_list, 12)

    page = request.GET.get('products')
    products = paginator.get_page(page)

    return render(request, 'Products/productGrid.html', {'products': products})