#nested if
'''
x = 50
y = 30
'''
'''
if x > 42:
    if<=50:
        print(f'{x} is greater than 42 or equal to 50')
'''

    #if x > 42 and x <= 50:
        #print(f"{x} is greater than or equal to 50")

# using in
'''
        nos = [1,2,3,50,60,30]
        if x not in nos:
            print("gruanted")
        else:
                print("not graunted")
'''
'''
# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

# Main function to take user input and perform calculations
def main():
    while True:
        print("Options:")
        print("1: Addition")
        print("2: Subtraction")
        print("3: Multiplication")
        print("4: Division")
        print("5: Exit")

        choice = input("Enter choice (1-5): ")

        # Check if the choice is valid
        if choice in ['1', '2', '3', '4', '5']:
            if choice == '5':
                print("Exiting calculator. Goodbye!")
                break

            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result: ", add(num1, num2))
            elif choice == '2':
                print("Result: ", subtract(num1, num2))
            elif choice == '3':
                print("Result: ", multiply(num1, num2))
            elif choice == '4':
                print("Result: ", divide(num1, num2))
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Run the calculator
if __name__ == "__main__":
    main()
    '''




























