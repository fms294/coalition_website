# Generated by Django 3.0.6 on 2020-05-24 17:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_auto_20200524_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
