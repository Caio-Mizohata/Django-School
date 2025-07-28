from django.shortcuts import render, redirect
from django.views.generic import ListView
from core.models import CoreModel

class HomeListView(ListView):
    model = CoreModel
    template_name = 'core/home.html'
    context_object_name = 'core'

class AboutListView(ListView):
    model = CoreModel
    template_name = 'core/about.html'
    context_object_name = 'core'

class ContactListView(ListView):
    model = CoreModel
    template_name = 'core/contact.html'
    context_object_name = 'core'
