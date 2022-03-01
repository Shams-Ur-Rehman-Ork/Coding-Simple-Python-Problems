"""We will take three values from user i.e
    1. Amount in integer form
    2. Time in integer form
    3. Rate percent in integer form
"""

# Method: 1 --> Brute force Approach.
"""
    Step: 1 --> get data from user
    Step: 2 --> implement formula
    Step: 3 --> return result
"""


def simple_interest(amount, time, rate):
    interest = (amount * time * rate) / 100
    return interest


amount_value = int(input("Enter Amount: "))
time_value = int(input("Enter time: "))
rate_value = int(input("Enter rate value: "))
result = simple_interest(amount_value, time_value, rate_value)
print(f"Simple interest on Amount {amount_value} is {result}")
