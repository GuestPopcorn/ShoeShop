from django.urls import reverse

from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser


# Create your models here.
class Category(models.Model):
    name = models.CharField("Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Subcategory(models.Model):
    name = models.CharField("Sub-Категория", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sub-Категория"
        verbose_name_plural = "Sub-Категории"


class Brand(models.Model):
    name = models.CharField("Бренд", max_length=150)
    url = models.SlugField(max_length=160, unique=True)
    description = models.TextField("Описание")

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "Бренды"

    def __str__(self):
        return self.name


class Size(models.Model):
    size = models.IntegerField()

    def __str__(self):
        return str(self.size)


class Color(models.Model):
    title = models.CharField("Название", max_length=150, null=True)
    code = models.CharField("Коде", max_length=50)

    def __str__(self):
        return self.title


class Material(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.material


class Product(models.Model):
    url = models.SlugField(max_length=160, unique=True, null=True)
    name = models.CharField("Название", max_length=150)
    poster = models.ImageField("Постер", upload_to="product/", null=True)
    price = models.PositiveSmallIntegerField("Цена", default=0, )
    stock = models.PositiveSmallIntegerField("Акция", default=0, )
    description = models.TextField("Описание")
    model = models.CharField("Модель обуви", max_length=150)
    color = models.ManyToManyField(Color,  null=True)
    size = models.ManyToManyField(Size, null=True)
    material = models.ManyToManyField(Material, null=True)
    capacity = models.IntegerField("Вес", null=True)
    brand = models.ForeignKey(
        Brand, verbose_name="Бренд", on_delete=models.CASCADE, null=True
    )
    subcategory = models.ForeignKey(
        Subcategory, verbose_name="Subcategory", on_delete=models.CASCADE, null=True
    )
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, null=True
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    image = models.ImageField("Изоброжение", upload_to="product_shots/")
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотогравии"


class Review(models.Model):
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True
    )
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.product}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Order(models.Model):
    url = models.SlugField(max_length=160, unique=True)
    number = models.IntegerField("Номер заказа", unique=True)
    datetime = models.DateTimeField(auto_now_add=True)
    total = models.PositiveSmallIntegerField("Общая цена", default=0)
    customer_id = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.number


class Order_detail(models.Model):
    url = models.SlugField(max_length=160, unique=True)
    product_url = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)
    product_pr = models.ForeignKey(Product, verbose_name="Цена продукта", related_name='order_detail_pr',
                                   on_delete=models.CASCADE)
    order = models.ForeignKey(Order, verbose_name="Продукт", on_delete=models.CASCADE)
    subtotal = models.PositiveSmallIntegerField("Промежуточный итог", default=0)

    def __str__(self):
        return self.order


class Cart(models.Model):
    user = models.ForeignKey(CustomUser, verbose_name="Ползователь", on_delete=models.CASCADE)
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


class Cart_Detail(models.Model):
    cart = models.ForeignKey("Cart", verbose_name="Корзина", on_delete=models.CASCADE)
    product = models.ForeignKey("Product", verbose_name="Продукт", on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
