from django.urls import path

from . import views

app_name = "comentario"

urlpatterns = [
path("", views.index, name="index"),
path("exito_comentario/",views.exito_comentario, name= "exito_comentario")
]
