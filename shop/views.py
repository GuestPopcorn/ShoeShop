from django.shortcuts import render

from .models import Product, ProductColor, Color, Category, Brand, ProductSize


def home_page(request):
    products = Product.objects.all()
    color = ProductColor.objects.all()
    return render(request, 'Shop/need/index.html', {'product_list': products, 'product_color': color})


def shop_view(request):
    products = Product.objects.all()
    color = ProductColor.objects.all()
    category = Category.objects.all()
    brands = Brand.objects.all()
    sizes = ProductSize.objects.all()
    context = {'product_list': products,
               'product_color': color,
               'size': sizes,
               'category': category,
               'brand': brands}
    return render(request, 'Shop/none/shop-left-sidebar.html',)


def product_detail(request, slug):
    product = Product.objects.get(url=slug)
    return render(request, 'Shop/need/shop-product-detail.html', {'product': product})
