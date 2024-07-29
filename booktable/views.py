from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from .utils import send_acceptance_email, send_not_acceptance_email
import datetime


# Create your views here.
@api_view(['GET'])
def getBookings(request):
    bookingObjs = Booking.objects.all()  
    serializers = BookingSerializer(bookingObjs, many=True)
    return Response({"status":"200","payload": serializers.data})


@api_view(['POST'])
def Bookings(request):
    data = request.data
    
    serializers= BookingSerializer(data=data)
    
    if not serializers.is_valid():
        return Response({
            "status": 400,
            "message": serializers.errors
        })
    
    serializers.save()
    return Response({"status":"200", "payload": serializers.data})


@api_view(['POST'])
def acceptBooking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"status": 404, "message": "Booking not found."})

    booking.accept = True
    booking.save()

    # Send acceptance email
    send_acceptance_email(booking.name, booking.email, booking.date)

    return Response({"status": "200", "message": "Booking accepted and email sent."})


@api_view(['POST'])
def notacceptBooking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({"status": 404, "message": "Booking not found."})

    booking.accept = False
    booking.save()

    send_not_acceptance_email(booking.name, booking.email, booking.date)
    return Response({"status": "200", "message": "Booking accepted and email sent."})