
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [

    path('', views.blog, name="Blog"),
    path('categoria/<int:categoria_id>', views.categoria, name="categoria"), 
    path('subcategoria/<int:subcategoria_id>', views.subcategoria, name="subcategoria"),   
    path('post/<int:post_id>', views.post, name="post"), 
    path('galeria', views.galeriaCloudinary, name="galeria"),
    path('electronic_component', views.electronic_component, name="electronic_component"),
    path('componentCategory/<int:componentCategory_id>', views.componentCategory, name="componentCategory"), 
      
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
