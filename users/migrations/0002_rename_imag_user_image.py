# Generated by Django 4.1.5 on 2023-09-19 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='imag',
            new_name='image',
        ),
    ]