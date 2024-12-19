from django.urls import path
from . import views

app_name = 'recipes_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('add-recipe/', views.add_recipe_view, name='add_recipe'),
    path('edit-recipe/<int:pk>/', views.edit_recipe_view, name='edit_recipe'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
]