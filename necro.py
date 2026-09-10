from player import Player

class Necromancer(Player):
    def attack(self, victim):
        attack = input("Would you like to save yourself or attack your opponent(s/a):")
        while attack != "s" and attack != "a":
            attack = input("Please enter a valid option (s/a):")
        
        if attack == "s":
            self.heal(10-self.health)
            return f"{self.name} has resurrected themselves! {self.name}'s current health is {self.health}."
        elif attack == "sl":
            victim.takeDamage(1)
            return f"{self.name} has attacked {victim.name}, but it wasn't very good! {victim.name}'s current health is {victim.health}."
        
