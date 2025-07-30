from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from core.models import CoreModel
from core.forms import RegisterCoreForm
from django.views.generic.edit import CreateView
from django.contrib.auth import logout

class HomeListView(ListView):
    model = CoreModel
    template_name = 'core/home.html'
    context_object_name = 'core'

class HomeLoginView(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

class HomeRegisterView(CreateView):
    form_class = RegisterCoreForm
    template_name = 'auth/register.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        return super().form_invalid(form)

def logout_view(request):
    logout(request)
    return redirect('home')
    
