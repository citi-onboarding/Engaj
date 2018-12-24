from django.shortcuts import render
from django.views.generic import TemplateView 
from templated_email import send_templated_mail
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, resolve

from core.models import *
import os

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["servicos"] = Servico.objects.all()

        context["sobre"] = Sobre.objects.last()
        context["banner"] = Banner.objects.last()
        context["valores"] = Valor.objects.all()
        context["contato"] = Contato.objects.last()
        
        return context


def send_email(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        servico = request.POST.get('servico')
        message = request.POST.get('message')
        forma_contato = request.POST.get('forma-contato')
        telefone = request.POST.get('telefone')

        send_templated_mail(
            template_name='email',
            from_email='email',
            recipient_list=['engaj.site@gmail.com',os.environ['EMAIL_RECIPIENT_ACCOUNT']],
            context={
                'nome':name,
                'email':email,
                'servico':servico,
                'mensagem':message,
                'forma_contato':forma_contato,
                'telefone': telefone
            }
        )

        return HttpResponseRedirect('/')

    return render(request,'core/index.html',{})
