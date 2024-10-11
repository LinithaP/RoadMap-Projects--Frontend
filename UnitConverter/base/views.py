# converter/views.py
from django.shortcuts import render
from .forms import ConversionForm_length, ConversionForm_weight, ConversionForm_temp

def convert_length(request):
    result = None
    if request.method == 'POST':
        form = ConversionForm_length(request.POST)
        if form.is_valid():
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            value = form.cleaned_data['value']
            
            # Perform conversion
            result = length(value, from_unit, to_unit)
    else:
        form = ConversionForm_length()

    return render(request, 'base/length.html', {'form': form, 'result': result})

def length(value, from_unit, to_unit):
    # Define conversion factors
    conversions = {
        'mm': {'cm': 0.1, 'inch': 0.03937, 'm': 0.001},
        'cm': {'mm': 10, 'inch': 0.3937, 'm': 0.01},
        'inch': {'mm': 25.4, 'cm': 2.54, 'm': 0.0254},
        'm': {'mm': 1000, 'cm': 100, 'inch': 39.3701},
    }
    
    if from_unit == to_unit:
        return value
    
    return value * conversions[from_unit][to_unit]

def convert_weight(request):
    result = None
    if request.method == 'POST':
        form = ConversionForm_weight(request.POST)
        if form.is_valid():
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            value = form.cleaned_data['value']
            
            # Perform conversion
            result = weight(value, from_unit, to_unit)
    else:
        form = ConversionForm_weight()

    return render(request, 'base/weight.html', {'form': form, 'result': result})

def weight(value, from_unit, to_unit):
    # Define conversion factors
    conversions = {
        'mg': {'g': 0.001, 'kg': 0.000001, 'lb': 0.00000220462, 'oz': 0.000035274},
        'g': {'mg': 1000, 'kg': 0.001, 'lb': 0.00220462, 'oz': 0.035274},
        'kg': {'mg': 1000000, 'g': 1000, 'lb': 2.20462, 'oz': 35.274},
        'lb': {'mg': 453592, 'g': 453.592, 'kg': 0.453592, 'oz': 16},
        'oz': {'mg': 28349.5, 'g': 28.3495, 'kg': 0.0283495, 'lb': 0.0625},
    }
    
    if from_unit == to_unit:
        return value
    
    return value * conversions[from_unit][to_unit]

def convert_temp(request):
    result = None
    if request.method == 'POST':
        form = ConversionForm_temp(request.POST)
        if form.is_valid():
            from_unit = form.cleaned_data['from_unit']
            to_unit = form.cleaned_data['to_unit']
            value = form.cleaned_data['value']
            
            # Perform conversion
            result = temp(value, from_unit, to_unit)
    else:
        form = ConversionForm_temp()

    return render(request, 'base/temp.html', {'form': form, 'result': result})

def temp(value, from_unit, to_unit):
    # Define conversion factors
    conversions = {
    'C': {  # Celsius
        'F': lambda c: c * 9/5 + 32,  # Celsius to Fahrenheit
        'K': lambda c: c + 273.15      # Celsius to Kelvin
    },
    'F': {  # Fahrenheit
        'C': lambda f: (f - 32) * 5/9,  # Fahrenheit to Celsius
        'K': lambda f: (f - 32) * 5/9 + 273.15  # Fahrenheit to Kelvin
    },
    'K': {  # Kelvin
        'C': lambda k: k - 273.15,  # Kelvin to Celsius
        'F': lambda k: (k - 273.15) * 9/5 + 32  # Kelvin to Fahrenheit
    },
}
    
    if from_unit == to_unit:
        return value
    
    return value * conversions[from_unit][to_unit]

