# converter/forms.py
from django import forms

class ConversionForm_length(forms.Form):
    units = [
        ('mm', 'Millimeters'),
        ('cm', 'Centimeters'),
        ('inch', 'Inches'),
        ('m', 'Meters'),
    ]
    
    from_unit = forms.ChoiceField(choices=units, label='From Unit')
    to_unit = forms.ChoiceField(choices=units, label='To Unit')
    value = forms.FloatField(label='Value to Convert')

class ConversionForm_weight(forms.Form):
    units = [
        ('mg', 'Milligrams'),
        ('g', 'Grams'),
        ('kg', 'Kilograms'),
        ('oz', 'Ounces'),
        ('lb', 'Pounds'),
    ]
    
    from_unit = forms.ChoiceField(choices=units, label='From Unit')
    to_unit = forms.ChoiceField(choices=units, label='To Unit')
    value = forms.FloatField(label='Value to Convert')

class ConversionForm_temp(forms.Form):
    units = [
    ('C', 'Celsius'),
    ('F', 'Fahrenheit'),
    ('K', 'Kelvin'),
]

    
    from_unit = forms.ChoiceField(choices=units, label='From Unit')
    to_unit = forms.ChoiceField(choices=units, label='To Unit')
    value = forms.FloatField(label='Value to Convert')
