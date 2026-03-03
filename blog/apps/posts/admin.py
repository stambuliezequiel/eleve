from django.contrib import admin
from .models import Categoria, Post


# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display= ('id', 'titulo', 'subtitulo', 'texto', 'activo', 'categoria', 'publicado', 'imagen', 'fecha' )


admin.site.register(Categoria)