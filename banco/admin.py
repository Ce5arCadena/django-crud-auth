from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Cuenta, Transaccion, CustomUser

# Register your models here.
admin.site.register(Cuenta)
admin.site.register(Transaccion)

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'apellido', 'numero_identificacion', 'is_staff']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Información Adicional', {'fields': ('apellido', 'numero_identificacion')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Información Adicional', {'fields': ('apellido', 'numero_identificacion')}),
    )