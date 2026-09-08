from player import Player
from wizard import Wizard
from warrior import Warrior

def main():
    wizname = input("Enter the name of the wizard: ")
    warname = input("Enter the name of the warrior: ")
    newplayer = input("Would you like to add a wizard or a warrior? (w/wa): ")
    if newplayer == "w":
        newname = input("Enter the name of the wizard: ")
        player3 = Wizard(name = newname, health = 10)
    elif newplayer == "wa":
        newname = input("Enter the name of the warrior: ")
        player3 = Warrior(name = newname, health = 10)

    # shared state for both players
    player1 = Wizard(name = wizname, health = 10)
    player2 = Warrior(name = warname, health = 10)
    print(f"Welcome {player1.name}, {player2.name}, and {player3.name}! Let the battle begin!")
    print("...Starting Game...")
    print("____________________________________")
    players = [player1, player2, player3]
                

    while player1.health > 0 and player2.health > 0 and player3.health > 0:
        # shared behavior for both players is displaying status
        for player in players:
            print(player.status())
        print("____________________________________")
        for player in players:
            victim = input(f"{player.name}, who would you like to attack? Enter 1 for {player1.name}, 2 for {player2.name}, or 3 for {player3.name}: ")
            print(player.attack(players[int(victim)-1]))
            print("Turn complete! Next player's turn...")
        
    
    
    if player1.health <= 0 or player2.health <= 0 or player3.health <= 0:
        print("Game Over! One of the players has been defeated.")
        

if __name__ == "__main__":
    main()


# Reflection
# A. METHOD: Which method did you override, and why does it belong in the parent contract?
# The overridden method is the 'attack' method. It belongs in the parent class since the activity of attacking is something that all players need too have the capability to do.

# B. DIFFERENCE: How do at least two subclasses implement it differently?
# The Warrior subclass allows for stabbing and slashing while the Wizard subclass allows for cursing, attacking, and healing. Each of these choices has a different impact on the playability of the game.

# C. COLLECTION: What is the declared type of your collection, and what object types does it actually contain?
# The type of the collection is a list containing player objects, and it holds Wizard and Warrior objects.

# D. DISPATCH: How does the program determine which version of the method runs?
# The kind of method run is done based off of the type of object it's called on(Wizard v. Warrior).

# E. REVISION: What did you change after testing or after Friday's peer interviews?
# I adjusted the turn logic to iterate through every player, and I added capabilities for a third player to be added to the game.
