

temp = float(input("Enter Temperature in Celcius: "))

if temp < -273.15:
    print("Invalid Input! Temperature is below absolute Zero")
elif temp >= -275.15 and temp != 0:
    print("Temperature is below freezing") 
elif temp == 0:
    print("Temperature is at freezing point")
elif temp > 0 or temp < 100:
    print("Temperature is within normal range")
elif temp == 100:
    print("Temperature is at boiling point")
elif temp > 100:
    print("Temperature is above boiling point")