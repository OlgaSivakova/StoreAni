# Generated by Django 4.1.5 on 2023-09-20 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='c_t',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='prod',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='quant',
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='us',
            field=models.TextField(blank=True, null=True),
        ),
    ]
