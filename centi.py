# CSC 104 LAB 7 

# Program that turns centimeters to inches
while 1 < 2:
    cm = float(input("Enter value in centimeters: "))
    inch = cm * 2.54

    err_msg = ("[!] Error: Value can not be less than 1\n")

    if cm < 1:
        print(err_msg)
    else: 
        print(f'{cm}cm = {inch}inches')
        break