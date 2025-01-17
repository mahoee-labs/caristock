# Generated by Django 5.0 on 2024-05-15 17:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_alter_stock_supply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name': 'Stock', 'verbose_name_plural': 'Stock'},
        ),
        migrations.AlterModelOptions(
            name='supply',
            options={'verbose_name': 'Supply', 'verbose_name_plural': 'Supplies'},
        ),
        migrations.AlterField(
            model_name='stock',
            name='quantity',
            field=models.IntegerField(verbose_name='Quantity'),
        ),
        migrations.AlterField(
            model_name='stock',
            name='supply',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='inventory.supply', verbose_name='Supply'),
        ),
        migrations.AlterField(
            model_name='supply',
            name='name',
            field=models.CharField(help_text='Enter the donated item name', max_length=80, unique=True, verbose_name='Name'),
        ),
    ]
