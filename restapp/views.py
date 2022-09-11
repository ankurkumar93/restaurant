from datetime import datetime
from django.shortcuts import render
from rest_framework.views import APIView

from restapp.methods import *
from .serializers import RestaurantProfileSerializer,LoginSerializer
from rest_framework import status
from rest_framework.response import Response
from rest import settings
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

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

    def get(self, request):
        userid = request.GET.get('userid')
        restaurant = GetRestaurantByUserId(userid)
        if not restaurant:
            return Response({'message': 'User with given id not found'}, status=status.HTTP_404_NOT_FOUND)
        restaurantdata = {
            'id': restaurant.id,
            'name': restaurant.name,
            'number_of_tables': restaurant.number_of_tables,
            'address': restaurant.address,
            'gstn': restaurant.gstn,
            'pan': restaurant.pan,
            'instagram': restaurant.instagram,
            'facebook': restaurant.facebook,
            'website': restaurant.website,
            'email': restaurant.email,
        }
        return Response(restaurantdata, status=status.HTTP_200_OK)

class LoginAPIView(APIView):
    def post(self, request):
        try:
            serializer = LoginSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            userid = serializer.data['userid']
            password = serializer.data['password']

            restaurant = GetRestaurantByUserId(userid, password)
            if not restaurant:
                return Response({'message': 'User with given credentials not found'}, status=status.HTTP_404_NOT_FOUND)
            accessToken = AccessToken.for_user(request.user)
            accessToken['userid'] = userid
            

            return Response({'access_token':str(accessToken), 'userid':userid}, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({'data':str(err)}, status=status.HTTP_400_BAD_REQUEST)

    
class CustomerView(APIView):
    
    def post(self, request):
        try:
            accessToken = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            tokenData = AccessToken(accessToken)
        except:
            return Response({'message':'Token is invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)

        restaurantObject = GetRestaurantByUserId(tokenData['userid'])
        customerPhone = request.data['customerPhone']
        customerName = request.data['customerName']
        customerInstance = Customer.objects.create(name=customerName, phone=customerPhone)
        customerInstance.restaurant.add(restaurantObject)
        data = {
            'customerName' : customerName,
            'customerPhone' : customerPhone,

        }
        return Response({'data': data}, status=status.HTTP_201_CREATED)

    def get(self,request):
        phone = request.GET.get('phone')
        try:
            accessToken = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
            tokenData = AccessToken(accessToken)
        except:
            return Response({'message':'Token is invalid or expired'}, status=status.HTTP_401_UNAUTHORIZED)
        restaurantObject = GetRestaurantByUserId(tokenData['userid'])
        customerObject = Customer.objects.filter(restaurant=restaurantObject, phone=phone).first()
        if customerObject is not None:
            customerdata = {
                'customerName': customerObject.name,
                'customerPhone': customerObject.phone,

            }
            return Response({'data': customerdata}, status=status.HTTP_200_OK)
        else:
            return Response({'data': []}, status=status.HTTP_200_OK)