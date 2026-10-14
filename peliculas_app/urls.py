from django.urls import path, include
from rest_framework import routers
from peliculas_app import views

# El Router genera automáticamente las urls de cada ModelViewSet:
#   /<recurso>/        -> GET (list)     y POST (create)
#   /<recurso>/<pk>/   -> GET (retrieve), PUT, PATCH y DELETE
enrutador = routers.DefaultRouter()

enrutador.register(r'paises', views.PaisViewSet)
enrutador.register(r'regiones', views.RegionViewSet)
enrutador.register(r'provincias', views.ProvinciaViewSet)
enrutador.register(r'comunas', views.ComunaViewSet)
enrutador.register(r'direcciones', views.DireccionViewSet)
enrutador.register(r'generos', views.GeneroViewSet)
enrutador.register(r'idiomas', views.IdiomaViewSet)
enrutador.register(r'clasificaciones', views.ClasificacionViewSet)
enrutador.register(r'estados', views.EstadoViewSet)
enrutador.register(r'productoras', views.ProductoraViewSet)
enrutador.register(r'plataformas', views.PlataformaViewSet)
enrutador.register(r'titulos', views.TituloViewSet)
enrutador.register(r'temporadas', views.TemporadaViewSet)
enrutador.register(r'episodios', views.EpisodioViewSet)
enrutador.register(r'personas', views.PersonaViewSet)
enrutador.register(r'roles', views.RolProduccionViewSet)
enrutador.register(r'repartos', views.RepartoViewSet)
enrutador.register(r'usuarios', views.UsuarioViewSet)
enrutador.register(r'criticos', views.CriticoViewSet)
enrutador.register(r'resenas', views.ResenaViewSet)
enrutador.register(r'visualizaciones', views.VisualizacionViewSet)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('api/', include(enrutador.urls)),
]
