# Generated by Django 2.1 on 2019-07-01 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('na_laalii_app', '0009_pro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pro',
            name='bg1',
            field=models.ImageField(blank=True, upload_to='bg1'),
        ),
        migrations.AlterField(
            model_name='pro',
            name='bg2',
            field=models.ImageField(blank=True, upload_to='bg2'),
        ),
        migrations.AlterField(
            model_name='pro',
            name='logo',
            field=models.ImageField(upload_to='logo'),
        ),
    ]