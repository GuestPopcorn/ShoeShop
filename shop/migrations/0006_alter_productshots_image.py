# Generated by Django 4.1.3 on 2022-11-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshots',
            name='image',
            field=models.ImageField(upload_to='product_shots/', verbose_name='Изоброжение'),
        ),
    ]