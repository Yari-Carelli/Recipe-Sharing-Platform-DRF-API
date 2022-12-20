from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    course_choices = [
        ('none', 'None'),
        ('appetizers_&_snacks', 'Appetizers & Snacks'),
        ('breakfast_&_brunch', 'Breakfast & Brunch'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('desserts', 'Desserts'),
        ('main_dishes', 'Main Dishes'),
        ('side_dishes', 'Side Dishes'),
        ('salads', 'Salads'),
        ('condiments', 'Condiemnts'),
        ('soups_&_stews', 'Soups & Stews'),
    ]
    category_choices = [
        ('none', 'None'),
        ('fruits', 'Fruits'),
        ('vegetables', 'Vegetables'),
        ('legumes', 'Legumes'),
        ('grains', 'Grains'),
        ('meats', 'Meats'),
        ('poultry', 'Poultry'),
        ('fish', 'Fish'),
        ('seafood', 'Seafood'),
        ('eggs', 'Eggs'),
        ('mushrooms', 'Mushrooms'),
        ('cheese_&_dairy', 'Cheese & Dairy'),
        ('nuts_&_seeds', 'Nuts & Seeds'),
        ('herbs_&_spices', 'Herbs & Spices'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    ingredients = models.TextField(blank=True)
    directions = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_wdyur2', blank=True
    )
    course = models.CharField(
        max_length=20,
        choices=course_choices,
        default='none'
    )
    category = models.CharField(
        max_length=20,
        choices=category_choices,
        default='none'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
