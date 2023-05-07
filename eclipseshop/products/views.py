from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# KEYBOARDS & MICE 4th section of Accessories
def keyboards_mice(request):

    section_name = 'KEYBOARDS & MICE'
    products = Product.objects.filter(available=True)
    context = {'section_name': section_name,
               'products': products,
               }
    return render(request, 'products/section-of-products.html', context)

# view for certain product
def certain_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    context = {'product': product,}
    return render(request, 'products/certain-product.html', context)