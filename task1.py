import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the number. Good luck!\n")

def get_player_name():
    return input("Enter your name: ")

def generate_random_number():
    return random.randint(1, 100)

def play_game():
    attempts = 10
    random_number = generate_random_number()
    
    for attempt in range(1, attempts + 1):
        guess = int(input(f"Attempt {attempt}: Enter your guess: "))
        
        if guess == random_number:
            print(f"Congratulations, you've guessed the number {random_number} correctly!")
            return True
        elif guess < random_number:
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
    
    print(f"\nGame over! The number was {random_number}. Better luck next time!")
    return False

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().startswith('y')

def main():
    welcome_message()
    player_name = get_player_name()

    while True:
        if play_game():
            if not play_again():
                print("Thanks for playing! Goodbye.")
                break
        else:
            if not play_again():
                print("Thanks for playing! Goodbye.")
                break
        print("\n")

if __name__ == "__main__":
    main()
