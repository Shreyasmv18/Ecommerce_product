from django.contrib import admin
from django.urls import path
from products.views import home, product_list, ProductListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # Homepage
    path('products/', product_list, name='product_list'),  # Product List Page
]
