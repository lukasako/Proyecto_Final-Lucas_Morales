from datetime import datetime
import re
from PIL import Image
from django.shortcuts import redirect, render
import urllib.request
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import AuthenticationForm , UserCreationForm
from django.contrib.auth import login , authenticate
from django.contrib.auth.decorators import login_required
from app_proyecto.models import Avatar, Post, Comentario
from app_proyecto.forms import UserEditForm
from app_proyecto.forms import *
from django.contrib.auth.models import User
from django.shortcuts import  get_object_or_404

def inicio(request):
           
             
    if request.user.is_authenticated is not None:
        user= User.objects.all()        
        avatares = Avatar.objects.filter(user=request.user.id)
        
        if avatares:
            return render( request , "plantillas.html", { "url":avatares[0].imagen.url })
        else:
            default= "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20"
            return render(request, 'plantillas.html', {'url': default} )
    return render(request, 'plantillas.html' )
    


def register(request):

    if request.user.is_authenticated:
        return redirect('PanelUsuario')

    if request.method == "POST":

        form= UserCreationForm(request.POST)

        if form.is_valid():

            form.save()
            return render(request, 'RegistroExitoso.html')

        else:
            form = UserCreationForm()
            mensaje= ("Ingresa los datos como se indica")
            return render( request , "registro.html" , {"form":form, "mensaje":mensaje})

    else:
        form = UserCreationForm()
        return render( request , "registro.html" , {"form":form})

    return render (request, "registro.html" )

def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)
            
             
            if user is not None:
                
                login(request,user)    
                
                avatares = Avatar.objects.filter(user=request.user.id)
                
                if avatares:
                    return render( request , "login.html", { "url":avatares[0].imagen.url })
                else:
                    default= "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20"
                    return render(request, 'login.html', {'url': default} )
            
            else:      
                form = AuthenticationForm()   
                mensaje= ("No se encontro el usuario, verifique los datos o cree un usuario")
                return render (request, "login.html", {'form':form, 'mensaje': mensaje})
            
        else:      
            form = AuthenticationForm()   
            mensaje= ("No se encontro el usuario, verifique los datos o cree un usuario")
            return render (request, "login.html", {'form':form, 'mensaje': mensaje})
            

    form = AuthenticationForm()

    return render( request , "login.html" , {"form":form})



@login_required
def editarPerfil(request):
    avatares= Avatar.objects.filter(user=request.user.id)
    usuario= request.user 
    if request.method == 'POST':
        
        miFormulario= UserEditForm(request.POST)

        if miFormulario.is_valid():

            info= miFormulario.cleaned_data

            usuario.username= info['username']
            password= info ['password1']
            usuario.set_password(password)
            usuario.save()

            return redirect('PanelUsuario')
    else:
        
        if avatares:
            miFormulario= {"url":avatares[0].imagen.url,  "miFormulario":UserEditForm(initial={'email':usuario.email })}
        else:
            miFormulario= {"url":"https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20",  "miFormulario":UserEditForm(initial={'email':usuario.email })}

    return render(request, "editar_perfil.html", miFormulario)
 
def pages(request):
    return render(request, "pages.html" )

@login_required
def crear_post(request):


    if request.method == "POST":
        
        formulario= formulario_post(data=request.POST, files=request.FILES)
        
        if formulario.is_valid():
            formulario.save()
            return redirect('Pages')
        else: 
            return HttpResponse("error") 

    else:
        avatares= Avatar.objects.filter(user=request.user.id)
    
        if avatares:
            Ava= {"url":avatares[0].imagen.url, 'form': formulario_post()}
    
        else:
            Ava= {"url":"https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", 'form': formulario_post()}
          
    return render(request, 'crear_post.html' , Ava)


def posts(request):
    
    posts= Post.objects.all()
    dicc= {'posts': posts}
    plantilla= loader.get_template('leerpost.html')
    documento= plantilla.render(dicc)
    return HttpResponse(documento)


@login_required
def leerpost(request):

    post= Post.objects.all()

    contexto= {"post":post}

    return render(request, "leerpost.html", contexto )

@login_required
def borrarpost(request, id):
    
    post= Post.objects.get(id=id)
    post.delete()

    post= Post.objects.all()

    return redirect('PanelUsuario')


@login_required 
def editarPost(request, id):

    post= Post.objects.get(id=id)
    
    if request.method == "POST":
        
        miFormulario= formulario_post(request.POST, files=request.FILES)
        
        if miFormulario.is_valid():

            datos= miFormulario.cleaned_data

            post.titulo= datos['titulo']
            post.subtitulo= datos ['subtitulo']
            post.cuerpo= datos ['cuerpo']
            post.autor= datos ['autor']
            post.imagen= datos ['imagen']
            post.fecha= datos ['fecha']
            
            post.save()

            post= Post.objects.all()
            return redirect('Pages')
        
    else:
        miFormulario= formulario_post(request.POST, files=request.FILES)
        avatares = Avatar.objects.filter(user=request.user.id) 
        if avatares:
            documento= {'url':avatares[0].imagen.url, 'post':post,"miFormulario": formulario_post(initial={'titulo':post.titulo, 
            'subtitulo':post.subtitulo,
                'cuerpo':post.cuerpo, 'autor':post.autor,
                    'imagen':post.imagen,})}
            return render(request, "editarpost.html", documento )
        
        else:
            documento= {"url": "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "post":post,"miFormulario": formulario_post(initial={'titulo':post.titulo, 
            'subtitulo':post.subtitulo,
                'cuerpo':post.cuerpo, 'autor':post.autor,
                    'imagen':post.imagen,})}
            return render(request, "editarpost.html", documento )
            
    return render( request , "editarpost.html" , documento)



def leer_comentarios(request):
    
    comentario= Comentario.objects.all()
    post= Post.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    

    if avatares:
        documento= {'url':avatares[0].imagen.url , "post":post , "comentario": comentario}
        return render(request, "leercoments.html", documento )
    
    else:
        documento= {"url": "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "post":post , "comentario":comentario}
        return render(request, "leercoments.html", documento )



def coments(request):
    
    coments= Comentario.objects.all()
    dicc= {'comentario': coments}
    plantilla= loader.get_template('leercoments.html')
    documento= plantilla.render(dicc)
    return HttpResponse(documento)

@login_required
def crear_coment(request, id):
    comentario= Comentario.objects.all()
    post= Post.objects.get(id=id)
    user= User.objects.filter(username=request.user.username)
    avatares= Avatar.objects.filter(user=request.user.id)
    
    post.id= [id]
    user.username= [user]
    if avatares:
        miFormulario={'url':avatares[0].imagen.url, "form" :formulario_comentario(initial= {"comentario": 'Escribir comentario', "post": post, "autor": user.username})}
    else: 
        miFormulario={'url':"https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "form" :formulario_comentario(initial= {"comentario": 'Escribir comentario', "post": post, "autor": user.username})}

    formulario= formulario_comentario(request.POST)

    if request.method == "POST":
        
        post.id= [id]
        comentario.autor= ['autor']
        
        if formulario.is_valid():
            
            formulario.save()

            return redirect ('Pages')

    return render (request, 'crear_comentario.html', miFormulario)
        

@login_required
def panel_usuario(request):
    
    comentario= Comentario.objects.all()
    post= Post.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    avatarb= Avatar.objects.all()
    
    if avatares:
        documento= {'url':avatares[0].imagen.url , "post": post , "comentario":comentario}
        return render(request, "panelusuario.html", documento )
    
    else:
        documento= {"url": "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "post": post , "comentario":comentario}
        return render(request, "panelusuario.html", documento )

  

@login_required
def editarComent(request, id):
   
    comentario= Comentario.objects.get(id=id)
    
    if request.method == "POST":
        
        miFormulario= formulario_comentario(request.POST, files=request.FILES)
        
        if miFormulario.is_valid():

            datos= miFormulario.cleaned_data

            comentario.comentario= datos ['comentario']
            comentario.autor= datos ['autor']
            comentario.post_id = datos ['post']
            
            comentario.save()

            comentario= Comentario.objects.all()
            return redirect('PanelUsuario')
        
    else:
        miFormulario= formulario_comentario(request.POST, files=request.FILES)
        avatares = Avatar.objects.filter(user=request.user.id) 

        if avatares:
            documento= {'url':avatares[0].imagen.url, 'comentario': comentario,"miFormulario": formulario_comentario(initial={'comentario': comentario.comentario, 
            'autor': comentario.autor,
                'post': comentario.post_id})}
            return render(request, "editarcomentario.html", documento)
        
        else:
            documento= {"url": "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "comentario": comentario ,"miFormulario": formulario_comentario(initial={'comentario': comentario.comentario, 
            'autor': comentario.autor,
                'post': comentario.post_id})}
            return render(request, "editarcomentario.html", documento)
            
    return render( request , "editarcomentario.html", documento)

@login_required
def borrarComentario(request, id):
    
    comentario= Comentario.objects.get(id=id)

    comentario.delete()


    return render(request, 'comentarioborrado.html', {"comentario": comentario})



@login_required
def AgregarAvatar(request):

    if request.method == "POST":

        miFormulario= formularioAvatar(request.POST, request.FILES)

        if miFormulario.is_valid():

            user= User.objects.get(username=request.user)
            avatar= Avatar (user=user, imagen= miFormulario.cleaned_data['imagen'])
            avatar.save()

            return redirect ('PanelUsuario')

    else: 
        avatares = Avatar.objects.filter(user=request.user.id) 
        avatar= Avatar.objects.all()

        if avatares:
            documento= {'url':avatares[0].imagen.url, "miFormulario": formularioAvatar, "avatar":avatar}
            return render(request, "editaravatar.html", documento)
        
        else:
            documento= {"url": "https://www.softzone.es/app/uploads/2018/04/guest.png?x=480&quality=20", "miFormulario": formularioAvatar, "avatar": avatar}
            return render(request, "editaravatar.html", documento)

    return render(request, "editaravatar.html", documento)

def BorrarAvatar(request, id):

    avatares= Avatar.objects.get(id=id)

    avatares.delete()

    return render(request, 'comentarioborrado.html', {"avatares": avatares})
        

    