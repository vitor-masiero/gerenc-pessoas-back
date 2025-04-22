
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/enderecos', include('app.enderecos.urls')),
    path('api/usuarios', include('app.usuarios.urls')),
    path('api/faces', include('app.faces.urls')),
    path('api/relatorios', include('app.relatorios.urls')),
    path('api/empresas', include('app.empresas.urls')),
]

