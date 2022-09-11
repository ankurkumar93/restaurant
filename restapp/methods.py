from .models import *
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed, NotFound
import jwt
from rest import settings
from django.contrib.auth.hashers import check_password


def GetRestaurant(token):
    if len(token) == 0:
        raise NotAuthenticated
    try:
        tokenData = jwt.Decode(token, settings.JWT_AUTH['JWT_SECRET_KEY'], algorithms=['HS256'])
        restaurantid = tokenData['id']
    except:
        raise AuthenticationFailed
    try:
        restaurant = RestaurantProfile.objects.get(id=restaurantid)
        return restaurant
    except:
        raise NotFound
    
# def CheckPassword(userid, password):
#     print("sasasasasasasa", userid)
#     userpassword = RestaurantProfile.objects.get(p)
#     return True


def GetRestaurantByUserId(userid, password=None):
    if not password:
        try:
            if '@' not in userid:
                restaurant = RestaurantProfile.objects.get(phone=userid)
                return restaurant
            else:
                restaurant = RestaurantProfile.objects.get(email=userid)
                return restaurant
        except:
            return None
    try:
        if '@' not in userid:
            print("sasasas", userid)
            restaurant = RestaurantProfile.objects.get(phone=userid)
            if check_password(password, restaurant.__dict__['password']):
                return restaurant
            else:
                return None
        else:
            restaurant = RestaurantProfile.objects.get(email=userid)
            if check_password(password, restaurant.__dict__['password']):
                return restaurant
            else:
                return None
    except:
        return None
    
