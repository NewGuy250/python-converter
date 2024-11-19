def convert_imperial_to_metric():
    print("Welcome to the Imperial to Metric Converter!")
    print("Choose the type of conversion:")
    print("1. Length (inches, feet, yards, miles to cm, meters, km)")
    print("2. Weight (pounds, ounces to kg, grams)")
    print("3. Temperature (Fahrenheit to Celsius)")

    while True:
        choice = input("Enter the number of your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            break
        print("Invalid choice. Please enter 1, 2, or 3.")

    if choice == '1':  # Length Conversion
        print("\nLength Conversion:")
        print("a. Inches to Centimeters")
        print("b. Feet to Meters")
        print("c. Yards to Meters")
        print("d. Miles to Kilometers")

        while True:
            sub_choice = input("Choose an option (a/b/c/d): ").lower()
            if sub_choice in ['a', 'b', 'c', 'd']:
                break
            print("Invalid option. Please enter a, b, c, or d.")
        
        while True:
            try:
                value = float(input("Enter the value to convert: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        if sub_choice == 'a':
            print(f"{value} inches = {value * 2.54} cm")
        elif sub_choice == 'b':
            print(f"{value} feet = {value * 0.3048} meters")
        elif sub_choice == 'c':
            print(f"{value} yards = {value * 0.9144} meters")
        elif sub_choice == 'd':
            print(f"{value} miles = {value * 1.60934} kilometers")

    elif choice == '2':  # Weight Conversion
        print("\nWeight Conversion:")
        print("a. Pounds to Kilograms")
        print("b. Ounces to Grams")

        while True:
            sub_choice = input("Choose an option (a/b): ").lower()
            if sub_choice in ['a', 'b']:
                break
            print("Invalid option. Please enter a or b.")
        
        while True:
            try:
                value = float(input("Enter the value to convert: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        if sub_choice == 'a':
            print(f"{value} pounds = {value * 0.453592} kg")
        elif sub_choice == 'b':
            print(f"{value} ounces = {value * 28.3495} grams")

    elif choice == '3':  # Temperature Conversion
        print("\nTemperature Conversion:")
        while True:
            try:
                value = float(input("Enter the temperature in Fahrenheit: "))
                break
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        
        celsius = (value - 32) * 5 / 9
        print(f"{value}°F = {celsius:.2f}°C")

# Run the converter
convert_imperial_to_metric()
