from rest_framework import serializers
from .models import CustomUser, Cuenta, Transaccion

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'apellido', 'numero_identificacion']
        read_only_fields = ['id']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'first_name', 'last_name', 'apellido', 'numero_identificacion']
    
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
            password=validated_data['password'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            apellido=validated_data['apellido'],
            numero_identificacion=validated_data['numero_identificacion']
        )
        return user

class CuentaSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    
    class Meta:
        model = Cuenta
        fields = ['id_cuenta', 'tipo_cuenta', 'valor_inicial', 'usuario', 'usuario_username']
        read_only_fields = ['id_cuenta']

class TransaccionSerializer(serializers.ModelSerializer):
    cuenta_tipo = serializers.CharField(source='cuenta.tipo_cuenta', read_only=True)
    
    class Meta:
        model = Transaccion
        fields = ['id_transaccion', 'tipo_transaccion', 'monto', 'cuenta', 'cuenta_tipo']
        read_only_fields = ['id_transaccion']