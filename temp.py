
# code to convert temperature from C to F or vice-versa

temp = input("Unit of result: ") # convert to celcius
if temp == "C": # upper case
    f = float(input("Temperature in Fahrenheit: "))
    c = 5/9 * (f - 32)
    rnd = round(c, 2) # round float to 2 dp cause why not
    print(f'{f}F in Celcius is {rnd}{temp}')
elif temp == "F": # upper case, obviously
    c = float(input("Temperature in Celcius: ")) # convert to Fahrenheit
    f = 9/5*c + 32
    rnd = round(f, 2) # round float to 2 dp cause why not
    print(f'{c}C in Fahrenheit is {rnd}{temp}')