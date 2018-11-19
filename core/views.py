from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class SassTestView(TemplateView):
    template_name = 'core/sass-test.html'
