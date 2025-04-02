import random
import sys

def start_game():
    print("""
    Please select the difficulty level:
    1. Easy (10 chances)
    2. Medium (5 chances)
    3. Hard (3 chances)
    """)
    choice = str(input("Enter your choice: ")).lower()
    
    if choice == "easy":
        chances = 10
        return choice, chances
        
    elif choice == "medium":
        chances = 5
        return choice, chances
        
    elif choice == "hard":
        chances = 3
        return choice, chances
    
    else:
        print("Invalid choice.")
        sys.exit(1)
    
def run_game(difficulty, chances):
    print(f"""
    Great! You have chosen the {difficulty} difficulty level.
    You now have {chances} chances.
    Let's start the game!
    """)
    
    number = random.randint(1, 100)
    turns = chances
    
    while turns > 0:
        guess = int(input("Enter your guess: "))
        
        if guess > number:
            turns -= 1
            print("Too high! Try a lower number.")
            print(f"Remaining attempts: {turns}")
            print()
        
        elif guess < number:
            turns -= 1
            print("Too low! Try a higher number.")
            print(f"Remaining attempts: {turns}")
            print()
            
        else:
            print(f"Congratulations! You guessed the correct number in {chances - turns} attempt(s)!")
            print(f"The number was indeed {number}")
            break
            
        if turns == 0:
            print(f"Sorry, you are out of attempts. The correct number was {number}.")
            
if __name__ == "__main__":
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    play_again = True
    
    while play_again:
        difficulty, chances = start_game()
        run_game(difficulty, chances)
        
        again = str(input("Play again? (y/n): ")).lower()
        print()
        if again == "n":
            play_again = False
            print("Thanks for playing!")
            sys.exit(0)
