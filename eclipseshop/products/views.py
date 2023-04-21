from django.shortcuts import render


def products(request):
    return render(request, 'products/section-of-products.html')
