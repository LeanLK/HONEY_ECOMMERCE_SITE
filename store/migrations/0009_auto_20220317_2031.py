# Generated by Django 2.2.13 on 2022-03-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_auto_20220317_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='total',
            field=models.CharField(max_length=100, null=True),
        ),
    ]