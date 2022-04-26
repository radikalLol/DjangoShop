# Generated by Django 4.0.3 on 2022-03-16 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='brand',
        ),
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.ManyToManyField(help_text='Select a Brand of the product', to='catalog.brand'),
        ),
    ]