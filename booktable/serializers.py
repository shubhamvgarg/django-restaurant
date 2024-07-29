from rest_framework import serializers
from datetime import datetime, date, time
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

    def validate(self, data):
        booking_date = data.get('date')
        booking_time = data.get('time')

        if not booking_date or not booking_time:
            raise serializers.ValidationError({"error": "Date and time must be provided."})

        if isinstance(booking_date, str):
            try:
                booking_date = datetime.strptime(booking_date, '%Y-%m-%d').date()
            except ValueError:
                raise serializers.ValidationError({"error": "Invalid date format."})

        if isinstance(booking_time, str):
            try:
                booking_time = datetime.strptime(booking_time, '%H:%M:%S').time()
            except ValueError:
                raise serializers.ValidationError({"error": "Invalid time format."})

        booking_datetime = datetime.combine(booking_date, booking_time)

        now = datetime.now()

        if booking_date < date.today():
            raise serializers.ValidationError({"error": "You cannot book for previous dates."})

        if booking_datetime < now:
            raise serializers.ValidationError({"error": "Time must be greater than or equal to the current time."})

        return data
