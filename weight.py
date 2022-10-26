
while 1 < 2:
    kg = float(input("Enter weight in KG: "))
    if kg <= 0:
        print("Invalid Value! Value must be more than 0")
    else:
        pnd = kg * 2.205
        rnd_pnd = round(pnd, 1)
        print(f'{kg} in pounds is {rnd_pnd}')
        break

        