fahrenheit_temps = [32, 68, 77, 104, 122]

print("Temperatures in Fahrenheit:", fahrenheit_temps)
celsius_temps = [(temp - 32) * 5 / 9 for temp in fahrenheit_temps]
print("Equivalent temperatures in Celsius:", celsius_temps)

