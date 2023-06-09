from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from .utils import paginate_products
from datetime import datetime, timedelta, date
from django.http import Http404
from cart.forms import CartAddProductForm


# view for sections
def sections(request, category_slug):
    reworked_name = f'{category_slug.replace("-", " ").upper()}'
    category = Category.objects.filter(slug=category_slug)
    cart_product_form = CartAddProductForm()
    if category:
        products = Product.objects.filter(category__slug=category_slug, available=True)
        custom_range, products = paginate_products(request, products, 6)
        context = {'section_name': reworked_name,
                    'products': products,
                    'cart_product_form': cart_product_form,
                    'custom_range': custom_range,
               }
        return render(request, 'products/section-of-products.html', context)
    else:
        raise Http404()

# view for certain product
def certain_product(request, product_slug):
    product = get_object_or_404(Product, slug=product_slug)
    delivery_time = date.today() + timedelta(hours=72)
    cart_product_form = CartAddProductForm()
    context = {'product': product,
               'delivery_time': delivery_time,
               'cart_product_form': cart_product_form,
               }
    return render(request, 'products/certain-product.html', context)
