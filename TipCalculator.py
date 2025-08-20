def tip_calculator():
    print("Welcome to the Tip Calculator!")
    
    # Get input from the user
    bill = float(input("Enter the total bill amount ($): "))
    tax_percentage = float(input("Enter the tax percentage (e.g., 8.5 for 8.5%(or 0 if tax included): "))
    tip_percentage = float(input("What percentage tip would you like to give? (e.g., 10, 15, 20): "))
    num_people = int(input("How many people are splitting the bill? "))

    # Calculate tax, tip, and total bill
    tax_amount = bill * (tax_percentage / 100)
    tip_amount = (bill + tax_amount) * (tip_percentage / 100)
    total_bill = bill + tax_amount + tip_amount
    per_person = total_bill / num_people

    # Display results
    print(f"\nTax Amount: ${tax_amount:.2f}")
    print(f"Tip Amount: ${tip_amount:.2f}")
    print(f"Total Bill (including tax and tip): ${total_bill:.2f}")
    print(f"Each person pays: ${per_person:.2f}")

# Run the tip calculator
tip_calculator()
