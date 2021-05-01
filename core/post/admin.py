from django.contrib import admin
from .models import Categoria,Publicacao
# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    prepopulated_fields = {'slug': ('title',)}
    


class PublicacaoAdmin(admin.ModelAdmin):
    list_display = ['title', 'category','updated_at', 'image_table']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_table',)
    list_filter = ['category']

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Publicacao, PublicacaoAdmin)