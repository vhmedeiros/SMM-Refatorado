from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.template.loader import render_to_string
from django.contrib import messages
from django.http import HttpResponse
from .models import Categoriapalavrachave, Palavrachave
from .forms import CategoriaForm, PalavraChaveForm
from clientes.models import ErpCliente


class CategoriaListView(ListView):
    model = Categoriapalavrachave
    template_name = "palavras_chave/categoria_list.html"
    context_object_name = "categorias"

    def get_queryset(self):
        self.cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        return Categoriapalavrachave.objects.filter(id_cliente=self.cliente)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs) # pega o contexto listview
        context["cliente_selecionado"] = self.cliente
        return context

    def get(self, request, *args, **kwargs):
        self.cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        request.session["cliente_selecionado"] = {
            "id_cliente": self.cliente.id_cliente
        }
        request.session.modified = True
        return super().get(request, *args, **kwargs)


class CategoriaCreateView(CreateView):
    model = Categoriapalavrachave
    form_class = CategoriaForm
    template_name = "palavras_chave/categoria_create.html"

    def form_valid(self, form):
        form.instance.id_cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("palavras_chave:categoria_list", kwargs={"id_cliente": self.kwargs["id_cliente"]})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cliente_selecionado"] = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        context["id_cliente"] = self.kwargs["id_cliente"]
        return context

    def get(self, request, *args, **kwargs):
        cliente = get_object_or_404(ErpCliente, pk=self.kwargs["id_cliente"])
        request.session["cliente_selecionado"] = {
            "id_cliente": cliente.id_cliente
        }
        request.session.modified = True
        return super().get(request, *args, **kwargs)

class CategoriaUpdateView(UpdateView):
    model = Categoriapalavrachave
    form_class = CategoriaForm
    template_name = "palavras_chave/categoria_update.html"

    def get_success_url(self):
        return reverse_lazy("palavras_chave:categoria_list", kwargs={"id_cliente": self.object.id_cliente_id})


class CategoriaDeleteView(DeleteView):
    model = Categoriapalavrachave
    template_name = "palavras_chave/categoria_delete.html"

    def get_object(self, get_queryset=None):
        return get_object_or_404(
            Categoriapalavrachave.objects.select_related("id_cliente"),
            pk=self.kwargs["pk"]
        )
    
    def get_context_data(self, **kwargs):
        print('DEBUG - cliente:', self.object.id_cliente)

        context = super().get_context_data(**kwargs)
        # categoria = self.get_object()
        context["cliente_selecionado"] = self.object.id_cliente
        return context

    def get_success_url(self):
        return reverse("palavras_chave:categoria_list", kwargs={
            "id_cliente": self.object.id_cliente.id_cliente
        })



class PalavraChaveCreateView(CreateView):
    model = Palavrachave
    form_class = PalavraChaveForm
    template_name = "palavras_chave/palavra_chave_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.id_cliente = self.kwargs["id_cliente"]
        self.id_categoria = self.kwargs["id_categoria"] # vem da url
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        # kwargs['id_categoria'] = self.id_categoria  # necessário para validação no form
        return kwargs

    def form_valid(self, form):
        cliente = get_object_or_404(ErpCliente, id_cliente=self.id_cliente)
        categoria = get_object_or_404(Categoriapalavrachave, pk=self.id_categoria)
        form.instance.id_cliente = cliente
        form.instance.id_categoria = categoria
        messages.success(self.request, "Palavra-chave criada com sucesso.")
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("palavras_chave:categoria_list", kwargs={"id_cliente": self.id_cliente})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cliente = get_object_or_404(ErpCliente, id_cliente=self.id_cliente)
        categoria = get_object_or_404(Categoriapalavrachave, pk=self.id_categoria)
        context["cliente_selecionado"] = cliente
        context["categoria"] = categoria
        return context

    def get(self, request, *args, **kwargs):
        cliente = get_object_or_404(ErpCliente, id_cliente=self.kwargs["id_cliente"])
        request.session["cliente_selecionado"] = {
            "id_cliente": cliente.id_cliente
        }
        request.session.modified = True
        return super().get(request, *args, **kwargs)


class PalavraChaveUpdateView(UpdateView):
    model = Palavrachave
    form_class = PalavraChaveForm
    template_name = "palavras_chave/palavra_chave_form.html"

    def form_valid(self, form):
        messages.success(self.request, "Palavra-chave atualizada com sucesso.")
        return super().form_valid(form)

    def get_success_url(self):
        id_cliente = self.object.id_cliente.id_cliente  # pega o cliente da instância
        return reverse_lazy("palavras_chave:categoria_list", kwargs={"id_cliente": id_cliente})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        palavra = self.object
        cliente = palavra.id_cliente
        categoria = palavra.id_categoria
        context["cliente_selecionado"] = cliente
        context["categoria"] = categoria
        return context

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        cliente = self.object.id_cliente
        request.session["cliente_selecionado"] = {
            "id_cliente": cliente.id_cliente
        }
        request.session.modified = True
        return super().get(request, *args, **kwargs)

class PalavraChaveDeleteView(DeleteView):
    model = Palavrachave
    template_name = "palavras_chave/palavra_chave_delete.html"

    def get_success_url(self):
        id_cliente = self.object.id_cliente.id_cliente
        return reverse("palavras_chave:categoria_list", kwargs={"id_cliente": self.object.id_cliente_id})

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Palavra-chave excluída com sucesso.")
        return super().delete(request, *args, **kwargs)