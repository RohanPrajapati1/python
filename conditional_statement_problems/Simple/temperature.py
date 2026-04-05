# Take a temperature value and print “Cold”, “Warm”, or “Hot” using range conditions. 
temperature = float(input("Enter the temperature: "))

if temperature < 0:
    print("Cold")
elif temperature <= 25:
    print("Warm")
else:
    print("Hot")