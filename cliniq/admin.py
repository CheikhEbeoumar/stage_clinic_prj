from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cliniq.models import *
# Register your models here.

admin.site.register(Gérent)
admin.site.register(Spécialiste)
admin.site.register(Patient)
admin.site.register(Spécialité)
admin.site.register(RDV)
