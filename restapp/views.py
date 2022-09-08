from django.shortcuts import render
from rest_framework.views import APIView

from restapp.methods import GetRestaurant
from .serializers import RestaurantProfileSerializer
from rest_framework import status
from rest_framework.response import Response

class RestaurantProfileView(APIView):
    serializer_class = RestaurantProfileSerializer

    def post(self, request):
        try:
            serializer = RestaurantProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = {
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)

        except:
            data = {
                'message': 'Failed'
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        restaurant = GetRestaurant(token)
        dataDict = {}
        dataDict['is']

    