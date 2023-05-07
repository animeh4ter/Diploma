from django.urls import path
from . import views


urlpatterns = [
    # 4th section of Accessories
    path('keyboards-mices/', views.keyboards_mice, name='keyboards_mice'),

    # certain product url
    path('keyboards-mices/<slug:product_slug>', views.certain_product, name='certain_product')
]
