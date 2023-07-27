from django.urls import include, path
from .views import HomePageView, HomePageRedirectView

urlpatterns = [
    path("", HomePageRedirectView.as_view()),
    path("home/", HomePageView.as_view(), name="home"),
]
