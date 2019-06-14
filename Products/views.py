from django.shortcuts import render, redirect
from .tasks import createProds

def addProducts(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'The uploaded file is not a csv file.')

        dataset = csv_file.read().decode('UTF-8')
        createProds.delay(dataset)
        return redirect('/dashboard')
    return render(request, 'Products/addProducts.html', {})

def dashboard(request):
    return render(request, 'Products/dashboard.html', {})