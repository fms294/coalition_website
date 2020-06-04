# Generated by Django 3.0.6 on 2020-06-02 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_category_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
        migrations.RemoveField(
            model_name='post',
            name='categories',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
