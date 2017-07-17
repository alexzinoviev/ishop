from django.shortcuts import render, get_object_or_404
from django.http.response import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def details(request, productid):
    return render(
        request,
        'details.html',
        {'product': get_object_or_404(Product, pk=int(productid))})