def farenheit_celcius(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

result = farenheit_celcius(98.6)
print(f"98.6 F converts to {result} C.")
