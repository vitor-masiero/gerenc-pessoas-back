from django.urls import path
from app.faces.views import FaceRegisterView, FaceDeleteView, FaceUpdateView, FaceValidationView

urlpatterns = [
    path('register/', FaceRegisterView.as_view(), name='face-register'),
    path('<int:id>/delete/', FaceDeleteView.as_view(), name='face-delete'),
    path('<int:id>/update/', FaceUpdateView.as_view(), name='face-update'),
    path('faces/validar/', FaceValidationView.as_view(), name='validar-face'),
]