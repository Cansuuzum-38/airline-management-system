from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.utils.timezone import now
from django.utils.timezone import make_aware
from datetime import datetime
from .models import Airplane, Flight, Reservation
from .serializers import AirplaneSerializer, FlightSerializer, ReservationSerializer

class AirplaneViewSet(viewsets.ModelViewSet):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        """
        Yeni bir rezervasyon eklerken kapasite kontrolü yapar.
        """
        flight_id = request.data.get("flight")

        try:
            flight = Flight.objects.get(id=flight_id)
        except Flight.DoesNotExist:
            return Response({"error": "Böyle bir uçuş bulunamadı!"}, status=status.HTTP_400_BAD_REQUEST)

        # 🔹 O uçuş için yapılan toplam rezervasyonları say
        total_reservations = Reservation.objects.filter(flight=flight).count()

        # 🔹 Eğer rezervasyon sayısı uçak kapasitesine ulaşmışsa hata döndür
        if total_reservations >= flight.airplane.capacity:
            return Response({"error": "Uçuş kapasitesi dolu!"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        """
        Rezervasyon yapılırken uçuş kapasitesini kontrol eder.
        """
        flight_id = request.data.get("flight")
        flight = Flight.objects.get(id=flight_id)

        if flight.reservations.count() >= flight.airplane.capacity:
            return Response({"error": "Uçuş kapasitesi dolu!"}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

