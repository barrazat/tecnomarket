from django.urls import path, include
from .views import home, contacto, galeria,agregar_marca, agregar_producto, listar_productos, modificar_producto,eliminar_producto, registro, ProductoViewSet, MarcaViewset, error_facebook,unico
from rest_framework import routers

router = routers.DefaultRouter()
router.register('producto', ProductoViewSet)
router.register('marca', MarcaViewset)

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('agregar-marca/', agregar_marca, name="agregar_marca"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/', listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar-producto/<id>/', eliminar_producto, name="eliminar_producto"),
    path('registro/', registro, name="registro"),
    path('api/', include(router.urls)),
    path('error-facebook/',error_facebook,name="error_facebook"),
    path('unico/<id>/', unico, name="unico"),
]