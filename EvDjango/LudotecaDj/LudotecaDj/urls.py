"""
URL configuration for LudotecaDj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views as core_views
from resenias import views as resenias_views
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name="index"),
    path('buscador-resenias/', resenias_views.buscador_resenias, name="buscador-resenias"),
    path('contacto/', core_views.contacto, name="contacto"),
    path('sobre-nosotros/', core_views.sobre_nosotros, name="sobre-nosotros"),
    path('resenias/<int:pk>', resenias_views.resenia, name="resenia"),
        
    ]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
