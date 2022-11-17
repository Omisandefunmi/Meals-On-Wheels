from django.shortcuts import render

from rest_framework.views import APIView
from .tasks import ScrapRestaurants
from rest_framework import status
from rest_framework.response import Response
# Create your views here.


class ChickenRepublicApi(APIView):
    def get(self, request):
        scrapped = ScrapRestaurants.chicken_republic()
        return Response(
            {
                "details": scrapped
            }, status=status.HTTP_200_OK
            )
