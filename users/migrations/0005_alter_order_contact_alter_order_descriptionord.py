# Generated by Django 4.1.5 on 2023-09-22 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_order_descriptionord'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='contact',
            field=models.CharField(max_length=13),
        ),
        migrations.AlterField(
            model_name='order',
            name='descriptionord',
            field=models.TextField(),
        ),
    ]
