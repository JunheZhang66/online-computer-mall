# Generated by Django 2.1.1 on 2018-09-09 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='goods',
        ),
        migrations.RemoveField(
            model_name='orderlineitem',
            name='orders',
        ),
        migrations.DeleteModel(
            name='Goods',
        ),
        migrations.DeleteModel(
            name='OrderLineItem',
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]