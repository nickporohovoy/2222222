from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preparation_steps = models.TextField()
    preparation_time = models.IntegerField()  # Время в минутах
    image = models.ImageField(upload_to='recipe_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name