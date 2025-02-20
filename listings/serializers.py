

from rest_framework import serializers
from .models import *

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model=Property
        fields='__all__'

# :: PRODUCT SERIALIZER
class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Listing
        fields='__all__'
        
# :: CART SERIALIZER
class UserListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserListing
        fields='__all__'

# :: CART PRODUCT SERIALIZER
class SingleListingSerializer(serializers.ModelSerializer):
    class Meta:
        model=SingleListing
        fields='__all__'

# :: ORDER SERIALIZER
class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields='__all__'

# :: CHECKOUT SERIALIZER
class CheckoutSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        exclude=['userlisting','amount','order_status','subtotal','payment_complete','ref']
 