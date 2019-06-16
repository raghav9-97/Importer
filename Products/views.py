from django.shortcuts import render, redirect
from django.core.paginator import Paginator
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
    if request.method == 'POST':
        drop = request.POST['dropdown']
        searchterm = request.POST['search']
        if drop == 'productSKU':
            products_list = Products.objects.filter(productSKU__icontains=searchterm).order_by('productSKU')
        elif drop == 'productName':
            products_list = Products.objects.filter(productName__icontains=searchterm).order_by('productSKU')
        else:
            products_list = Products.objects.filter(productDesc__icontains=searchterm).order_by('productSKU')    
    else:
        products_list = Products.objects.get_queryset().order_by('productSKU')

    paginator = Paginator(products_list, 12)

    page = request.GET.get('products', 1)
    products = paginator.get_page(page)

    return render(request, 'Products/productGrid.html', {'products': products})