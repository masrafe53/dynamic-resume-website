# Generated by Django 4.1.5 on 2023-01-31 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_delete_blog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='blog')),
                ('details', models.TextField(max_length=3000)),
            ],
        ),
    ]