from django.urls import path
from .views import home_page, product_detail, shop_view

urlpatterns = [
    path("", home_page, name='home'),
    path("shop/", shop_view, name='shop'),
    path('<slug:slug>/', product_detail, name='product_detail')
]
