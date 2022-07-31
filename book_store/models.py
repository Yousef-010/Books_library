from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.FileField(upload_to='Book_images', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_list')
