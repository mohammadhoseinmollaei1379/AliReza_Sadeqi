def numbers():
    numbers = []
    for number in range(1,7):
        numb = float(input(f"{number} enter number: "))
        numbers.append(numb)

    average = sum(numbers) / len(numbers)
    return average

print(numbers())