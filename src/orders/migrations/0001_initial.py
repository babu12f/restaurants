# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-30 06:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('foods', '0001_initial'),
        ('accounts', '0001_initial'),
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('products', models.ManyToManyField(blank=True, to='foods.Food')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurants.Restaurant')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('phone', models.CharField(default='', max_length=20)),
                ('shipping_address', models.CharField(default='', max_length=200)),
                ('_type', models.CharField(choices=[('Home', 'Home'), ('Restaurant', 'Restaurant')], default='Home', max_length=100)),
                ('_payment', models.CharField(choices=[('pod', 'Pay On Delivery'), ('bkash', 'bKash'), ('dbbl', 'DBBL')], default='pod', max_length=100)),
                ('expected_date', models.DateField(blank=True, default='', null=True)),
                ('expected_time', models.TimeField(blank=True, default='', null=True)),
                ('discountID', models.CharField(blank=True, max_length=100, null=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=12)),
                ('is_active', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.Account')),
                ('cart', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.Cart')),
            ],
        ),
    ]
