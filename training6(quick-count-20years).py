print("")
print("Welcome to quickcountinvest")
print("Please input on how long investation you would like to count in 1 - 20 years.")
print("")

while True:
    choice = input("How many years of investment plan would you like to be count? : ")

    if choice in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
        if '1' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 1 year will be : ", (invst * 12))
            print("")
        elif '2' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 2 year will be : ", (invst * 24))
            print("")
        elif '3' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 3 year will be : ", (invst * 36))
            print("")
        elif '4' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 4 year will be : ", (invst * 48))
            print("")
        elif '5' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 5 year will be : ", (invst * 60))
            print("")
        elif '6' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 6 year will be : ", (invst * 72))
            print("")
        elif '7' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 7 year will be : ", (invst * 84))
            print("")
        elif '8' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 8 year will be : ", (invst * 96))
            print("")
        elif '9' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 9 year will be : ", (invst * 108))
            print("")

    if choice in ('10', '11', '12', '13', '14', '15', '16', '17', '18', '19'):

        if '10' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 10 year will be : ", (invst * 120))
            print("")
        elif '11' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 11 year will be : ", (invst * 132))
            print("")
        elif '12' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 12 year will be : ", (invst * 144))
            print("")
        elif '13' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 13 year will be : ", (invst * 156))
            print("")
        elif '14' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 14 year will be : ", (invst * 168))
            print("")
        elif '15' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 15 year will be : ", (invst * 180))
            print("")
        elif '16' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 16 year will be : ", (invst * 192))
            print("")
        elif '17' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 17 year will be : ", (invst * 204))
            print("")
        elif '18' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 18 year will be : ", (invst * 216))
            print("")
        elif '19' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 19 year will be : ", (invst * 228))
            print("")

    if choice in '20':

        if '20' in choice:
            invst = int(input("How much amount would you like to put monthly? : "))
            print("Your investment in 20 year will be : ", (invst * 240))
            print("")

    else:
        print("Please input in 1 to 20 years range.")
