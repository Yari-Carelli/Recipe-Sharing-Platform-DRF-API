from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('none', 'None'),
        ('appetizer', 'Appetizer'),
        ('breakfast_&_brunch', 'Breakfast & Brunch'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('dessert', 'Dessert'),
        ('main_dish', 'Main Dish'),
        ('side_dish', 'Side Dish'),
        ('salad', 'Salad'),
        ('condiment', 'Condiemnt'),
        ('soup_&_stew', 'Soup & Stew'),
        ('fruit', 'Fruit'),
        ('vegetable', 'Vegetable'),
        ('legume', 'Legume'),
        ('grain', 'Grain'),
        ('meat', 'Meat'),
        ('poultry', 'Poultry'),
        ('fish', 'Fish'),
        ('seafood', 'Seafood'),
        ('egg', 'Egg'),
        ('mushroom', 'Mushroom'),
        ('cheese_&_dairy', 'Cheese & Dairy'),
        ('nuts_&_seeds', 'Nuts & Seeds'),
        ('herbs_&_spices', 'Herbs & Spices'),
    ]
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_wdyur2', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
