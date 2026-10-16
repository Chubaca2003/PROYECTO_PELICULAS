from django.contrib import admin

from .models import Pais
from .models import Genero
from .models import Idioma
from .models import Clasificacion
from .models import Estado
from .models import Productora
from .models import Plataforma
from .models import Titulo
from .models import Temporada
from .models import Episodio
from .models import Persona
from .models import RolProduccion
from .models import Reparto
from .models import Usuario
from .models import Critico
from .models import Resena
from .models import Visualizacion

# Register your models here.
admin.site.register(Pais)
admin.site.register(Genero)
admin.site.register(Idioma)
admin.site.register(Clasificacion)
admin.site.register(Estado)
admin.site.register(Productora)
admin.site.register(Plataforma)
admin.site.register(Titulo)
admin.site.register(Temporada)
admin.site.register(Episodio)
admin.site.register(Persona)
admin.site.register(RolProduccion)
admin.site.register(Reparto)
admin.site.register(Usuario)
admin.site.register(Critico)
admin.site.register(Resena)
admin.site.register(Visualizacion)
