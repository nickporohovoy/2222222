from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from .models import Recipe
from .forms import RecipeForm, IngredientForm

def index(request):
    latest_recipes = Recipe.objects.order_by('-id')[:5]
    context = {'latest_recipes': latest_recipes}
    return render(request, 'recipes_app/index.html', context)

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipes_app/recipe_detail.html'
    context_object_name = 'recipe'

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'recipes_app/registration.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes_app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return render(request, 'recipes_app/logout.html')

def add_recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', pk=recipe.pk)
    else:
        form = RecipeForm()
    return render(request, 'recipes_app/add_recipe.html', {'form': form})

def edit_recipe_view(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe_detail', pk=pk)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes_app/edit_recipe.html', {'form': form})