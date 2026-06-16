# Gather coordinates points.

x_1 = int(input("Enter first x-coordinate: "))
y_1 = int(input("Enter first y-coordinate: "))
x_2 = int(input("Enter second x-coordinate: "))
y_2 = int(input("Enter second y-coordinate:)"))

# Calculate the rise & run.

rise = y_2 - y_1
run = x_2 - x_1

# Check for division by zero then calculate and return slope.

if run == 0:
    print("Vertical Line/Slope Undefined")
else:
    m = rise / run
    print("The line has a slope of " + str(m))


