def celsius_en_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temperature_celsius = float(input("Entrez la température en degrés Celsius : "))
temperature_fahrenheit = celsius_en_fahrenheit(temperature_celsius)
print(f"{temperature_celsius}°C équivaut à {temperature_fahrenheit}°F.")
