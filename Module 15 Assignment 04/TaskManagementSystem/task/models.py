from django.db import models
from category.models import Category
# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    categories = models.ManyToManyField(Category)
    is_complete = models.BooleanField(default=False)
    assign_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title