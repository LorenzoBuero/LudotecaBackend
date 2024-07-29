from django.db import models

# Create your models here.
class Project(models.Model):
    id = models.AutoField(primary_key=True)  #id = models.IntegerField(primary_key=True)
    
    titulo = models.CharField(max_length=100, verbose_name = 'título', default="")
    subtitulo_1 = models.CharField(max_length=200, verbose_name = 'subtitulo 1', default="")
    imagen_caratula = models.ImageField(verbose_name = 'imagen de la caratula', upload_to="resenias", null=True)
    
    parrafo_1 = models.TextField(verbose_name = 'primer parrafo', default="")
    imagen_1 = models.ImageField(verbose_name = 'imagen 1', upload_to="", null=True)
    imagen_2 = models.ImageField(verbose_name = 'imagen 2', upload_to="", null=True)
    subtitulo_2 = models.CharField(max_length=200, verbose_name = 'subtitulo 2', default="")
    parrafo_2 = models.TextField(verbose_name = 'segundo parrafo', default="")
    
    sintesis = models.TextField(verbose_name = 'síntesis', default="")
    nota = models.CharField(max_length=10,verbose_name = 'nota', default="")
    
    aside_generos = models.CharField(max_length=300, default="")
    aside_plataformas = models.CharField(max_length = 200, default="")
    aside_creador = models.CharField(max_length=200, default="")
    aside_pais_origen = models.CharField(max_length=200, default="")
    aside_dato_curioso = models.TextField(default="")
    
    creado = models.DateTimeField(auto_now_add=True, verbose_name = 'Fecha de creación: ', null=True)
    actualizado = models.DateTimeField(auto_now=True, verbose_name = 'Fecha de modificación: ', null=True)
    
    
    class Meta:
        verbose_name = 'Reseña'
        verbose_name_plural = 'Reseñas'
        ordering = ['-creado']
        
        
    def __str__(self) -> str:
        return self.titulo
    
    
    
