from django.urls import path
from app.faces_anonimas.views import FaceAnonimaDeleteView, FaceAnonimaRegisterView

urlpatterns = [
    path('register/', FaceAnonimaRegisterView.as_view(), name='face-register'),
    path('<int:id>/delete/', FaceAnonimaDeleteView.as_view(), name='face-delete'),
]