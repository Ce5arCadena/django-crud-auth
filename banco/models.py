from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    apellido = models.CharField(max_length=100)
    numero_identificacion = models.CharField(max_length=50, unique=True)
    
    def __str__(self):
        return f"{self.username} - {self.apellido}"

class Cuenta(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('AHORROS', 'Ahorros'),
        ('CORRIENTE', 'Corriente'),
        ('CDT', 'CDT')
    ]
    id_cuenta = models.AutoField(primary_key=True)
    tipo_cuenta = models.CharField(max_length=10, choices=TIPO_CUENTA_CHOICES)
    valor_inicial = models.DecimalField(max_digits=10, decimal_places=2)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_cuenta} - {self.usuario.username} - {self.valor_inicial}'

class Transaccion(models.Model):
    TIPO_TRANSACCION_CHOICES = [
        ('CONSIGNACION', 'Consignación'),.
        ('RETIRO', 'Retiro'),
    ]
    id_transaccion = models.AutoField(primary_key=True)
    tipo_transaccion = models.CharField(max_length=12, choices=TIPO_TRANSACCION_CHOICES)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    cuenta = models.ForeignKey(Cuenta, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.tipo_transaccion} - {self.monto}'

    def save(self, *args, **kwargs):
        if self.tipo_transaccion == 'CONSIGNACION':
            self.cuenta.valor_inicial += self.monto
        elif self.tipo_transaccion == 'RETIRO':
            if self.cuenta.valor_inicial >= self.monto:
                self.cuenta.valor_inicial -= self.monto
            else:
                raise ValueError("Fondos insuficientes en la cuenta")
        self.cuenta.save()
        super().save(*args, **kwargs)