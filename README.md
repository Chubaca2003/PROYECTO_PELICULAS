# PROYECTO_PELICULAS — API de Películas y Series

Evaluación N.º 2 — Programación Backend — INACAP 2026
Proyecto asignado N.º 29: **API de Películas y Series**

API REST construida con Django REST Framework sobre un portal audiovisual.
Expone CRUD completo (GET, POST, PUT, PATCH y DELETE) para las 21 clases del
modelo de datos mediante `ModelViewSet` y un `DefaultRouter`.

## Requisitos previos

- Python 3.11 o superior
- MySQL 8 o superior en ejecución

## Puesta en marcha

1. **Ambiente virtual e instalación de dependencias**

    ```bash
    python3 -m venv venv
    source venv/bin/activate          # en Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

2. **Base de datos** — ejecutar los scripts de `sql/` en orden, como
   administrador de MySQL:

    ```bash
    mysql -u root -p < sql/01_crear_base_datos.sql    # crea proyecto_peliculas
    mysql -u root -p < sql/02_crear_usuario.sql       # crea peliculas_user
    mysql -u root -p < sql/03_asignar_permisos.sql    # otorga permisos
    ```

3. **Variables de entorno**

    ```bash
    cp .env.example .env
    ```

    El archivo `.env` contiene la `SECRET_KEY` y las credenciales de conexión.
    **No se versiona** (está excluido en `.gitignore`); `settings.py` las lee
    con `python-decouple`, de modo que no hay credenciales escritas en el código.

    Para generar una `SECRET_KEY` nueva:

    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```

4. **Migraciones y datos iniciales**

    ```bash
    python manage.py migrate
    python manage.py loaddata data_paises data_regiones data_provincias data_comunas \
        data_generos data_idiomas data_clasificaciones data_estados data_roles data_plataformas
    ```

5. **Ejecución**

    ```bash
    python manage.py runserver
    ```

    - Portada: <http://127.0.0.1:8000/>
    - API navegable: <http://127.0.0.1:8000/api/>
    - Administrador: <http://127.0.0.1:8000/admin/> (requiere `createsuperuser`)

## Modelo de datos

21 clases agrupadas en cuatro áreas:

**Ubicación geográfica** — `Pais`, `Region`, `Provincia`, `Comuna`, `Direccion`

**Catálogo audiovisual** — `Genero`, `Idioma`, `Clasificacion`, `Estado`,
`Productora`, `Plataforma`, `Titulo`, `Temporada`, `Episodio`

`Titulo` es la obra audiovisual y su campo `tipo` distingue entre `PELICULA` y
`SERIE`. Una serie se desglosa en `Temporada` y cada temporada en `Episodio`.

**Personas y reparto** — `Persona`, `RolProduccion`, `Reparto`

`Reparto` relaciona una `Persona` con un `Titulo` indicando el `RolProduccion`
que cumplió (actor, director, guionista) y el personaje interpretado.

**Usuarios y actividad** — `Usuario`, `Critico`, `Resena`, `Visualizacion`

`Critico` corresponde a un `Usuario` acreditado, lo que permite distinguir
perfiles de acceso. `Resena` registra puntuaciones y comentarios, y
`Visualizacion` mantiene el historial de reproducción para auditoría y reportes.

## Endpoints

Todos cuelgan de `/api/` y entregan el CRUD completo:

| Recurso | URL | Recurso | URL |
|---|---|---|---|
| País | `/api/paises/` | Título | `/api/titulos/` |
| Región | `/api/regiones/` | Temporada | `/api/temporadas/` |
| Provincia | `/api/provincias/` | Episodio | `/api/episodios/` |
| Comuna | `/api/comunas/` | Persona | `/api/personas/` |
| Dirección | `/api/direcciones/` | Rol de producción | `/api/roles/` |
| Género | `/api/generos/` | Reparto | `/api/repartos/` |
| Idioma | `/api/idiomas/` | Usuario | `/api/usuarios/` |
| Clasificación | `/api/clasificaciones/` | Crítico | `/api/criticos/` |
| Estado | `/api/estados/` | Reseña | `/api/resenas/` |
| Productora | `/api/productoras/` | Visualización | `/api/visualizaciones/` |
| Plataforma | `/api/plataformas/` | | |

Métodos disponibles en cada recurso:

| Método | URL | Acción |
|---|---|---|
| `GET` | `/api/<recurso>/` | Listar |
| `POST` | `/api/<recurso>/` | Crear |
| `GET` | `/api/<recurso>/<id>/` | Consultar uno |
| `PUT` | `/api/<recurso>/<id>/` | Actualizar completo |
| `PATCH` | `/api/<recurso>/<id>/` | Actualizar parcial |
| `DELETE` | `/api/<recurso>/<id>/` | Eliminar |

## Estructura del proyecto

```
backend_1/
├── drf/                    # Configuración del proyecto Django
│   ├── settings.py         # INSTALLED_APPS, DB y credenciales vía .env
│   └── urls.py             # Incluye las urls de peliculas_app
├── peliculas_app/          # Aplicación particular
│   ├── models.py           # 21 clases del modelo de datos
│   ├── serializer.py       # Un ModelSerializer por clase
│   ├── views.py            # Un ModelViewSet por clase + portada
│   ├── urls.py             # Router de DRF
│   ├── admin.py            # Registro de las 21 clases en el admin
│   ├── migrations/         # Migraciones del modelo
│   ├── fixtures/           # Datos iniciales
│   └── templates/          # Portada y página de sistema no disponible
├── sql/                    # Scripts de base de datos, usuario y permisos
├── .env                    # Datos sensibles (NO versionado)
├── .env.example            # Plantilla del archivo de ambiente
└── requirements.txt        # Dependencias
```

## Notas

**Nombres de las variables de entorno.** Las variables de base de datos llevan
el prefijo `DB_` porque `python-decouple` da prioridad a las variables del
sistema operativo por sobre el archivo `.env`. En macOS y Linux `USER` y `HOST`
ya existen —apuntan al usuario y al equipo—, de modo que sin el prefijo la
conexión tomaría esos valores en lugar de los de la base de datos.

**Interruptor de disponibilidad.** `SISTEMA_ABIERTO` en `settings.py` permite
cerrar el sitio: cuando está en `False` la portada responde `no_dispo.html` con
HTTP 503 en lugar de `index.html`.
