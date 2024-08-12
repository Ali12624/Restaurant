from django.db import models

# Create your models here.

class Food(models.Model):
    FOOD_TYPE = [
        ('breakfast', 'Breakfast'),
        ("lunch", "Lunch"),
        ('dinner', 'Dinner'),
        ("drinks", 'Drinks'),
        ('dessert', 'Dessert')
    ]
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    # recipe  = models.TextField()
    photo = models.ImageField(upload_to='foods/')
    # ingredient  = models.JSONField(blank=True, null=True)
    ingredient  = models.CharField(blank=True, null=True, max_length=300)
    food_type = models.CharField(max_length=10, choices=FOOD_TYPE, default='lunch')

    def __str__(self):
        return self.name