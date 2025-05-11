# Rock, Paper, Scissors Game Program. This program allows users to play a game of Rock, Paper, Scissors against the computer. It keeps track of the score and announces the overall winner at the end of the game.


import random


def computer_choice():
    
    return random.choice(['rock', 'paper', 'scissors'])


def user_choice():
    
    a = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    
    while a not in ['rock', 'paper', 'scissors']:
        
        print("Invalid input! Please enter (rock, paper, scissors) only.")
        print("\n")
        
        a = input("Enter your choice (rock, paper, scissors): ").strip().lower()
    
    return a


def determine_winner(user, computer):
    
    if user == computer:
        
        return "It's a tie!"
    
    elif (user == 'rock' and computer == 'scissors') or (user == 'paper' and computer == 'rock') or (user == 'scissors' and computer == 'paper'):
        
        return "You win!"
    
    else:
        
        return "Computer wins!"
    
    
def display_score(user_score, computer_score):
    
    print(f"Score: You - {user_score}, Computer - {computer_score}")
    print("\n")
    
    if user_score == computer_score:
        
        print("It's a tie!")
        print("\n")
        
    elif user_score > computer_score:
        
        print("Congratulations! You are the overall winner!")
        print("\n")
        
    else:
        print("Computer is the overall winner!")
        print("\n")
        

def main():
    
    user_score = 0
    computer_score = 0
    
    print("\n")
    print("Welcome to Rock, Paper, Scissors Game!")
    print("\n")
    
    rounds = int(input("Enter the number of rounds you want to play: "))
    print("\n")
    
    while rounds < 1:
        print("Invalid input! Please enter a number greater than 0.")
        print("\n")
        
        rounds = int(input("Enter the number of rounds you want to play: "))
        print("\n")
    
    for i in range(rounds):
        
        user = user_choice()
        computer = computer_choice()
        
        print(f"Computer chose: {computer}")
        print("\n")
        
        result = determine_winner(user, computer)
        
        print(result)
        print("\n")
        
        if result == "You win!":
            
            user_score += 1
            
        elif result == "Computer wins!":
            
            computer_score += 1
        
        else:
            
            pass

    display_score(user_score, computer_score)
    
    print("Thank you for playing!")
    print("Goodbye!")
    print("\n")


if __name__ == "__main__":
    
    main()