def add(a,b): # Function to add two numbers.
    return (a+b)

def subtract(a,b): # Function to subtract two numbers.
    return (a-b)

def multiplication(a,b): # Function to multiply two numbers.
    return (a*b)

def division(a,b): # Function to divide two numbers.
    return (a/b)

def main():  # Main function to run the calculator.
    
    print("Welcome to the Simple Calculator!")
    print("Select operation to continue:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    
    while True:
        
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            
            try:
                num1 = eval(input("Enter first number: "))
                num2 = eval(input("Enter second number: "))

            except ValueError:
                print("Invalid Input! Please enter numeric values only.")
                continue
            
            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiplication(num1, num2))

            elif choice == '4':
                if num2 != 0:
                    print(num1, "/", num2, "=", division(num1, num2))
                else:
                    print("Error! Division by zero.")
            
            else:
                print("Invalid Input! Please select a valid operation.")

        else:
            print("Invalid Choice! Please select a valid operation.")
        
            # Check if the user wants to perform another calculation
        ch = input("Do you want to exit? (Y/N): ")
        
        if ch.upper() == 'Y':
            print("Thank you for using the Simple Calculator!")
            print("Goodbye!")
            break
        
main()  # Call the main function to run the calculator.