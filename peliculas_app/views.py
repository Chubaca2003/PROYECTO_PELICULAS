from django.conf import settings
from django.shortcuts import render
from rest_framework import viewsets

from .models import Pais, Genero, Idioma, Clasificacion, Estado, Productora
from .models import Plataforma, Titulo, Temporada, Episodio, Persona
from .models import RolProduccion, Reparto, Usuario, Critico, Resena
from .models import Visualizacion

from .serializer import PaisSerializer, GeneroSerializer, IdiomaSerializer
from .serializer import ClasificacionSerializer, EstadoSerializer
from .serializer import ProductoraSerializer, PlataformaSerializer
from .serializer import TituloSerializer, TemporadaSerializer
from .serializer import EpisodioSerializer, PersonaSerializer
from .serializer import RolProduccionSerializer, RepartoSerializer
from .serializer import UsuarioSerializer, CriticoSerializer, ResenaSerializer
from .serializer import VisualizacionSerializer


# inicio es una vista basada en función (FBV) que entrega la portada.
def inicio(request):
    if not settings.SISTEMA_ABIERTO:
        return render(request, 'no_dispo.html', status=503)
    return render(request, 'index.html')


# Vistas basadas en clase (CBV).
# ModelViewSet entrega el CRUD completo para cada clase del modelo:
# GET (list/retrieve), POST (create), PUT (update),
# PATCH (partial_update) y DELETE (destroy).

class PaisViewSet(viewsets.ModelViewSet):
    queryset = Pais.objects.all()
    serializer_class = PaisSerializer

class GeneroViewSet(viewsets.ModelViewSet):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer

class IdiomaViewSet(viewsets.ModelViewSet):
    queryset = Idioma.objects.all()
    serializer_class = IdiomaSerializer

class ClasificacionViewSet(viewsets.ModelViewSet):
    queryset = Clasificacion.objects.all()
    serializer_class = ClasificacionSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class ProductoraViewSet(viewsets.ModelViewSet):
    queryset = Productora.objects.all()
    serializer_class = ProductoraSerializer

class PlataformaViewSet(viewsets.ModelViewSet):
    queryset = Plataforma.objects.all()
    serializer_class = PlataformaSerializer

class TituloViewSet(viewsets.ModelViewSet):
    queryset = Titulo.objects.all()
    serializer_class = TituloSerializer

class TemporadaViewSet(viewsets.ModelViewSet):
    queryset = Temporada.objects.all()
    serializer_class = TemporadaSerializer

class EpisodioViewSet(viewsets.ModelViewSet):
    queryset = Episodio.objects.all()
    serializer_class = EpisodioSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class RolProduccionViewSet(viewsets.ModelViewSet):
    queryset = RolProduccion.objects.all()
    serializer_class = RolProduccionSerializer

class RepartoViewSet(viewsets.ModelViewSet):
    queryset = Reparto.objects.all()
    serializer_class = RepartoSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CriticoViewSet(viewsets.ModelViewSet):
    queryset = Critico.objects.all()
    serializer_class = CriticoSerializer

class ResenaViewSet(viewsets.ModelViewSet):
    queryset = Resena.objects.all()
    serializer_class = ResenaSerializer

class VisualizacionViewSet(viewsets.ModelViewSet):
    queryset = Visualizacion.objects.all()
    serializer_class = VisualizacionSerializer
