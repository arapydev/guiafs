from django.contrib import admin
from .models import Category, Professional

# Registramos los modelos para que aparezcan en el panel de admin
admin.site.register(Category)
admin.site.register(Professional)