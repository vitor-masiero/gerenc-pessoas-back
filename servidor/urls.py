
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/enderecos/', include('app.enderecos.urls')),
    path('api/usuarios/', include('app.usuarios.urls')),
    path('api/faces/', include('app.faces.urls')),
    path('api/relatorios/', include('app.relatorios.urls')),
    path('api/empresas/', include('app.empresas.urls')),
    path('api/tentativas-acesso/', include('app.tentativas_acesso.urls')),
    path('api/tentativas-acesso-anonimo/', include('app.tentativas_acesso_anonimo.urls')),
    path('api/faces-anonimas/', include('app.faces_anonimas.urls')),
    path('api/usuarios-empresa/', include('app.usuarios_empresas.urls')),
]

