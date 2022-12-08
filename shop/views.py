from django.db.models import Q
from django.views.generic import ListView
import datetime
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Product, Color, Category, Brand, Size, Subcategory, Order, OrderItem, ShippingAddress
import json
from users.models import CustomUser


def home_page(request):

    products = Product.objects.all()
    context = {
        'product_list': products,

    }
    return render(request, 'Shop/need/index.html', context=context)


def shop_view(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}
        cartItems = order['get_cart_items']

    products = Product.objects.all()
    brands = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()

    category = request.GET.get('category', 0)
    brand = request.GET.get('brand', 0)
    if category != 0 and brand != 0:
        products = Product.objects.filter(category__name=category, brand__name=brand)
    elif category != 0:
        products = Product.objects.filter(category__name=category)
    elif brand != 0:
        products = Product.objects.filter(brand__name=brand)
    context = {'product_list': products,
               'brand': brands,
               'size': size,
               'color': color,
               'cartItems': cartItems,
               }
    return render(request, 'Shop/need/shop-left-sidebar.html', context=context)


def product_detail(request, pk):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0, }
        cartItems = order['get_cart_items']

    product = Product.objects.get(id=pk)
    context = {
        'product': product,

        'cartItems': cartItems,
    }
    return render(request, 'Shop/need/shop-product-detail.html', context)





def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']

    print('Action:', action)
    print('productId:', productId)

    customer = request.user
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)


def cart(request):
    return render(request, 'Shop/need/shop-cart.html',)


def checkout(request):
    return render(request, 'Shop/need/checkout.html',)


def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                address=data['shipping']['address'],
                city=data['shipping']['city'],
                state=data['shipping']['state'],
                zipcode=data['shipping']['zipcode'],

            )

    else:
        print('User is not logged..')

    return JsonResponse('Payment complete!', safe=False)



