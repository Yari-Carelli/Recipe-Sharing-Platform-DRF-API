from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    """
    Book model for database.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(blank=True)
    number_of_pages = models.IntegerField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    book_link = models.URLField('Book URL', max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_wdyur2', blank=True
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
