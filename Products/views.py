from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .tasks import createProds
from .models import Products

def addProducts(request):
    exists = False
    if Products.objects.all().exists():
        exists = True
    
    elif request.method == 'POST':
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'The file is not a csv file.')
            return redirect('/addProducts')

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

def prodGrid(request,stat):
    products_list = Products.objects.all().order_by('productSKU')

    searchterm = request.GET.get('search')
    searchby = request.GET.get('dropdown')
    if searchby:
        if searchby == "productSKU":
            products_list = products_list.filter(productSKU__icontains=searchterm)
        if searchby == "productDesc":
            products_list = products_list.filter(productDesc__icontains=searchterm)
        if searchby == "productName":
            products_list = products_list.filter(productName__icontains=searchterm)
    
    if stat == 'Active':
        products_list = products_list.filter(productActive=True)
    elif stat == 'Inactive':
        products_list = products_list.filter(productActive=False)
    
    paginator = Paginator(products_list, 12)

    page = request.GET.get('products')
    products = paginator.get_page(page)

    return render(request, 'Products/productGrid.html', {'products': products})

def delProducts(request):
    Products.objects.all().delete()
    return redirect('/addProducts')

def deleteProd(request,identifier):
    Products.objects.filter(productSKU=identifier).delete()
    return redirect('/dashboard')