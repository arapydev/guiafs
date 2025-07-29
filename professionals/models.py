from django.db import models
from django.conf import settings

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
    
class TimeSlot(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='timeslots', verbose_name="Profesional")
    day_of_week = models.IntegerField(choices=[(i, i) for i in range(7)], verbose_name="Día de la semana") # 0=Lunes, 6=Domingo
    start_time = models.TimeField(verbose_name="Hora de inicio")
    end_time = models.TimeField(verbose_name="Hora de fin")
    is_available = models.BooleanField(default=True, verbose_name="Disponible")

    class Meta:
        verbose_name = "Franja Horaria"
        verbose_name_plural = "Franjas Horarias"
        # Evita que un profesional cree la misma franja horaria dos veces
        unique_together = ('professional', 'day_of_week', 'start_time')

    def __str__(self):
        return f"{self.professional.full_name} - Día {self.day_of_week}: {self.start_time.strftime('%H:%M')}"

class Appointment(models.Model):
    class AppointmentStatus(models.TextChoices):
        PENDING = 'PENDING', 'Pendiente'
        CONFIRMED = 'CONFIRMED', 'Confirmado'
        CANCELLED = 'CANCELLED', 'Cancelado'
        COMPLETED = 'COMPLETED', 'Completado'

    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='appointments_as_professional', verbose_name="Profesional")
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='appointments_as_client', verbose_name="Cliente")
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Franja Horaria")
    appointment_date = models.DateField(verbose_name="Fecha del turno")
    status = models.CharField(
        max_length=10,
        choices=AppointmentStatus.choices,
        default=AppointmentStatus.PENDING,
        verbose_name="Estado"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        verbose_name = "Turno"
        verbose_name_plural = "Turnos"
        ordering = ['appointment_date', 'timeslot__start_time']

    def __str__(self):
        return f"Turno de {self.client.username} con {self.professional.full_name} el {self.appointment_date}"    