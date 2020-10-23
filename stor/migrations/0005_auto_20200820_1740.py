# Generated by Django 2.2 on 2020-08-20 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stor', '0004_customarregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customarregistration',
            name='user',
        ),
        migrations.AddField(
            model_name='customarregistration',
            name='email',
            field=models.EmailField(default='exit', max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customarregistration',
            name='first_name',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customarregistration',
            name='last_name',
            field=models.CharField(default='exit', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customarregistration',
            name='mobile_number',
            field=models.CharField(default='exit', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customarregistration',
            name='password',
            field=models.CharField(default='exit', max_length=500),
            preserve_default=False,
        ),
    ]