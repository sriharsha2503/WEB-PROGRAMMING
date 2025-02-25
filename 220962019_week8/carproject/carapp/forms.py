# carapp/forms.py
from django import forms

class CarForm(forms.Form):
    # List of car manufacturers
    MANUFACTURERS = [
        ('toyota', 'Toyota'),
        ('honda', 'Honda'),
        ('ford', 'Ford'),
        ('bmw', 'BMW'),
        ('mercedes', 'Mercedes'),
    ]
    
    manufacturer = forms.ChoiceField(choices=MANUFACTURERS, label="Car Manufacturer")
    model_name = forms.CharField(max_length=100, label="Model Name")

