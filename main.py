from player import Player
from wizard import Wizard
from warrior import Warrior

def main():
    wizname = input("Enter the name of the wizard: ")
    warname = input("Enter the name of the warrior: ")

    # shared state for both players
    player1 = Wizard(name = wizname, health = 10)
    player2 = Warrior(name = warname, health = 10)
    print(f"Welcome {player1.name} the wizard and {player2.name} the warrior! Let the battle begin!")
    print("...Starting Game...")
    print("____________________________________")
    turn = 0

    while player1.health > 0 and player2.health > 0:
        # shared behavior for both players is displaying status
        print(player1.status())
        print(player2.status())
        print("____________________________________")
        
        if turn % 2 == 0:
            print(f"{player1.name}'s turn!")
            # wizard specific behavior
            print(player1.attack(player2))
            print("____________________________________")

            print(f"{player1.name}'s turn is over!")
            turn = turn + 1
        else:
            print(f"{player2.name}'s turn!")
            # warrior specific behavior
            print(player2.attack(player1))
            print("____________________________________")
            print(f"{player2.name}'s turn is over!")
            turn = turn + 1
    
    if player1.health <= 0:
        print("____________________________________")
        print(f"{player1.name} has been defeated! {player2.name} wins!")
    elif player2.health <= 0:
        print("____________________________________")
        print(f"{player2.name} has been defeated! {player1.name} wins!")

if __name__ == "__main__":
    main()


# 1. What information or behavior did you define once in Player rather than repeat?
# Within the Player class, the attributes 'name' and 'health' were defined. Concerning player behavior, the player class has methods for taking damage, healing, and showing statue.

# 2. Identify the line in your language that establishes the inheritance relationship. What does that line mean?
# The lines that build that inheritance relationship are 'class Warrior(Player):' and 'class Wizard(Player)', and they associate all the behavior and states of the Player class with both the Warrior and Wizard classes.

# 3. Why is this design better than copying an entire Player class for every specialized player?
# It allows for efficiency and more readable code while also separating the unique and specific behavior of wizards and warriors. In addition, it saves storage space by cutting down on unnecessary code.

# IB HL Learning Path
# The 'is-a' relationship means that a specific class is a kind of a broader class. If this relationship doens't hold true, the inheritance wouldn't be the most efficient way to go about design constraints and it could lead to deeper issues within the code.
