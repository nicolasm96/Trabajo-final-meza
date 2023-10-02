from django.urls import path
from django.views.generic import TemplateView


from . import views

app_name = "producto"

urlpatterns = [
    path("", TemplateView.as_view(template_name="producto/index.html"), name="index"),
]

# PRODUCTO

urlpatterns += [
    path("producto/list/", views.ProductoList.as_view(), name="producto_list"),
    path("producto/detail/<int:pk>", views.ProductoDetail.as_view(), name="producto_detail"),
    path("producto/create/", views.ProductoCreate.as_view(), name="producto_create"),

    
]
