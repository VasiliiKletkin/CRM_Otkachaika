from django.urls import path

from . import views

urlpatterns = [
    path('', views.AboutAuthorView.as_view(), name='about'),
]