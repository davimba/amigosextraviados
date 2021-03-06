from rest_framework import serializers

from .models import Usuario


class UsuarioRegistroSerializer(serializers.ModelSerializer):
    """UsuarioSerializer, Clase para el registro de Usuario"""
    password = serializers.CharField(required=False, allow_blank=True, write_only=True)

    class Meta:
        model = Usuario
        fields = ('id', 'email', 'nombre','is_active', 'password')
        read_only_fields = ('id', 'is_active')
        #write_only_fields = ('password')#pending deprecation
        extra_kwargs = {'password': {'write_only': True}}
        #password = serializers.Field(source='password', required=False)

    def update(self, instance, validated_data):
        make_passwork = False
        #instance.nombre = validated_data.get('nombre', instance.nombre)
        #instance.apellido = validated_data.get('apellido', instance.apellido)
        try:
            if validated_data.get('password', None):
                instance.password = validated_data.get('password', None)
                make_passwork = True
        except KeyError:
            print("No found")

        instance.update(make_passwork=make_passwork)
        return instance


class UsuarioPublicoSerializer(serializers.ModelSerializer):
    """Usuario Publico Serializer, Clase para mostrar la informacion del usuario al publico"""
    full_name = serializers.CharField(source='get_full_name', read_only=True)

    class Meta():
        model = Usuario
        fields = ('id', 'is_active', 'full_name')
        read_only_fields = ('id', 'is_active')


class UsuarioSerializer(serializers.ModelSerializer):
    """Clase para el update"""

    class Meta():
        model = Usuario
        fields = ('id', 'is_active', 'email', 'nombre', 'apellido', 'direccion', 'telefono')
        #read_only_fields = ('id', 'is_active')
