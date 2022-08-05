from django.shortcuts import get_object_or_404, render
from . models import Product

# Create your views here.

def store(request, category_slug=None):
    categories = None
    products = None
    
    if category_slug != None:
        catgories = get_object_or_404(Category, category_slug=slug)
    products = Product.objects.all().filter(is_available=True)
    product_count = products.count()

    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)