from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import login
from .forms import CreationForm


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('admin')
    template_name = "users/signup.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("home")
