from django.contrib import admin
from .models import Capitulo, Dominio, Seccion, Wiki
# Register your models here.
admin.site.register(Dominio)
admin.site.register(Seccion)
admin.site.register(Wiki)
admin.site.register(Capitulo)
