from django.shortcuts import render, get_object_or_404, redirect
from django.http.response import HttpResponse, Http404
from .models import Product
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.conf import settings
from django.contrib import messages
from comments.forms import CommentForm
from comments.models import Comment
from .forms import ProductForm
from comments.views import get_comments_quantity
from django.urls.base import reverse

# Create your views here.
def index(request):
    try:
        page = (request.GET.get('p',1))
        products = Paginator(
            Product.objects.order_by('name').all(),
            settings.ITEMS_ON_PAGE
        ).page(
            page
        )
    except (EmptyPage, PageNotAnInteger):
        raise Http404
    return render(request,
                  'index.html',
                  {
                      'products': products,
                      'comments_count': get_comments_quantity(request)
                  })

def details(request, slug):
    product = get_object_or_404(Product, slug = slug)
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data['author'],
                body = form.cleaned_data['body'],
                product=product
            )
            comment.save()
            return redirect(product.get_absolute_url())
    return render(
        request,
        'details.html',
        {'product': product,
         'form': form, # на страницу деталей передали форму камментов
         }
    )

def edit(request, slug):
    product = get_object_or_404(Product, slug = slug)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.INFO, 'Product has been updated'
            )
    return render(request, 'edit.html', {'form': form})