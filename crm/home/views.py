from django.shortcuts import render
from django.views.generic.base import TemplateView, RedirectView


class HomePageView(TemplateView):
    template_name = 'home/index.html'
    
    
class HomePageRedirectView(RedirectView):
    permanent = True
    pattern_name = 'home'