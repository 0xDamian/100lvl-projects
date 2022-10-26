
count = 5
while 1 < 2:
    usrnm = input("Username: ")
    passwd = input("Password: ")
    set_passwd = "admin"
    if passwd == set_passwd:
        print(f'Welcome {usrnm}! You are logged in')
        break
    else:
        if count > 0:
            print(f'Incorrect Password! You have {count} tries')
            count -= 1
        else:
            print("Too many attempts! You have been booted off the system")
            break
