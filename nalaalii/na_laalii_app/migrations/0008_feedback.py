# Generated by Django 2.1 on 2018-11-04 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('na_laalii_app', '0007_dealer_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('body', models.CharField(max_length=1000)),
            ],
        ),
    ]