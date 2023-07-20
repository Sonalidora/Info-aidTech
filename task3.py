import random

def roll_dice(num_dice):
    dice_rolls = [random.randint(1, 6) for _ in range(num_dice)]
    return dice_rolls

def main():
    print("Welcome to the Dice Rolling App!")
    
    while True:
        try:
            num_dice = int(input("Enter the number of dice you want to roll (0 to quit): "))
            if num_dice == 0:
                print("Thank you for using the Dice Rolling App. Goodbye!")
                break
            elif num_dice < 0:
                print("Please enter a positive number or 0 to quit.")
                continue

            dice_results = roll_dice(num_dice)
            print(f"Dice roll result: {', '.join(str(roll) for roll in dice_results)}")
        except ValueError:
            print("Invalid input. Please enter a number or 0 to quit.")

if __name__ == "__main__":
    main()
