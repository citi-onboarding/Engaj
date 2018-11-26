from django.shortcuts import render
from django.views.generic import TemplateView 
from core.models import *

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all()
        
        context["sobre"] = Sobre.objects.last()
        context["valores"] = Valor.objects.all()
        
        return context