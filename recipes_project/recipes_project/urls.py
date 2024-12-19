from django.urls import path, include  # Добавлен include
from django.contrib import admin

urlpatterns = [
    path('', include('recipes_app.urls')),  # Новый маршрут
    path('admin/', admin.site.urls),
]