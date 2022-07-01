from dataclasses import fields
from email.policy import default
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from app_proyecto import models
from app_proyecto.models import *
from datetime import date
from datetime import datetime
from django.contrib.admin import widgets
import urllib.request






class UserEditForm(UserCreationForm):
    username= forms.CharField(label="username", max_length=30, min_length=3)
    email= forms.EmailField(label="agregar/modificar mail", required=False)
    password1= forms.CharField(label="password", widget=forms.PasswordInput)
    password2= forms.CharField(label="repeat password", widget=forms.PasswordInput)

    class Meta: 
        model= User
        fields= ['username','email', 'password1', 'password2']
        help_text={k:"" for k in fields}




class formulario_post(forms.ModelForm):
    def __str__(self):
        return f"titulo: {self.titulo} - subtitulo :{self.subtitulo} cuerpo: {self.cuerpo} imagen: {self.imagen} autor: {self.autor} fecha {self.fecha}"
    titulo= models.CharField(max_length=100)
    subtitulo= models.CharField(max_length=50)
    cuerpo= models.TextField()
    imagen= models.ImageField(upload_to='posts' , null=True , blank=True)
    autor= models.ForeignKey(User, on_delete=models.CASCADE) 
    fecha= models.DateField(default= date.today)
    class Meta:
        model= Post
        fields= '__all__'
    

class editPost(forms.ModelForm):
  
    class Meta:
        model= Post
        fields= ('titulo', 'subtitulo' ,'autor', 'cuerpo', 'imagen', 'fecha')


class formulario_comentario(forms.ModelForm):
    comentario= models.TextField()
    autor= models.ForeignKey(User, on_delete=models.CASCADE) 
    class Meta:
        model= Comentario
        fields= ('comentario', 'autor', 'post')

class formularioAvatar(forms.ModelForm):

    class Meta:
        model= Avatar
        fields= ('imagen',)
       

