from django.urls import path
from .views import producto_list, registrar_producto, mostrar_username, producto_detalle

urlpatterns = [
    path('', producto_list, name='producto_list'),
    path('registrar/', registrar_producto, name='registrar_producto'),
    path('productos/', producto_list, name='producto_list'),
    path('producto/username/<str:cadena>/', mostrar_username, name='mostrar_username'),
    path('producto/<int:id>/', producto_detalle, name='producto_detalle'),
]