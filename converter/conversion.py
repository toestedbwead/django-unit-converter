# each units value in meters

LENGTH_TO_METERS = {
    'millimeter': 0.001,
    'centimeter': 0.01,
    'meter': 1.0,
    'kilometer': 1000.0,
    'inch': 0.0254,
    'foot': 0.3048,
    'yard': 0.9144,
    'mile': 1609.34
}

def convert_length(value, from_unit, to_unit):
    """Convert a length value from one unit to another."""

    # converting input to meters
    value_in_meters = value * LENGTH_TO_METERS[from_unit]

    # converting meters to target unit
    result = value_in_meters / LENGTH_TO_METERS[to_unit]
    return result

WEIGHT_TO_GRAMS = {
    'milligram': 0.001,
    'gram': 1.0,
    'kilogram': 1000,
    'ounce': 28.3495,
    'pound': 453.592,
}

def convert_weight(value, from_unit, to_unit):
    """Convert a weight value from one unit to another."""

    # convert input to grams
    value_in_grams = value * WEIGHT_TO_GRAMS[from_unit]

    # convert grams to target unit
    result = value_in_grams / WEIGHT_TO_GRAMS[to_unit]
    return result

def convert_temperature(value, from_unit, to_unit):
    """Convert a temperature value from one unit to another."""

    if from_unit == 'celsius':
        celsius = value
    elif from_unit == 'fahrenheit':
        celsius = (value - 32) * 5/9
    elif from_unit == 'kelvin':
        celsius = value - 273.15

    if to_unit == 'celsius':
        return celsius
    elif to_unit == 'fahrenheit':
        return (celsius * 9/5) + 32
    elif to_unit == 'kelvin':
        return celsius + 273.15