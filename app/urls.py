from django.urls import path
from .views import FaceRegisterView

urlpatterns = [
    path('', FaceRegisterView.as_view())
]

