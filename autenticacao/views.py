from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.utils.timezone import now, timedelta
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView
from .forms import EditarPerfilForm, UsuarioForm


class CustomLoginView(LoginView):
    template_name = 'autenticacao/login.html'
    success_url = reverse_lazy('perfil')

@login_required
def perfil(request):
    return render(request, 'autenticacao/perfil.html')

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('perfil')
    else:
        form = EditarPerfilForm(instance=request.user)

    return render(request, 'autenticacao/editar_perfil.html', {'form': form})

class UsuarioListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'usuarios/usuario_list.html'
    context_object_name = 'usuarios'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tempo_limite'] = now() - timedelta(minutes=5)
        return context

from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import UsuarioForm

class UsuarioCreateView(CreateView):
    model = User
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioUpdateView(UpdateView):
    model = User
    form_class = UsuarioForm
    template_name = 'usuarios/usuario_form.html'
    success_url = reverse_lazy('usuario_list')

class UsuarioDeleteView(DeleteView):
    model = User
    template_name = 'usuarios/usuario_delete.html'
    success_url = reverse_lazy('usuario_list')
