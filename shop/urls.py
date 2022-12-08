from django.urls import path
from .views import *


urlpatterns = [
    path("", home_page, name='home'),
    path("shop/", shop_view, name='shop'),
    path("cart/", cart, name='cart'),
    path("checkout/", checkout, name='checkout'),
    path('product/<str:pk>', product_detail, name='product_detail'),
    path('update_item/', updateItem, name='update_item'),
    path('process_order/', processOrder, name='process_order'),

]
