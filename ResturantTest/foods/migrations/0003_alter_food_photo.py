# Generated by Django 5.0.3 on 2024-07-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_food_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='photo',
            field=models.ImageField(upload_to='foods/'),
        ),
    ]
