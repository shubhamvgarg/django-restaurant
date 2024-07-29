from django.contrib import admin
from .models import Booking
from .utils import send_acceptance_email, send_not_acceptance_email
# Register your models here.

# admin.site.register(Booking)


class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'persons', 'date','time', 'accept')
    actions = ['accept_booking', 'not_accept_booking']

    def accept_booking(self, request, queryset):
        for booking in queryset:
            booking.accept = True
            booking.save()
            # Send acceptance email
            send_acceptance_email(booking.name, booking.email, booking.date)
        self.message_user(request, "Selected bookings have been accepted and emails sent.")
    accept_booking.short_description = "Accept selected bookings"

    def not_accept_booking(self, request, queryset):
        for booking in queryset:
            booking.accept = False
            booking.save()
            # Send acceptance email
            send_not_acceptance_email(booking.name, booking.email, booking.date)
        self.message_user(request, "Selected bookings has not been accepted and emails sent.")
    not_accept_booking.short_description = "Cannot Accept selected bookings"

admin.site.register(Booking,BookingAdmin)
