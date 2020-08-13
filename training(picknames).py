import random

names = ['Roger', 'Daniel', 'Catherine', 'Alex', 'Ricky']
choice = input("Type roll to randomly pick one of those names : ")
while "roll" in choice:
    print("The selected name is : ")
    print(random.choice(names))
    break