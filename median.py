import math

def median(numbers):
    length = len(numbers)
    midpoint = math.floor(length / 2)
    return (length == 1 and numbers[0]) or (length % 2 == 0 and (numbers[midpoint - 1] + numbers[midpoint]) / 2) or numbers[midpoint]

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break
print(median(numbers))
