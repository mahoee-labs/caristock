# Generated by Django 5.0 on 2024-05-14 18:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='When this record was updated')),
                ('name', models.CharField(help_text='Insira o nome do item doado', max_length=80, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='When this record was created')),
                ('updated', models.DateTimeField(auto_now=True, help_text='When this record was updated')),
                ('quantity', models.IntegerField()),
                ('supply', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.supply', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
