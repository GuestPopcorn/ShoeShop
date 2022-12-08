from shop.models import Category, Subcategory, Order


def extras(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    category = Category.objects.all()
    # category_id = Category.objects.get(id=1)
    # subcategory = category_id.subcats.all()
    return {'category': category, 'cartItems': cartItems, 'items': items, 'order': order,}
