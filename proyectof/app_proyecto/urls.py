from django.urls import path
from app_proyecto import views
from django.contrib.auth.views import LogoutView





urlpatterns = [
    path('', views.inicio),
    path("register" , views.register , name="Register"),
    path("login" , views.login_request , name="Login"),
    path("logout", LogoutView.as_view (template_name="logout.html"), name="Logout"),
    path('editar_perfil', views.editarPerfil, name='editarPerfil'   ),
    path('crear_post', views.crear_post, name='Crear_post'),
    path('leer_post', views.leerpost, name="LeerPost"),
    path('borrarPost/<int:id>', views.borrarpost , name="BorrarPost"),
    path('borrarComentario/<int:id>', views.borrarComentario, name='BorrarComentario'),
    path('editarPost/<int:id>', views.editarPost, name="editarPost"),
    path('editarPost/', views.editarPost, name="editarPost"),
    path('editarcomentario/<int:id>', views.editarComent, name='EditarComentario'),
    path('editarcomentario/', views.editarComent, name='EditarComentario'),
    path('comentar/<int:id>', views.crear_coment, name='Comentar'),
    path('comentar/', views.crear_coment, name="Comentar"),
    path('pages', views.leer_comentarios, name="Pages"),
    path('panelUsuario', views.panel_usuario, name='PanelUsuario'),
    path('agregar_avatar',  views.AgregarAvatar, name="AgregarAvatar"),
    path('eliminar_avatar/<int:id>', views.BorrarAvatar, name='BorrarAvatar')
]
