# Generated by Django 4.1.3 on 2022-11-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_remove_brand_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmaterial',
            name='material',
        ),
        migrations.RemoveField(
            model_name='productmaterial',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='product',
        ),
        migrations.RemoveField(
            model_name='productsize',
            name='size',
        ),
        migrations.AddField(
            model_name='product',
            name='color',
            field=models.ManyToManyField(null=True, to='shop.color'),
        ),
        migrations.AddField(
            model_name='product',
            name='material',
            field=models.ManyToManyField(null=True, to='shop.material'),
        ),
        migrations.AddField(
            model_name='product',
            name='size',
            field=models.ManyToManyField(null=True, to='shop.size'),
        ),
        migrations.DeleteModel(
            name='ProductColor',
        ),
        migrations.DeleteModel(
            name='ProductMaterial',
        ),
        migrations.DeleteModel(
            name='ProductSize',
        ),
    ]
