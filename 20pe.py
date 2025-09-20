def  fcth():
    numbers = []
    for number in range(1,7):
        numb = float(input(f"{number} enter number: "))
        numbers.append(numb)
    average = sum(numbers) / len(numbers)
    print("The average of your chosen numbers is: ", average)

