from django.urls import path
from . import views


urlpatterns = [
    # sections
    path('store/<slug:category_slug>/', views.sections, name='section'),

    # certain product url
    path('products/<slug:product_slug>/', views.certain_product, name='certain_product')
]
