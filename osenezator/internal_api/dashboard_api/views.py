from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import status

class DashboardAPIView(APIView):
    def get(self, request, format=None):
        username = request.GET.get('username')
        user = get_object_or_404(User, username=username)
        # if user.is_superuser:
        #     context_data= {
        #         'last_year':"f", 
        #     }
        #     return Response(context_data, status=status.HTTP_200_OK)
        # else:
        #     context_data= {
        #         'profit_last_year':,
        #         'profit_now_year': ,
        #         'profit_orders':
        #         ''
        #     }
        return Response(user.username, status=status.HTTP_200_OK)