from django.urls import path, include

urlpatterns = [
    path('', include('internal_api.orders_api.urls')),
    # path('', include('internal_api.clients_api.urls')),
    path('', include('internal_api.addresses_api.urls')),
    path('', include('internal_api.employees_api.urls')),
    path('', include('internal_api.companies_api.urls')),
    path('', include('internal_api.reports_api.urls')),
    path('', include('internal_api.users_api.urls')),
]
