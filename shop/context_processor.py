from shop.models import Category, Subcategory


def extras(request):
    category = Category.objects.all()
    # category_id = Category.objects.get(id=1)
    # subcategory = category_id.subcats.all()
    return {'category': category}
