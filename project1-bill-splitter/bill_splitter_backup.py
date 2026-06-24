print("=" * 40)
print("BILL SPLIT CALCULATOR".center(40))
print("=" * 40)

print("Welcome to Bill Splitter!")  #GREETINGS TO THE USER

def get_percentage(prompt):
    while True:
        try:
            value = float(input(prompt))
            if 0 <= value <= 100:
                return value
            else:
                print("Please enter a percentage between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
            
def get_positive_int(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    

total_bill = get_positive_int("Enter the total bill amount: $")  
tax_percentage = get_percentage("Enter tax percentage: ")
tip_percentage = get_percentage("Enter tip percentage: ")
num_of_people = int(get_positive_int("How many people? "))

tax = total_bill * (tax_percentage / 100)   #TAX CALCULATION

tip = total_bill * (tip_percentage / 100)   #TIP CALCULATION

total = total_bill + tax + tip   #TOTAL AMOUNT CALCULATION

per_person = total / num_of_people

print("=" * 40)
print("CALCULATION BREAKDOWN".center(40))
print("=" * 40)

print(f"{'Original Bill:':<20} ${total_bill:>8.2f}")
print(f"Tax {int(tax_percentage)}%: ${tax:>8.2f}")
print(f"Tip {int(tip_percentage)}%: ${tip:>8.2f}")
print("-" * 40)
print(f"{'Total Amount:':<20} ${total:>8.2f}")
print(f"{'Number of People:':<20} {num_of_people:>8}")
print("-" * 40)
print(f"{'Each person pays:':<20} ${per_person:>8.2f} /person")
print("=" * 40)