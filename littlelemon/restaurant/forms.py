from django.forms import ModelForm
from .models import Booking
from django import forms
# Code added for loading form data on the Booking page
class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = "__all__"
        widgets = {
            'reservation_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
            'reservation_time': forms.TimeInput(attrs={'type': 'time'}, format='%H:%M')
        }
        input_formats = {
            'reservation_date': ['%Y-%m-%d'],  # Date format
            'reservation_time': ['%H:%M']  # Time format (24-hour)
        }