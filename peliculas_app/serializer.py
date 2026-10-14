from rest_framework import serializers

from .models import Pais, Region, Provincia, Comuna, Direccion, Genero, Idioma
from .models import Clasificacion, Estado, Productora, Plataforma, Titulo
from .models import Temporada, Episodio, Persona, RolProduccion, Reparto
from .models import Usuario, Critico, Resena, Visualizacion

# Un serializador por cada clase del modelo de datos.
# ModelSerializer construye los campos a partir del modelo, por lo que
# fields = '__all__' expone todos los atributos de la clase.

class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'

class ComunaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comuna
        fields = '__all__'

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'

class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'

class IdiomaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idioma
        fields = '__all__'

class ClasificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clasificacion
        fields = '__all__'

class EstadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = '__all__'

class ProductoraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productora
        fields = '__all__'

class PlataformaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataforma
        fields = '__all__'

class TituloSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titulo
        fields = '__all__'

class TemporadaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temporada
        fields = '__all__'

class EpisodioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Episodio
        fields = '__all__'

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class RolProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolProduccion
        fields = '__all__'

class RepartoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reparto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        # La contraseña se puede escribir (POST/PUT/PATCH) pero nunca
        # se devuelve en las respuestas GET.
        extra_kwargs = {'contrasenia': {'write_only': True}}

class CriticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Critico
        fields = '__all__'

class ResenaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resena
        fields = '__all__'

class VisualizacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visualizacion
        fields = '__all__'
