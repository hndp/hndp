name = input("Please enter your name : ")
id = input("Please enter your student id number : ")
print("")

print("Hello, " + name)
print(id)
print("")

print("Please answer this multiple choice question")
print("Answer the following question with a / b / c / d.")

print("Who is the president of Indonesia in 2020?")
print("a. Soeharto")
print("b. Moeldoko")
print("c. Gusdur")
print("d. Joko Widodo")

q1 = input("Enter : ")
if "a" in q1:
    print("Incorrect")
if "b" in q1:
    print("Incorrect")
if "c" in q1:
    print("Incorrect")
if "d" in q1:
    print("correct")

print("What is the capital city of Indonesia?")
print("a. Jakarta")
print("b. Ho Chi Minh")
print("c. Bandung")
print("d. Semarang")

q2 = input("Enter : ")
if "a" in q2:
    print("correct")
if "b" in q2:
    print("Incorrect")
if "c" in q2:
    print("Incorrect")
if "d" in q2:
    print("Incorrect")