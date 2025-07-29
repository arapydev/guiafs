from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name="Nombre")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")

    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name

class Professional(models.Model):
    # --- Información Básica ---
    full_name = models.CharField(max_length=255, verbose_name="Nombre Completo")
    specialty = models.CharField(max_length=255, verbose_name="Especialidad Principal")
    bio = models.TextField(verbose_name="Biografía o Descripción")
    
    # --- Información de Contacto y Ubicación ---
    phone_number = models.CharField(max_length=20, blank=True, verbose_name="Número de Teléfono")
    email = models.EmailField(unique=True, verbose_name="Correo Electrónico")
    address = models.CharField(max_length=255, verbose_name="Dirección")
    
    # --- Relaciones ---
    categories = models.ManyToManyField(Category, verbose_name="Categorías")

    class Meta:
        verbose_name = "Profesional"
        verbose_name_plural = "Profesionales"

    def __str__(self):
        return f"{self.full_name} - {self.specialty}"