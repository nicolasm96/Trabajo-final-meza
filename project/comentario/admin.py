from django.contrib import admin
from .models import Comentario

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('texto', 'fecha_creacion')
    list_filter = ('fecha_creacion',)
    search_fields = ('texto',)

# Register your models here.
