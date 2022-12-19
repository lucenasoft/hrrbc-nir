from django.contrib import admin

from .models import Transferencias_Adu, Transferencias_Ges, Transferencias_Ped

admin.site.register(Transferencias_Ped)
admin.site.register(Transferencias_Adu)
admin.site.register(Transferencias_Ges)
