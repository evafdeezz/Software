from django.contrib import admin
from . import models

# Personalización de la clase de administración para 'Destination'
class DestinationAdmin(admin.ModelAdmin):
    # Muestra estos campos en la vista de lista
    list_display = ('name', 'description', 'image')  # Muestra nombre, descripción e imagen

    # Habilita la búsqueda por nombre y descripción en el panel de admin
    search_fields = ('name', 'description')

    # Campos que se mostrarán en el formulario de edición
    fields = ('name', 'description', 'image')  # Muestra los campos de nombre, descripción e imagen


# Register your models here.
admin.site.register(models.Cruise)
admin.site.register(models.Destination)
admin.site.register(models.InfoRequest)