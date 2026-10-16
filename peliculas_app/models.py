from django.db import models

int_habilitado = 1
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"
str_codigo = "Código"
str_nombre = "Nombre"
str_descripcion = "Descripción"
str_www = "WWW"
str_email = "Email"
str_telefono = "Teléfono"
str_fecha_nac = "Fecha Nacimiento"

# ---------------------------------------------------------------------
# Países
# ---------------------------------------------------------------------

class Pais(models.Model):
    nombre = models.CharField("País",max_length=50,null=False)
    nacionalidad = models.CharField("Nacionalidad",max_length=30,null=False)
    iso_2 = models.CharField("ISO 2",max_length=2,null=False)
    iso_3 = models.CharField("ISO 3",max_length=3,null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table_comment = "Información de paises del mundo, para asociar a títulos, personas y usuarios."

# ---------------------------------------------------------------------
# Catálogo audiovisual
# ---------------------------------------------------------------------

class Genero(models.Model):
    genero = models.CharField("Género Audiovisual",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.genero
    class Meta:
        db_table_comment = "Géneros audiovisuales: acción, drama, comedia, documental, etc."

class Idioma(models.Model):
    idioma = models.CharField("Idioma",max_length=30,null=False)
    codigo = models.CharField(str_codigo,max_length=5,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.idioma
    class Meta:
        db_table_comment = "Idioma original y de doblaje de los títulos del catálogo."

class Clasificacion(models.Model):
    codigo = models.CharField(str_codigo,max_length=10,null=False)
    clasificacion = models.CharField("Clasificación",max_length=50,null=False)
    edad_minima = models.IntegerField("Edad Mínima",null=False,default=0)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.codigo} - {self.clasificacion}"
    class Meta:
        db_table_comment = "Clasificación por edad del contenido: TV-MA, PG-13, etc."

class Estado(models.Model):
    estado = models.CharField("Estado",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.estado
    class Meta:
        db_table_comment = "Estado de emisión de un título: estreno, en emisión, finalizado, cancelado."

class Productora(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    anio_fundacion = models.IntegerField("Año Fundación",null=True)
    web = models.URLField(str_www,null=True)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table_comment = "Estudios y casas productoras responsables de los títulos."

class Plataforma(models.Model):
    nombre = models.CharField(str_nombre,max_length=50,null=False)
    web = models.URLField(str_www,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table_comment = "Plataformas de streaming donde está disponible un título."

class Titulo(models.Model):
    TIPO_PELICULA = 'PELICULA'
    TIPO_SERIE = 'SERIE'
    TIPOS = [(TIPO_PELICULA,'Película'),(TIPO_SERIE,'Serie')]

    titulo = models.CharField("Título",max_length=150,null=False)
    titulo_original = models.CharField("Título Original",max_length=150,null=True)
    tipo = models.CharField("Tipo",max_length=10,choices=TIPOS,default=TIPO_PELICULA,null=False)
    sinopsis = models.TextField("Sinopsis",null=True)
    anio_estreno = models.IntegerField("Año Estreno",null=False)
    duracion = models.IntegerField("Duración (minutos)",null=True)
    genero = models.ForeignKey(Genero,on_delete=models.CASCADE,null=False)
    idioma = models.ForeignKey(Idioma,on_delete=models.CASCADE,null=False)
    clasificacion = models.ForeignKey(Clasificacion,on_delete=models.CASCADE,null=False)
    estado = models.ForeignKey(Estado,on_delete=models.CASCADE,null=False)
    productora = models.ForeignKey(Productora,on_delete=models.CASCADE,null=False)
    plataforma = models.ForeignKey(Plataforma,on_delete=models.CASCADE,null=True)
    pais_origen = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.titulo} ({self.anio_estreno})"
    class Meta:
        db_table_comment = "Obra audiovisual del catálogo: puede ser una película o una serie."

class Temporada(models.Model):
    serie = models.ForeignKey(Titulo,on_delete=models.CASCADE,null=False)
    numero = models.IntegerField("Número Temporada",null=False)
    nombre = models.CharField(str_nombre,max_length=100,null=True)
    anio_estreno = models.IntegerField("Año Estreno",null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.serie} - Temporada {self.numero}"
    class Meta:
        db_table_comment = "Temporadas de un título de tipo serie."

class Episodio(models.Model):
    temporada = models.ForeignKey(Temporada,on_delete=models.CASCADE,null=False)
    numero = models.IntegerField("Número Episodio",null=False)
    titulo = models.CharField("Título",max_length=150,null=False)
    sinopsis = models.TextField("Sinopsis",null=True)
    duracion = models.IntegerField("Duración (minutos)",null=True)
    fecha_emision = models.DateField("Fecha Emisión",null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.temporada} E{self.numero} - {self.titulo}"
    class Meta:
        db_table_comment = "Episodios pertenecientes a una temporada."

# ---------------------------------------------------------------------
# Personas y reparto
# ---------------------------------------------------------------------

class Persona(models.Model):
    nombre = models.CharField(str_nombre,max_length=100,null=False)
    pseudonimo = models.CharField("Pseudónimo",max_length=50,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(str_fecha_nac,null=True)
    fecha_defuncion = models.DateField("Fecha Defunción",null=True)
    biografia = models.TextField("Biografía",null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table_comment = "Personas del medio audiovisual: actores, directores, guionistas."

class RolProduccion(models.Model):
    rol = models.CharField("Rol",max_length=30,null=False)
    descripcion = models.CharField(str_descripcion,max_length=255,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return self.rol
    class Meta:
        db_table_comment = "Rol que cumple una persona en un título: actor, director, guionista."

class Reparto(models.Model):
    titulo = models.ForeignKey(Titulo,on_delete=models.CASCADE,null=False)
    persona = models.ForeignKey(Persona,on_delete=models.CASCADE,null=False)
    rol = models.ForeignKey(RolProduccion,on_delete=models.CASCADE,null=False)
    personaje = models.CharField("Personaje",max_length=100,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.persona} como {self.personaje or self.rol} en {self.titulo}"
    class Meta:
        db_table_comment = "Relaciona personas con títulos indicando el rol que cumplieron."

# ---------------------------------------------------------------------
# Usuarios y actividad
# ---------------------------------------------------------------------

class Usuario(models.Model):
    nombre = models.CharField(str_nombre,max_length=150,null=False)
    rut = models.CharField("RUT",max_length=12,null=False)
    correo = models.EmailField(str_email,null=True)
    telefono = models.CharField(str_telefono,max_length=15,null=True)
    nacionalidad = models.ForeignKey(Pais,on_delete=models.CASCADE,null=True)
    fecha_nacimiento = models.DateField(str_fecha_nac,null=False)
    contrasenia = models.CharField(max_length=128,null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.nombre} ({self.rut})"
    class Meta:
        db_table_comment = "Usuarios registrados en la plataforma audiovisual."

class Critico(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    medio = models.CharField("Medio",max_length=100,null=True)
    acreditacion = models.CharField("Acreditación",max_length=50,null=True)
    fecha_acreditacion = models.DateField("Fecha Acreditación",null=True)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.usuario} - {self.medio}"
    class Meta:
        db_table_comment = "Usuarios acreditados como críticos, con perfil de acceso diferenciado."

class Resena(models.Model):
    titulo = models.ForeignKey(Titulo,on_delete=models.CASCADE,null=False)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    puntuacion = models.IntegerField("Puntuación",null=False)
    comentario = models.TextField("Comentario",null=True)
    es_critica = models.BooleanField("Reseña de Crítico",default=False,null=False)
    publica = models.BooleanField("Pública",default=True,null=False)
    habilitado = models.BooleanField(int_habilitado,default=True,null=False)
    created_at = models.DateTimeField(str_fecha_creacion,auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion,auto_now=True)
    def __str__(self):
        return f"{self.usuario} -> {self.titulo}: {self.puntuacion}"
    class Meta:
        db_table_comment = "Reseñas y puntuaciones que los usuarios y críticos dan a un título."

class Visualizacion(models.Model):
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE,null=False)
    titulo = models.ForeignKey(Titulo,on_delete=models.CASCADE,null=False)
    episodio = models.ForeignKey(Episodio,on_delete=models.CASCADE,null=True)
    plataforma = models.ForeignKey(Plataforma,on_delete=models.CASCADE,null=True)
    fecha_inicio = models.DateTimeField("Fecha Inicio",auto_now_add=True)
    fecha_termino = models.DateTimeField("Fecha Término",null=True)
    minutos_vistos = models.IntegerField("Minutos Vistos",null=False,default=0)
    completada = models.BooleanField("Completada",default=False,null=False)
    def __str__(self):
        return f"{self.usuario} vio {self.episodio or self.titulo}"
    class Meta:
        db_table_comment = "Historial de visualizaciones, para auditoría y reportes de actividad."
