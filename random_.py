import random

open("New_text","a")
x = 1
number1 = 0
while x<21:
    number = random.randint(1,200)
    if number % 2 != 0:
        number1 = number + number1 
        with open("New_text", "a") as file:
            file.write((str(number))+"\n")
            x = x+1
with open("New_text") as file:
    print(file.read())
    print(number1)
    
