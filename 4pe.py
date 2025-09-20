# بازی اعداد0 تا 100

import random

number = random.randint(1, 100)
print("please enter a number in 1 to 100.")

while True:
    x = int(input("enter a number: "))

    if x < number:
        print("adad shoma koochak ast.")

    elif x > number:
        print("adad shoma bozorg  ast.")

    else:
        print("affarin!")
        break


# python .\4pe.py
