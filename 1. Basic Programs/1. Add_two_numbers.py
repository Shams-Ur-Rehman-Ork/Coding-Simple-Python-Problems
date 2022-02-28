# Method:1 --> Using hard coded values
first_number = 10
second_number = 20

sum_value = first_number + second_number
print(f"The sum of two numbers is --> {sum_value}")
print("The sum of {0} and {1} is {2}".format(first_number, second_number, sum_value))

# Method:2 --> Getting input from User
first_value = int(input("Enter 1st number: "))
second_value = int(input("Enter 2nd number: "))

sum_value = first_value + second_value
print(f"The sum of user provided two numbers is --> {sum_value}")
sum_string = "The sum of {first_value} and {second_value} is {sum_value}"
print(sum_string.format(first_value=first_value,
                        second_value=second_value,
                        sum_value=sum_value))
