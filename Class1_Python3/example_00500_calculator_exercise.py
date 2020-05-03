# print welcome to user
print("Welcome user! I will calculate for you!")
# read user input for operation
operation = input("Please enter one of: '+', '/', '+', '-' ")

# read user input for first value
number_1 = float(input("Please enter first number: "))

# read user input for second value
number_2 = float(input("Please enter second number: "))


# calculate depending on operators
result = None

if operation == "+":
    result = number_1 + number_2
elif operation == "-":
    result = number_1 - number_2
elif operation == "*":
    result = number_1 * number_2
elif operation == "/" and number_2 != 0:
    result = number_1 / number_2

# and print result
if result is None:
    print(f"Result of {number_1} {operation} {number_2} could not be calculated, please try again")
else:
    print(f"{number_1} {operation} {number_2} = {result}")




