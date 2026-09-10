from player import Player
from wizard import Wizard
from warrior import Warrior
from necro import Necromancer

def main():
    wizname = input("Enter the name of the wizard: ")
    warname = input("Enter the name of the warrior: ")
    necroname = input("Enter the name of the necromancer:")

    # shared state for both players
    player1 = Wizard(name = wizname, health = 10)
    player2 = Warrior(name = warname, health = 10)
    player3 = Necromancer(name = necroname, health = 10)
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
