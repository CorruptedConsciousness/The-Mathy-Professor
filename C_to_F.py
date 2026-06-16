# Converts degrees Celsius to degrees Farenheit.

def celsius_fahrenheit(c_temp):
    f_temp = (c_temp * (9 / 5)) + 32
    return f_temp

# Asks user for Celsius input, performs conversion, 
# and returns the result.

int_c = float(input("Enter Celsisus Temp: "))
result = celsius_fahrenheit(int_c)
print(f"{int_c}° C converts to {result:.1f}° F.")





    
