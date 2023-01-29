from django.views.generic import TemplateView

from companies.models import Company

class HomePageView(TemplateView):
    template_name = "home/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['book_list'] = Company.objects.count()
        return context