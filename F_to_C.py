# Converts degrees Farenheit to degrees Celsius. 

def fahrenheit_celsius(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

# Asks user for Fahrenehit input, performs conversion, 
# and returns the result.

int_f = float(input("Enter Fahrenheit Temp: "))
result = fahrenheit_celsius(int_f)
print(f"{int_f}° F converts to {result:.1f}° C.")

