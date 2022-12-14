from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Book model for database.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=255, null=True)
    description = models.TextField(blank=True)
    number_of_pages = models.IntegerField(null=True)
    published_date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
