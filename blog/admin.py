from django.contrib import admin
from django.utils.html import format_html
from .models import Categoria, Post, PostSection,PostSectionElement, Subcategoria, CloudinaryMedia, CloudinaryFile, ElectronicComponent, DeviceCategory

# Register your models here.
class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    
class SubcategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')


class PostAdmin(admin.ModelAdmin):
    list_display = ("title","created","subcategoriaprincial","description","post_image")
    search_fields = ['title', 'description']
  #  seach_fields = ("title","subcategoriaprincial")
    readonly_fields=('created','updated')
    list_filter=["subcategorias"]
    date_hierarchy=("created")

class CloudinaryMediaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class CloudinaryFileAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostSectionAdmin(admin.ModelAdmin):
    list_display = ("relatedPost","__str__","created") 
    list_filter=["relatedPost", "created"]
   # search_fields = ['relatedPost']   
    readonly_fields=('created','updated')
    date_hierarchy=("created")

class PostSectionElementAdmin(admin.ModelAdmin):
   
    readonly_fields=('created','updated')
    list_display = ("__str__","created","body", 'image_tag') 
    list_filter=[ "created"]
    
    
class ElectronicComponentAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    list_display = ("deviceName","deviceType","deviceDescription","created") 
        
class DeviceCategoryAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated') 
    
admin.site.register(Subcategoria, CategoriaAdmin)
admin.site.register(Categoria, SubcategoriaAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostSection, PostSectionAdmin)
admin.site.register(PostSectionElement, PostSectionElementAdmin)
admin.site.register(CloudinaryMedia, CloudinaryMediaAdmin)
admin.site.register(CloudinaryFile, CloudinaryFileAdmin)
admin.site.register(ElectronicComponent, ElectronicComponentAdmin)
admin.site.register(DeviceCategory, DeviceCategoryAdmin)