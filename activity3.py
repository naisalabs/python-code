try:
    age = int(input("Enter your age: "))

    # Check if age is valid
    if age <= 0 or age > 120:
        print("Error: Invalid age entered.")
    else:
        print("Valid age entered.")

        # Check even or odd
        if age % 2 == 0:
            print("The age is Even.")
        else:
            print("The age is Odd.")
except ValueError:
    print("Error: Please enter a valid numeric age.")