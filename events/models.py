from django.db import models
from django.contrib.auth.models import User


class Event(models.Model):
    """
    Event model for database.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    content = models.TextField(blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    location = models.CharField(max_length=50)
    price = models.IntegerField(null=True, blank=True)
    event_link = models.URLField('Event URL', max_length=400, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} {self.date}'
