#number = int(input("enter a number:"))
#numbers = [1,2,3,4,5,6,7,8,9,10]
#for i in numbers:
#    if i == number:
#        print('peyda shod')
#        break
#else:
#    print('peyda nashod')


print('well come to back to   calculator!')
calculater = input("amal mohasebati delkhah ra vared konid: ")
if calculater == "+":
    while True:
        x = float(input("enter a number:"))
        y = float(input("enter a number:"))
        xy = x + y
        print(xy)
        edame = str(input("mi khai edame bedi? "))
        if edame == "no":
            break
elif calculater == "*":
    while True:
        x = float(input("enter a number:"))
        y = float(input("enter a number:"))
        xy = x * y
        print(xy)
        edame = str(input("mi khai edame bedi? "))
        if edame == "no":
            break
elif calculater == "-":
    while True:
        x = float(input("enter a number:"))
        y = float(input("enter a number:"))
        xy = x - y
        print(xy)
        edame = str(input("mi khai edame bedi? "))
        if edame == "no":
            break
elif calculater == "/":
    while True:
        x = float(input("enter a number:"))
        y = float(input("enter a number:"))
        xy = x / y
        print(xy)
        edame = str(input("mi khai edame bedi? "))
        if edame == "no" and edame == "na":
            break
#def show_user_info(name, age):
#    print(f"Hello! My name is {name} and I am {age} years old.")
#
#
#show_user_info(age=25, name="Maryam")

