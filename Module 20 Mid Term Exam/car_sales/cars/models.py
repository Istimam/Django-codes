from django.db import models
from django.contrib.auth.models import User
from brands.models import CarBrand
# Create your models here.
class Car(models.Model):    
    name = models.CharField(max_length=100)
    brand = models.ForeignKey('brands.CarBrand', on_delete=models.CASCADE)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=None)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    quantity = models.PositiveIntegerField(default=0)
    author = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    buyers  = models.ManyToManyField(User, related_name='bought_cars', blank=True)
    def __str__(self):
        return self.name
    

class Comments(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    comment = models.TextField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
    def __str__(self):
        return self.name
