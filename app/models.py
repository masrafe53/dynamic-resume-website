from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=50)
    dis = models.TextField(max_length=500)
    img = models.ImageField(upload_to='ServicesImage')
    category = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.title

class RecentWork(models.Model):
    title = models.CharField(max_length=50)
    dis = models.TextField(max_length=500)
    img = models.ImageField(upload_to='ServicesImage')
    category = models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.title
class Clint(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(upload_to='Clients')
    def __str__(self) -> str:
        return self.title
class MySelf(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    mail = models.EmailField(max_length=50)
    phone = models.IntegerField
    details = models.TextField(max_length=300)
    def __str__(self) -> str:
        return self.title
class Blog(models.Model):
    time = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='blog')
    details = models.TextField(max_length=3000)
    def __str__(self) -> str:
        return self.title