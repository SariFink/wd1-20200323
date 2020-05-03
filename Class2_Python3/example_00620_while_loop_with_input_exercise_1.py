# Write a loop, which asks for an input,
# until you entered a valid operator

# hint:
# "+" in "+-/*"
# "+" in ["*", "+", "-", "/"]
print("+-" in "+-/*")                # True
print("+-" in ["*", "+", "-", "/"])  # False

operation = None

while operation not in ["*", "+", "-", "/"]:
    operation = input("Please enter one of the following: '*', '+', '-', '/'")
else:
    print(f"Thank you, you entered: {operation}")