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
        

def get_bill_amount():
    total_bill = get_positive_int("Enter the total bill amount: $")
    return total_bill

def get_tax_percentage():
    tax_percentage = get_percentage("Enter tax percentage: ")
    return tax_percentage

def get_tip_percentage():
    tip_percentage = get_percentage("Enter tip percentage: ")
    return tip_percentage

def get_number_of_people():
    num_of_people = int(get_positive_int("How many people? "))
    return num_of_people
    
def calculate_amounts(total_bill, tax_percentage, tip_percentage):
    tax = total_bill * (tax_percentage / 100)
    tip = total_bill * (tip_percentage / 100)
    total = total_bill + tax + tip
    return tax, tip, total

def display_results(tax_percentage, tip_percentage, total_bill, tax, tip, total, num_of_people):
    per_person = total / num_of_people
    print("=" * 40)
    print("CALCULATION BREAKDOWN".center(40))
    print("=" * 40)

    print(f"{'Original Bill:':<20} ${total_bill:>8.2f}")
    print(f"Tax {tax_percentage}%: ${tax:>8.2f}")
    print(f"Tip {tip_percentage}%: ${tip:>8.2f}")
    print("-" * 40)
    print(f"{'Total Amount:':<20} ${total:>8.2f}")
    print(f"{'Number of People:':<20} {num_of_people:>8}")
    print("-" * 40)
    print(f"{'Each person pays:':<20} ${per_person:>8.2f} /person")
    print("=" * 40)


def main():
    """Main program flow."""
    print("=" * 40)
    print("BILL SPLIT CALCULATOR".center(40))
    print("=" * 40)
    
    # Get inputs
    bill = get_bill_amount()
    tax_percentage = get_tax_percentage()
    tip_percentage = get_tip_percentage()
    people = get_number_of_people()
    
    # Calculate
    tax, tip, total = calculate_amounts(bill, tax_percentage, tip_percentage)
    
    # Display
    display_results(tax_percentage, tip_percentage, bill, tax, tip, total, people)
    
if __name__ == "__main__":
    main()