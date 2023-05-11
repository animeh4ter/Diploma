from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from datetime import datetime, timedelta, date

# KEYBOARDS & MICE 4th section of Accessories
def keyboards_mice(request, category_slug):
    reworked_name = f'{category_slug.replace("-", " ").upper()}'
    products = Product.objects.filter(category__slug=category_slug, available=True)
    context = {'section_name': reworked_name,
               'products': products,
               }
    return render(request, 'products/section-of-products.html', context)

# view for certain product
def certain_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    delivery_time = date.today() + timedelta(hours=72)
    context = {'product': product,
                'delivery_time': delivery_time,
               }
    return render(request, 'products/certain-product.html', context)