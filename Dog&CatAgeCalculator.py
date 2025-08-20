def DogAgeCalc(fAge):
    nDog_Age = 7.3
    while True:
            try:
                if fAge <= 0:
                    print(f'You entered {fAge}, but you must enter a number greater than 0')
                    continue
                elif fAge <= 1:
                    fHumanAge = fAge * nDog_Age
                else:
                    fHumanAge = (fAge -1) * nDog_Age + fAge
                return fHumanAge
            except ValueError:
                print("Enter a valid number like 3.2 or 6")
                continue
def CatAgeCalc(fAge):
    if fAge <= 0:
        return f"You entered {fAge}, but you must enter a number greater than 0."
    
    # Dictionary for exact mappings
    age_map = {
        1: 15, 2: 24, 3: 28, 4: 32, 5: 36, 6: 40, 7: 44, 8: 48,
        9: 52, 10: 56, 11: 60, 12: 64, 13: 68, 14: 72, 15: 76,
        16: 80, 17: 84}
    
    # If the age is in the dictionary, return the mapped value
    if fAge in age_map:
        return age_map[fAge]
    
    # For ages beyond 17, estimate using a formula (adding ~4 years per extra year)
    return 84 + (fAge - 17) * 4

def Main():
     while True:
        try:
            Pet = input("Do you have a Cat or Dog (or type 'exit' to quit): ").lower()
            if Pet == 'exit':
                print("Goodbye")
                break
            elif Pet == "dog":
                fAge = float(input("Enter your dog's age: "))
                fHumanAge = DogAgeCalc(fAge)
                print(f"The human age equal to your dog is: {fHumanAge:.1f}")
            else:
                fAge = float(input("Enter your cat's age: "))
                fHumanAge = CatAgeCalc(fAge)
                print(f"The human age equal to your cat is: {fHumanAge:.1f}")
        except ValueError:
            print("Enter 'Cat', 'Dog', or 'exit'")
        continue
Main()

    
