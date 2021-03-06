# Generated by Django 3.0.6 on 2020-05-22 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=100)),
                ('areacode', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('may_contact', models.BooleanField()),
                ('feedback', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Feedback',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=200)),
                ('lastname', models.CharField(max_length=100)),
                ('areacode', models.IntegerField()),
                ('phone_number', models.IntegerField()),
                ('email', models.EmailField(max_length=100)),
                ('profession', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=50)),
            ],
        ),
    ]
