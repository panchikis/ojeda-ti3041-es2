from django.urls import path
from . import views

app_name = "catalogo"

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("catalogo/", views.lista, name="lista"),
    path("producto/<int:id>/imagen.svg", views.imagen_producto, name="imagen_producto"),
    path("producto/<int:id>/", views.detalle, name="detalle"),
    path("comprar/<int:id>/", views.comprar, name="comprar"),
    path("administrar/agregar/", views.agregar_producto, name="agregar_producto"),
    path("administrar/stock/<int:id>/", views.agregar_stock, name="agregar_stock"),
]
