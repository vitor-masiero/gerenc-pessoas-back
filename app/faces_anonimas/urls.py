from django.urls import path
from app.faces_anonimas.views import FacesAnonimas, FacesAnonimasPorEmpresaView

urlpatterns = [
    path('', FacesAnonimas.as_view()),
    path('empresa/', FacesAnonimasPorEmpresaView.as_view())
]