print("")
print("Welcome to quickcountinvest")
print("Please input on how long investation you would like to count in 1 - 20 years.")
print("")

while True:
    choice = input("How many years of investment plan would you like to be count? : ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if '1' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 1 year will be : ", ":", (invst * 12))
        elif '2' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 2 year will be : ", ":", (invst * 24))
        elif '3' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 3 year will be : ", ":", (invst * 36))
        elif '4' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 4 year will be : ", ":", (invst * 48))
        elif '5' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 5 year will be : ", ":", (invst * 60))
        elif '6' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 6 year will be : ", ":", (invst * 72))
        elif '7' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 7 year will be : ", ":", (invst * 84))
        elif '8' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 8 year will be : ", ":", (invst * 96))
        elif '9' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 9 year will be : ", ":", (invst * 108))

    if choice in ('10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):

        if '10' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 10 year will be : ", ":", (invst * 120))
        elif '11' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 11 year will be : ", ":", (invst * 132))
        elif '12' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 12 year will be : ", ":", (invst * 144))
        elif '13' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 13 year will be : ", ":", (invst * 156))
        elif '14' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 14 year will be : ", ":", (invst * 168))
        elif '15' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 15 year will be : ", ":", (invst * 180))
        elif '16' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 16 year will be : ", ":", (invst * 192))
        elif '17' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 17 year will be : ", ":", (invst * 204))
        elif '18' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 18 year will be : ", ":", (invst * 216))
        elif '19' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 19 year will be : ", ":", (invst * 228))

    if choice in '20':

        if '20' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 20 year will be : ", ":", (invst * 240))

    else:
        print("Please input in 1 to 20 years range.")
