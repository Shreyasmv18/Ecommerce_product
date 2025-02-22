from django.contrib import admin
from .models import Product, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'description')


admin.site.site_header = "E-Commerce Admin Panel"
admin.site.site_title = "E-Commerce Admin"
admin.site.index_title = "Manage Products & Categories"
