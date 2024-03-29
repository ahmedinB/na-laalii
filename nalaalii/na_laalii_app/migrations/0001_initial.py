# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-08-06 15:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEALER',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('phonenumber', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='mtrlinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mapp_address', models.ImageField(upload_to='mapp_address')),
                ('cost', models.IntegerField()),
                ('frontal_picture', models.ImageField(upload_to='frontal_picture')),
                ('word_address', models.CharField(max_length=150)),
                ('no_of_rooms', models.IntegerField()),
                ('photo_from_inside', models.ImageField(upload_to='photo_from_inside')),
                ('rooms_in_birdeye', models.ImageField(upload_to='rooms_in_birdeye')),
                ('dealer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='na_laalii_app.DEALER')),
            ],
        ),
    ]
