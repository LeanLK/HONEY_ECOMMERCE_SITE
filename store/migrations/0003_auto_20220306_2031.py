# Generated by Django 2.2.13 on 2022-03-06 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='digital',
        ),
        migrations.AddField(
            model_name='product',
            name='descriere',
            field=models.CharField(max_length=500, null=True),
        ),
    ]