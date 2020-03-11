# Generated by Django 2.1 on 2018-10-05 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('na_laalii_app', '0004_mtrlinfo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='dealer',
            name='email',
            field=models.EmailField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='dealer',
            name='password',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]