from django.urls import reverse

from PIL import Image as Img
import io
from django.core.files.uploadhandler import InMemoryUploadedFile

from django.contrib.auth.models import User
from django.db import models

from users.models import CustomUser
from django_resized import ResizedImageField


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
    slogan = models.CharField('Слоган', max_length=200, null=True)
    poster = models.ImageField("Постер", upload_to="product/", null=True)
    price = models.PositiveSmallIntegerField("Цена", default=0, )
    stock = models.PositiveSmallIntegerField("Акция", default=0, )
    description = models.TextField("Описание")
    model = models.CharField("Модель обуви", max_length=150)
    color = models.ManyToManyField(Color, null=True)
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

    def save(self, **kwargs):
        if self.poster:
            img = Img.open(io.BytesIO(self.poster.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((540, 600), Img.ANTIALIAS)  # (width,height)
            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg"
                                              % self.poster.name.split('.')[0], 'image/jpeg',
                                              "Content-Type: charset=utf-8", None)
            super(Product, self).save()

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class ProductShots(models.Model):
    title = models.CharField("Заголовок", max_length=100)
    # imageSmall = ResizedImageField(size=[150, 160],  upload_to="product_shots/", null=True)
    # imageBig = ResizedImageField(size=[540, 600], upload_to="product_shots/", null=True)
    # imageZoom = ResizedImageField(size=[810,900], upload_to="product_shots/", null=True)
    imageSmall = models.ImageField("Фото 150X160", upload_to="product_shots/", null=True)
    imageBig = models.ImageField("Фото 540X600", upload_to="product_shots/", null=True)
    imageZoom = models.ImageField("Фото 810X900", upload_to="product_shots/", null=True)
    product = models.ForeignKey(Product, verbose_name="Продукт", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, **kwargs):
        if self.imageSmall:
            img = Img.open(io.BytesIO(self.imageSmall.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((150, 160), Img.ANTIALIAS)  # (width,height)
            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg"
                                              % self.imageSmall.name.split('.')[0], 'image/jpeg',
                                              "Content-Type: charset=utf-8", None)
            super(ProductShots, self).save()

        if self.imageBig:
            img = Img.open(io.BytesIO(self.imageBig.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((540, 600), Img.ANTIALIAS)  # (width,height)
            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg"
                                              % self.imageBig.name.split('.')[0], 'image/jpeg',
                                              "Content-Type: charset=utf-8", None)
            super(ProductShots, self).save()

        if self.imageZoom:
            img = Img.open(io.BytesIO(self.imageZoom.read()))
            if img.mode != 'RGB':
                img = img.convert('RGB')
            img.thumbnail((810, 900), Img.ANTIALIAS)  # (width,height)
            output = io.BytesIO()
            img.save(output, format='JPEG')
            output.seek(0)
            self.image = InMemoryUploadedFile(output, 'ImageField', "%s.jpg"
                                              % self.imageZoom.name.split('.')[0], 'image/jpeg',
                                              "Content-Type: charset=utf-8", None)
            super(ProductShots, self).save()

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
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total