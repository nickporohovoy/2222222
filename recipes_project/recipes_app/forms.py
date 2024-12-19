from django import forms
from .models import Recipe, Ingredient

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'preparation_steps',
                  'preparation_time', 'image', 'author']

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['name']