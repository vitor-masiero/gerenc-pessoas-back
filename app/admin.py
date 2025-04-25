from django.utils.html import mark_safe
from django.contrib import admin
from app.faces_anonimas.models import FaceAnonima

@admin.register(FaceAnonima)
class FaceAnonimaAdmin(admin.ModelAdmin):
    list_display = ['id_empresa', 'dt_criado', 'preview']

    def preview(self, obj):
        if obj.imagem:
            return mark_safe(f'<img src="{obj.imagem.url}" width="100" />')
        return "Sem imagem"
