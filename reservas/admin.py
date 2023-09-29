from django.contrib import admin
from .models import Reserva, Stand
# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display=('cnpj', 'nome', 'categoria_empresa', 'quitado', 'stand')

admin.site.register(Reserva)
admin.site.register(Stand)