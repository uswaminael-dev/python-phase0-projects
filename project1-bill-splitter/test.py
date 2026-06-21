# Test 1: Variables and types
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"{name} is {age} years old")

# Test 2: Math with floats
bill = float(input("Enter bill: "))
tip = bill * 0.20
total = bill + tip
print(f"Bill: ${bill:.2f}")
print(f"Tip: ${tip:.2f}")
print(f"Total: ${total:.2f}")