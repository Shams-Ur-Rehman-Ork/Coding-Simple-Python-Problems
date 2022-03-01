# a and b
# if a > b return a else b
# if equal return both numbers are equal

# Method:1 --> Using hard coded values
value_1 = 30
value_2 = 90

if value_1 > value_2:
    print("The Maximum Value is: {}".format(value_1))
else:
    print("The Maximum Value is: {}".format(value_2))


# Method:2 --> Function that returns a maximum value
def maximum(value_1, value_2):
    if value_1 > value_2:
        return value_1
    elif value_2 > value_1:
        return value_2
    else:
        return None


first_value = int(input("Enter a number: "))
second_value = int(input("Enter a number: "))
result = maximum(first_value, second_value)
print(f"The Maximum number is {result}")

# Method: 3 --> Using built-in max function

value_1 = int(input("Enter a number: "))
value_2 = int(input("Enter a number: "))

maximum_number = max(value_1, value_2)
print(f"The maximum value is {maximum_number}")

# Method: 4 --> Using Ternary Operator

integer_1 = int(input("Enter a number: "))
integer_2 = int(input("Enter a number: "))

print("Maximum value is -->", integer_1 if integer_1 >= integer_2 else integer_2)
