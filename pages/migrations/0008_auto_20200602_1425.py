# Generated by Django 3.0.6 on 2020-06-02 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_auto_20200525_1208'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='lastname',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='feedback',
            old_name='firstname',
            new_name='prenom',
        ),
    ]
