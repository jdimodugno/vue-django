# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-10 19:57
from __future__ import unicode_literals

import backend.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, null=True)),
                ('description', models.TextField(max_length=1000)),
                ('abv', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', backend.models.IntegerRangeField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('beer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Beer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='city',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Country'),
        ),
        migrations.AddField(
            model_name='brand',
            name='city',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.City'),
        ),
        migrations.AddField(
            model_name='beer',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Brand'),
        ),
    ]
