
def is_good_deal(name1, price1, quantity1, unit1, name2, price2, quantity2, unit2):
    unit_price1 = price1 / (quantity1 * unit1)
    unit_price2 = price2 / (quantity2 * unit2)

    if unit_price1 < unit_price2:
        return f"{name1} is a better deal at ${unit_price1:.2f} per unit."
    elif unit_price2 < unit_price1:
        return f"{name2} is a better deal at ${unit_price2:.2f} per unit."
    else:
        return "Both items ar equally price per unit."

print("Welcome to the 'Is this a good deal?' Checker")
while True:
    name1 = input("Enter item 1 (or leave empty to quit): ")
    if name1 == "":
        break
    while True:
        try:
            price1 = float(input("Enter the price: "))
            if price1 <= 0:
                raise ValueError("Price must be greater than 0.")
            break
        except ValueError as e:
            print(f'Invalid input: {e}')
    while True:
        try:
            quantity1 = float(input("Enter the quantity(e.g. (24) bottles of water): "))
            if quantity1 <= 0:
                raise ValueError("Quantity must be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")
    while True:
        try:
            unit1 = float(input("Enter measurement for item 1 (e.g. (10) gallons): "))
            if unit1 <= 0:
                raise ValueError("Measurement should be greater than 0.")
            break
        except ValueError as e:
            print(f"Invalid input: {e}")

    name2 = input("Enter item 2 (or leave empty to quit): ")
    if name2 == "":
        break
    while True:
        try:
            price2 = float(input("Enter the price: "))
            if price1 <= 0:
                raise ValueError("Price must be greater than 0.")
            break
        except ValueError as e:
            print(f'Invalid input: {e}')
    while True:
        try:
            quantity2 = float(input("Enter the quantity(e.g. (8) juice boxes): "))
            if price1 <= 0:
                raise ValueError("Price must be greater than 0.")
            break
        except ValueError as e:
            print(f'Invalid input: {e}')
    while True:
        try:
            unit2 = float(input("Enter unit measurement for item 2(e.g. (30) oz): "))
            if price1 <= 0:
                raise ValueError("Price must be greater than 0.")
            break
        except ValueError as e:
            print(f'Invalid input: {e}')

    print(is_good_deal(name1, price1, quantity1, unit1, name2, price2, quantity2, unit2))
        
    cont = input("Do you want to compare more items? (yes/no): ").strip().lower()
    if cont != 'yes':
        break



                            
            
