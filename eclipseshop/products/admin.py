from django.contrib import admin
from .models import Category, Product, TechSpec

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'multiple_types_helper', 'price', 'stock', 'available', 'created', 'updated']
    prepopulated_fields = {'slug': ('name', )}
    list_editable = ['multiple_types_helper', 'price', 'stock', 'available']
admin.site.register(Product, ProductAdmin)


admin.site.register(TechSpec)
