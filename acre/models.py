from django.db import models

# Create your models here.
class Dominio(models.Model):
    iddominio = models.IntegerField(primary_key=True, verbose_name='id de dominio')
    nomdominio = models.CharField(max_length=20, verbose_name='Nombre de dominio')

    def __str__(self):
        return self.nomdominio

class Seccion(models.Model):
    idseccion = models.IntegerField(primary_key=True, verbose_name='id de seccion')
    nomseccion = models.CharField(max_length=20, verbose_name='Nombre de seccion')
    

    def __str__(self):
        return self.nomseccion

class Capitulo(models.Model):
    idcapitulo =  models.CharField(primary_key=True,max_length=20 , verbose_name='id de capitulo')
    nomcapitulo = models.CharField(max_length=80,verbose_name='Nombre de capitulo')
    numcapitulo = models.IntegerField(null= True, verbose_name='Numero de capitulo')
    url = models.CharField(max_length=200,verbose_name='Link de video')
    imgcap = models.ImageField(upload_to="capitulo", blank=False)
    dominio = models.ForeignKey(Dominio,on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion,on_delete=models.CASCADE)

    def __str__(self):
        return self.idcapitulo



   

class Wiki(models.Model):
    idwiki = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=40,verbose_name='Titulo wiki')
    texto = models.TextField(max_length=1000,verbose_name='Texto wiki')
    imagen = models.ImageField(upload_to="mapa", blank=True )
    titulo2 = models.CharField(blank=True, max_length=40,verbose_name='Segundo titulo')
    texto2 = models.TextField(blank=True ,max_length=1000,verbose_name='Texto wiki')
    imagen2 = models.ImageField(upload_to="mapa2", blank=True )
    capitulo = models.ForeignKey(Capitulo,on_delete=models.CASCADE)

    

    def __str__(self):
        return self.titulo        



class Comentario(models.Model):
    idcoment = models.AutoField(primary_key=True, verbose_name='Id comentario')
    comentario = models.TextField(max_length= 500, verbose_name= 'Comentario' )
    capitulo = models.ForeignKey(Capitulo,on_delete=models.CASCADE)
       