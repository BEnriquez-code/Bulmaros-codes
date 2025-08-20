#This code is to round decimals to whichever you like

value = input("Do you have a decimal to round? Y/N: ").strip().lower()
if value == 'y':
    try:
        number = float(input("Enter the number: "))
        decimals = int(input("How many decimal places do you want to round to? "))

        rounded_num = round(number, decimals)
        print(f"The rounded number is: {rounded_num}")
    except ValueError:
        print("Invalid input")
else:
    print("Exiting program.")
