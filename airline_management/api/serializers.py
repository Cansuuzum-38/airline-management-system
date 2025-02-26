from rest_framework import serializers
from .models import Airplane, Flight, Reservation

class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = '__all__'

class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['id', 'passenger_name', 'passenger_email', 'flight', 'status', 'reservation_code', 'created_at']
        read_only_fields = ['reservation_code', 'created_at']


