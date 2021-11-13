from django.contrib import admin
from .models import Categoria, Post, Subcategoria

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class SubcategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Subcategoria, CategoriaAdmin)
admin.site.register(Categoria, SubcategoriaAdmin)
admin.site.register(Post, PostAdmin)