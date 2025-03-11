import streamlit as st

# App set up
st.set_page_config(page_title="Unit Converter", layout="wide")
st.title("Unit Converter")
st.write("Convert your units with ease")

# Categories dropdown
category = st.selectbox("Choose a category:", ("Select", "Length", "Weight", "Temperature", "Time", "Volume"))

if category != "Select":
    st.write(f"You selected {category} category.")

# All units for Length, Weight, Temperature, Time, Volume
length_units = {
    "Kilometre": 1000,
    "Metre": 1,
    "Centimetre": 0.01,
    "Millimetre": 0.001,
    "Micrometre": 0.000001,
    "Nanometre": 0.000000001,
    "Mile": 1609.344,
    "Yard": 0.9144,
    "Foot": 0.3048,
    "Inch": 0.0254,
    "Nautical mile": 1852
}

weight_units = {
    "Gram": 1,
    "Kilogram": 1000,
    "Milligram": 0.001,
    "Metric Ton": 1000000,
    "Ounce": 28.3495,
    "Pound": 453.592,
    "Short Ton (US)": 907184.74,
    "Long Ton (UK)": 1016046.9088
}

temperature_units = {
    "Celsius": lambda x: x,
    "Fahrenheit": lambda x: x * 9 / 5 + 32,
    "Kelvin": lambda x: x + 273.15
}

time_units = {
    "Second": 1,
    "Minute": 60,
    "Hour": 3600,
    "Day": 86400,
    "Week": 604800,
    "Month": 2592000,  # Approximation
    "Year": 31536000  # Approximation
}

volume_units = {
    "Cubic Meter": 1,
    "Liter": 0.001,
    "Milliliter": 0.000001,
    "Cubic Centimeter": 0.000001,
    "Cubic Inch": 0.000016387064,
    "Cubic Foot": 0.0283168,
    "Gallon (US)": 0.00378541,
    "Quart (US)": 0.000946353,
    "Pint (US)": 0.000473176,
    "Ounce (US)": 0.0000295735
}

# Conversion Functions
def convert_length(value, from_unit, to_unit):
    value_in_meters = value * length_units[from_unit]
    converted_value = value_in_meters / length_units[to_unit]
    return converted_value

def convert_weight(value, from_unit, to_unit):
    value_in_grams = value * weight_units[from_unit]
    converted_value = value_in_grams / weight_units[to_unit]
    return converted_value

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return value * 9 / 5 + 32
    elif from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    elif from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5 / 9
    elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
        return (value - 273.15) * 9 / 5 + 32
    else:
        return value  # same unit conversion

def convert_time(value, from_unit, to_unit):
    value_in_seconds = value * time_units[from_unit]
    converted_value = value_in_seconds / time_units[to_unit]
    return converted_value

def convert_volume(value, from_unit, to_unit):
    value_in_cubic_meters = value * volume_units[from_unit]
    converted_value = value_in_cubic_meters / volume_units[to_unit]
    return converted_value

# Convert the units based on the selected category
if category == "Length":
    from_unit = st.selectbox("From Unit", list(length_units.keys()))
    to_unit = st.selectbox("To Unit", list(length_units.keys()))
    value = st.number_input("Value to Convert", min_value=0.0, value=1.0)

    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From Unit", list(weight_units.keys()))
    to_unit = st.selectbox("To Unit", list(weight_units.keys()))
    value = st.number_input("Value to Convert", min_value=0.0, value=1.0)

    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From Unit", list(temperature_units.keys()))
    to_unit = st.selectbox("To Unit", list(temperature_units.keys()))
    value = st.number_input("Value to Convert", min_value=-273.15, value=0.0)

    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif category == "Time":
    from_unit = st.selectbox("From Unit", list(time_units.keys()))
    to_unit = st.selectbox("To Unit", list(time_units.keys()))
    value = st.number_input("Value to Convert", min_value=0.0, value=1.0)

    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")

elif category == "Volume":
    from_unit = st.selectbox("From Unit", list(volume_units.keys()))
    to_unit = st.selectbox("To Unit", list(volume_units.keys()))
    value = st.number_input("Value to Convert", min_value=0.0, value=1.0)

    if st.button("Convert"):
        result = convert_volume(value, from_unit, to_unit)
        st.write(f"{value} {from_unit} is equal to {result} {to_unit}")
