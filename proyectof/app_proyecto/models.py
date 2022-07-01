from django.db import models
from django.contrib.auth.models import User
from datetime import date
from django.utils import timezone


class Avatar(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(default='usuario.jpg' ,upload_to='avatares' , null=True ) 


class Post(models.Model):
    def __str__(self):
        return f"titulo: {self.titulo} - subtitulo :{self.subtitulo} cuerpo: {self.cuerpo} imagen: {self.imagen} autor: {self.autor} fecha {self.fecha}"
    titulo= models.CharField(max_length=100)
    subtitulo= models.CharField(max_length=50)
    cuerpo= models.TextField()
    imagen= models.ImageField(upload_to='posts' , null=True , blank=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE) 
    fecha= models.DateField(default= date.today)
   

class Comentario (models.Model):
    def __str__(self):
        return f"comentario:{self.comentario} autor{self.autor} post{self.post}"
    
    post= models.ForeignKey(Post, on_delete=models.CASCADE)
    comentario= models.TextField(max_length=200)
    autor= models.ForeignKey(User, on_delete=models.CASCADE,)

    

