from django.shortcuts import render
from django.views.generic import TemplateView 
from templated_email import send_templated_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, resolve

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


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        servico = request.POST.get('servico')
        message = request.POST.get('message')
        conhecer = request.POST.get('conhecer')

        send_templated_mail(
            template_name='email',
            from_email='email',
            recipient_list=['abcr@cin.ufpe.br', 'jrmmendes@outlook.com'],
            context={
                'nome':name,
                'email':email,
                'servico':servico,
                'mensagem':message,
                'conhecer':conhecer
            }
        )

        return HttpResponseRedirect('/')
    
    return render(request,'core/index.html',{})