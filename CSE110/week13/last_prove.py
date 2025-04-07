#clesius to fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

#wind chill
def calculate_wind_chill(temp_f, wind_speed):
    return 35.74 + (0.6215 * temp_f) - (35.75 * (wind_speed ** 0.16)) + (0.4275 * temp_f * (wind_speed ** 0.16))

#user input 
temp = float(input("What is the temperature? "))
unit = input("Fahrenheit or Celsius (F/C)? ").strip().upper()


if unit == "C":
    temp_f = celsius_to_fahrenheit(temp)
else:
    temp_f = temp

print()

for wind_speed in range(5, 65, 5):
    wind_chill = calculate_wind_chill(temp_f, wind_speed)
    print(f"At temperature {temp_f:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")
