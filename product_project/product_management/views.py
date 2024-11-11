from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Product


class BaseProductView:
    model = Product

    def get_template_names(self):
        view_name = self.__class__.__name__.replace("Product", "").lower()
        return [f"product_{view_name}.html"]


class ProductList(BaseProductView, ListView):
    context_object_name = "products"


class ProductDetail(BaseProductView, DetailView):
    context_object_name = "product"


class ProductCreate(BaseProductView, CreateView, LoginRequiredMixin):
    fields = ["name", "description", "price"]

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('product_list')


class ProductUpdate(BaseProductView, UpdateView, LoginRequiredMixin):
    fields = ["name", "description", "price"]

    def get_success_url(self):
        return reverse_lazy('product_update', kwargs={"pk": self.object.pk})

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ProductDelete(BaseProductView, DeleteView, LoginRequiredMixin):
    def get_success_url(self):
        return reverse_lazy('product_list')

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
