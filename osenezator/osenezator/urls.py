"""osenezator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path as url
from django.conf import settings
from rest_framework import routers
from drivers.views import DriverViewSet 
from orders.views import OrderViewSet
from addresses.views import AddressAutocomplete 
from drivers.views import DriverAutocomplete
from django.views.static import serve as mediaserve
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'driver', DriverViewSet, basename='driver')
router.register(r'order', OrderViewSet, basename='order')


urlpatterns = [
    path('about/', include('about.urls')),
    path('auth/', include('users.urls')),
        
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('address-autocomplete/', AddressAutocomplete.as_view(),name='address-autocomplete'),
    path('driver-autocomplete/', DriverAutocomplete.as_view(),name='driver-autocomplete'),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        url(f'^{settings.MEDIA_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.MEDIA_ROOT}),
        url(f'^{settings.STATIC_URL.lstrip("/")}(?P<path>.*)$',
            mediaserve, {'document_root': settings.STATIC_ROOT}),
    ]