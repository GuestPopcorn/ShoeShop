from django.shortcuts import render

from .models import Product, Color, Category, Brand, Size


def home_page(request):
    products = Product.objects.all()
    context = {'product_list': products,
               }
    return render(request, 'Shop/need/index.html', context=context)


def shop_view(request):
    products = Product.objects.all()
    category = Category.objects.all()
    brands = Brand.objects.all()
    size = Size.objects.all()
    color = Color.objects.all()
    context = {'product_list': products,
               'category': category,
               'brand': brands,
               'size': size,
               'color': color,
               }
    return render(request, 'Shop/need/shop-left-sidebar.html', context=context)


def product_detail(request, slug):
    product = Product.objects.get(url=slug)

    return render(request, 'Shop/need/shop-product-detail.html', {'product': product})
