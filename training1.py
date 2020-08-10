print("Hello welcome to newbie calculator app.")
print("")

import time
time = time.asctime()
print(time)

print("Please fill this field below before your start.")
name = input("Name : ")
print("")

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y


while True:
    print("Hello " + name + ",")
    print("1. [+] Addition, 2. [-] Subtraction, 3. [*] Multiply, 4. [/] Divide")
    print("Please select the calculation you need.")
    choice = input("Enter : ")
    print("")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter the first number : "))
        num2 = float(input("Enter the second number : "))

        if choice == '1':
            print("Result : ", num1, "+", num2, "=", add(num1, num2))
            print("Thank you  " + name + ", for using this application :)")
            print("")

        if choice == '2':
            print("Result : ", num1, "-", num2, "=", subtract(num1, num2))
            print("Thank you  " + name + ", for using this application :)")
            print("")

        if choice == '3':
            print("Result : ", num1, "*", num2, "=", multiply(num1, num2))
            print("Thank you  " + name + ", for using this application :)")
            print("")

        if choice == '4':
            print("Result : ", num1, "/", num2, "=", divide(num1, num2))
            print("Thank you  " + name + ", for using this application :) ")
            print("")

    else:
        print("Invalid input, please try again.")
        print("")
