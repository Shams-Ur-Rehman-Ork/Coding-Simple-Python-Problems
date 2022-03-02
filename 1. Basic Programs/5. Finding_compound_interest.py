# Step: 1 --> First understand compound interest formula
"""
Formula --> A = P(1 + R/100)^t
A --> Amount, P --> Principal amount, R --> Rate, T --> Time span
"""


# Step: 2 --> Solution
def calculate_compound_interest(p_amount, rate, time):
    # Calculating power using **
    # Amount = p_amount * ((1 + rate/100) ** time)

    # Calculating power using pow
    amount = p_amount * pow(1 + rate / 100, time)
    compound_interest = amount - p_amount
    return compound_interest


principal_amount = int(input("Enter a principal Amount: "))
rate_amount = float(input("Enter Rate Amount: "))
time_span = int(input("Enter a Time Span: "))

result = calculate_compound_interest(principal_amount, rate_amount, time_span)

print(result)
