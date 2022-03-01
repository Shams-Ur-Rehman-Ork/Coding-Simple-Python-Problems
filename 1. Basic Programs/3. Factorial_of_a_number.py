import math


# a
# a * (a - 1) * (a - 2) * (a - n)

# Method: 1 --> Brute Force solution by me (Also called iterator approach)

def factorial(value):
    if value < 0:
        return None
    result = 1
    while value != 0:
        result *= value
        value -= 1
    return result


number = int(input("Enter a number: "))
print("The factorial of {0} is {1}".format(number, factorial(number)))


# Method: 2 --> Recursive approach to find factorial
def factorial(num):
    if num < 0:
        return None
    return 1 if num == 0 or num == 1 else num * factorial(num - 1)


number = int(input("Enter a number: "))
print(f"The factorial of number ({number}) is {factorial(number)}")


# Method: 3 --> Using built-in method
def factorial(num):
    try:
        return math.factorial(num)
    except ValueError:
        return None


number = int(input("Enter a number: "))
print(f"The Factorial value of number {number} is {factorial(number)}")
