from django.contrib import admin
from .models import Categoria, Post, Subcategoria, CloudinaryMedia, CloudinaryFile

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class SubcategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class CloudinaryMediaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class CloudinaryFileAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Subcategoria, CategoriaAdmin)
admin.site.register(Categoria, SubcategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(CloudinaryMedia, CloudinaryMediaAdmin)
admin.site.register(CloudinaryFile, CloudinaryFileAdmin)
