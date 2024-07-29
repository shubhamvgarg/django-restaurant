# utils.py

from django.core.mail import send_mail
from django.conf import settings

def send_acceptance_email(name, email, date):
    subject = 'Booking Accepted'
    message = f"Dear {name},\n\nYour booking for {date} has been accepted. We look forward to seeing you!\n\nBest Regards,\nYour Company"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])

def send_not_acceptance_email(name, email, date):
    subject = 'Booking Cannot be Accept'
    message = f"Dear {name},\n\nYour booking for {date} has been rejected. We look forward to seeing you some other time!\n\nBest Regards,\nYour Company"
    from_email = settings.EMAIL_HOST_USER
    send_mail(subject, message, from_email, [email])
