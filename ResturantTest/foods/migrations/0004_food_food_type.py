# Generated by Django 5.0.3 on 2024-07-31 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0003_alter_food_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='food_type',
            field=models.CharField(choices=[('B', 'Breakfast'), ('L', 'Lunch'), ('Di', 'Dinner'), ('Dr', 'Drinks'), ('De', 'Dessert')], default='L', max_length=10),
        ),
    ]
