from rest_framework import serializers
from .models import Message,Ride

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        exclude = ('time_sent')

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        field = '__all__'