# def temp_conversion():
#     userInput = input("Would you like to convert from Fahrenheit ('F') or Celsius ('C'): ")
#     if userInput.upper() == "F":
#         # use float rather than int to allow the user to enter decimal places
#         fahrenheit_temp_val = float(input("What is the temperature in Fahrenheit? "))
#         # formula to convert fahrenheit to celsius
#         celsius_temp_val = (fahrenheit_temp_val - 32) * 5.0 / 9.0
#         print(f"The temperature {fahrenheit_temp_val} in Fahrenheit is equivalent to {celsius_temp_val} in Celsius.")
#     elif userInput.upper() == "C":
#         celsius_temp_val = float(input("What is the temperature in Celsius? "))
#         # formula to convert celsius to fahrenheit
#         fahrenheit_temp_val = 9.0 / 5.0 * celsius_temp_val + 32
#         print(f"The temperature {celsius_temp_val} in Celsius is equivalent to {fahrenheit_temp_val} in Fahrenheit.")
#
#
# temp_conversion()
#
#
# def temp_convert(temp, scale):
#     if scale.upper() == "C":
#         fahrenheit_temp_val = 9.0 / 5.0 * temp + 32
#         return fahrenheit_temp_val
#     elif scale.upper() == "F":
#         celsius_temp_val = (temp - 32) * 5.0 / 9.0
#         return celsius_temp_val
#
#
# userScale = input("Would you like to convert from Fahrenheit (F) or Celsius (C): ")
# userTemp = float(input("What temperature would you like to convert: "))
# print(temp_convert(userTemp, userScale))
