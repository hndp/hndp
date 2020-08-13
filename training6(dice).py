import random
min = 1
max = 6

rolldice = input("Roll the dice? : ")
while rolldice == "yes":
    print("The result are : ")
    print(random.randint(min, max))
    print(random.randint(min, max))
    break


