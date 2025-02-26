from django.db import models

class Airplane(models.Model):
    tail_number = models.CharField(max_length=10, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.IntegerField()
    production_year = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.model} ({self.tail_number})"

class Flight(models.Model):
    flight_number = models.CharField(max_length=10, unique=True)
    departure = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    airplane = models.ForeignKey(Airplane, on_delete=models.CASCADE, related_name="flights")

    def __str__(self):
        return f"{self.flight_number} ({self.departure} -> {self.destination})"

class Reservation(models.Model):
    passenger_name = models.CharField(max_length=100)
    passenger_email = models.EmailField()
    reservation_code = models.CharField(max_length=10, unique=True, editable=False)
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE, related_name="reservations")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.reservation_code:
            import uuid
            self.reservation_code = str(uuid.uuid4())[:8].upper()  # 8 karakterlik benzersiz kod
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.passenger_name} - {self.reservation_code}"

