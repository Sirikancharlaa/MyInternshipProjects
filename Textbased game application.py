import time

def introduction():
    print("Welcome to the Text-based Adventure Game!")
    time.sleep(1)
    print("You find yourself standing at the entrance of a mysterious cave.")
    time.sleep(1)
    print("Your journey begins...\n")

def make_choice(choices):
    print("Choose your path:")
    for i, choice in enumerate(choices, start=1):
        print(f"{i}. {choice}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(choices):
                return choice
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

def cave():
    print("You enter the dark cave.")
    time.sleep(1)
    print("As you venture deeper, you see two tunnels.")
    time.sleep(1)
    choices = ["Go left", "Go right"]
    choice = make_choice(choices)

    if choice == 1:
        print("You chose to go left.")
        time.sleep(1)
        print("A giant spider blocks your way!")
        time.sleep(1)
        print("What do you do?")
        choices = ["Fight the spider", "Try to run"]
        choice = make_choice(choices)
        if choice == 1:
            print("You bravely fight the spider and emerge victorious!")
            return "victory"
        else:
            print("The spider catches you. Game over.")
            return "game_over"
    else:
        print("You chose to go right.")
        time.sleep(1)
        print("You discover a treasure chest!")
        time.sleep(1)
        print("Do you open it?")
        choices = ["Open the chest", "Leave it"]
        choice = make_choice(choices)
        if choice == 1:
            print("You open the chest and find a magical artifact!")
            return "victory"
        else:
            print("You decide to leave the chest. The adventure continues.")
            return "continue"

def main():
    introduction()
    result = cave()

    if result == "victory":
        print("Congratulations! You have successfully completed the adventure.")
    elif result == "game_over":
        print("Game over. Better luck next time.")
    else:
        print("The adventure continues...")

if __name__ == "__main__":
    main()
