
from django.contrib import admin
from django.urls import include, path
import app_proyecto
from app_proyecto import urls
from django.conf import settings 
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'app_proyecto/', include(app_proyecto.urls) ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT ) 