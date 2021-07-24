from django import forms
from .models import Order


class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [ 'home_number','street','area',
                  'postal_code', 'city','district']

