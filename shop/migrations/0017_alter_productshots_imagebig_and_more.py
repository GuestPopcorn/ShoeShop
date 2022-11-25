# Generated by Django 4.1.3 on 2022-11-25 13:22

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_remove_productshots_imagebig_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productshots',
            name='imageBig',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[540, 600], upload_to='product_shots/'),
        ),
        migrations.AlterField(
            model_name='productshots',
            name='imageSmall',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[150, 160], upload_to='product_shots/'),
        ),
        migrations.AlterField(
            model_name='productshots',
            name='imageZoom',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, null=True, quality=75, scale=0.5, size=[810, 900], upload_to='product_shots/'),
        ),
    ]
