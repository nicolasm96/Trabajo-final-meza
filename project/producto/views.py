from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy


from . import forms, models


class ProductoList(ListView):
    model = models.Producto

    def get_queryset(self):
        if self.request.GET.get("buscar"):
            consulta = self.request.GET.get("buscar")
            object_list = models.Producto.objects.filter(nombre__icontains=consulta)
        else:
            object_list = models.Producto.objects.all()
        return object_list
    
      
class ProductoDetail(DetailView):
    model = models.Producto
   

class ProductoCreate(CreateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoUpdate(UpdateView):
    model = models.Producto
    form_class = forms.ProductoForm
    success_url = reverse_lazy("producto:producto_list")


class ProductoDelete(DeleteView):
    model = models.Producto
    success_url = reverse_lazy("producto:producto_list")



# Create your views here.
