# Generated by Django 2.2 on 2020-09-08 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stor', '0010_auto_20200908_1601'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerorders',
            name='quantity',
        ),
    ]
