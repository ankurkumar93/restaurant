from .models import *
from rest_framework.exceptions import NotAuthenticated, AuthenticationFailed, NotFound
import jwt
from rest import settings


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