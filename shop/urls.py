from django.urls import path
from .views import home_page, product_detail, shop_view, updateItem, cart, checkout

urlpatterns = [
    path("", home_page, name='home'),
    path("shop/", shop_view, name='shop'),
    path("cart/", cart, name='cart'),
    path("checkout/", checkout, name='checkout'),
    path('product/<str:pk>', product_detail, name='product_detail'),
    path('update_item/', updateItem, name='update_item')
]
