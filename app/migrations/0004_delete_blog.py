# Generated by Django 4.1.5 on 2023-01-31 11:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_blog'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]