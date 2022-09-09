from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView

from restapp.methods import *
from .serializers import RestaurantProfileSerializer,LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest import settings
import jwt
class RestaurantProfileView(APIView):
    serializer_class = RestaurantProfileSerializer

    def post(self, request):
        try:
            serializer = RestaurantProfileSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            data = {
                'id': serializer.data['id'],
                'name': serializer.data['name'],
                'number_of_tables': serializer.data['number_of_tables'],
                'phone': serializer.data['phone'],
                'address': serializer.data['address'],
                'gstn': serializer.data['gstn'],
                'pan': serializer.data['pan'],
                'instagram': serializer.data['instagram'],
                'facebook': serializer.data['facebook'],
                'website': serializer.data['website'],
                'email': serializer.data['email'],

            }
            return Response(data, status=status.HTTP_201_CREATED)

        except Exception as error:
            data = {
                'message': str(error)
            }
            return Response(data, status=status.HTTP_400_BAD_REQUEST)


    # def get(self, request):
    #     token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    #     restaurant = GetRestaurant(token)
    #     dataDict = {}
    #     dataDict['is']

class LoginAPIView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            userid = serializer.data['userid']
            password = serializer.data['password']

            restaurant = GetRestaurantPhone(userid, password)
            if not restaurant:
                return Response({'message': 'User with given credentials not found'}, status=status.HTTP_404_NOT_FOUND)
            payload = {
                'email': userid,
                'date':str(datetime.now())
            }
            accessToken = jwt.encode(payload, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithm='HS256')
            return Response({'access_token':accessToken}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({'data':str(err)}, status=status.HTTP_400_BAD_REQUEST)



    