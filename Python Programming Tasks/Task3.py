# Password Generator Program. This program generates a random password based on user-defined complexity levels. It allows users to choose between low, medium, and high complexity passwords and ensures that the password length is at least 8 characters.

import random # Importing the random module to generate random numbers.

import string # Importing the string module to access string constants.


def generate_password(length , complexity): # Function to generate a password.
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    if complexity == 'low':
        
        characters = lowercase + digits
        
    elif complexity == 'medium':
        
        characters = lowercase + uppercase + digits
        
    elif complexity == 'high': 
        
        characters = lowercase + uppercase + digits + special_characters
    
    password_list = [] # Initialize an empty list to store the password characters.
    
    if complexity == 'low': # For low complexity, add at least one lowercase and one digit.
        
        password_list.append(random.choice(lowercase))
        password_list.append(random.choice(digits))
        
    elif complexity == 'medium': # For medium complexity, add at least one lowercase, one uppercase, and one digit.
        
        password_list.append(random.choice(lowercase))
        password_list.append(random.choice(uppercase))
        password_list.append(random.choice(digits))
        
    elif complexity == 'high': # For high complexity, add at least one lowercase, one uppercase, one digit, and one special character.
        
        password_list.append(random.choice(lowercase))
        password_list.append(random.choice(uppercase))
        password_list.append(random.choice(digits))
        password_list.append(random.choice(special_characters))   
    
    while len(password_list) < length: # Ensure the password length is met.
            
            password_list.append(random.choice(characters)) # Append random characters to the password list.
            
    random.shuffle(password_list) # Shuffle the password list to randomize the order.
            
    password = ''.join(password_list) # Join the list into a string.
    
    return password # Return the generated password.


def main(): # Main function to run the password generator.
    
    while True: 
        
        print("Welcome to the Password Generator!")
        print("\n")
        print("Select complexity level:")
        print("\n")
        print("1. Low")
        print("2. Medium")
        print("3. High")
        print("\n")
            
        complexity = input("Enter your choice (1/2/3): ").strip()

        while complexity not in ['1', '2', '3']:   # Check if the entered complexity level is valid, otherwise, prompt again.
            
            print("Invalid input! Please enter (1/2/3) only.")
            print("\n")
            complexity = input("Enter your choice (1/2/3): ").strip()

        if complexity == '1': # Convert the complexity choice to a string ('low', 'medium', 'high')
            
            complexity = 'low'
            
        elif complexity == '2': # Convert the complexity choice to a string ('low', 'medium', 'high')
            
            complexity = 'medium'
            
        elif complexity == '3': # Convert the complexity choice to a string ('low', 'medium', 'high')
            
            complexity = 'high'

        while True: # Get the desired password length from the user
            
            try:
                
                length = int(input("Enter the desired password length (minimum 10): ").strip())

                if length < 10: # Check if the length is valid (at least 10 characters)
                    
                    print("Password length must be at least 10 characters.")
                    
                    continue  # Ask for the length again if it's invalid
                
                break  # Exit the loop if the length is valid
            
            except ValueError:
                
                print("Invalid input! Please enter a valid number for the password length.")
                continue  # Ask for the length again if it's invalid

        password = generate_password(length, complexity)
            
        print("Generating your password...")
        print("\n")
        print("Password generated successfully!")
        print(f"Your password is: {password}")
        print("\n")
        
        ch = input("Do you want to exit the application? (Y/N): ").strip() # Ask user if they want to exit the application.
        
        while ch not in ['Y', 'N', 'y', 'n']: # Check if the input is valid.
                
                print("Invalid input! Please enter (Y/N) only.")
                print("\n")
                
                ch = input("Do you want to exit the application? (Y/N): ").strip()
        
        if ch.lower() == 'y':
            
            print("Thank you for using the Password Generator!")
            print("Goodbye!")
            print("\n")
            break # Exit the application if user chooses 'Y'
        
        else:
            
            continue
            
if __name__ == "__main__":
    
    main()