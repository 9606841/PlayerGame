from player import Player

class Wizard(Player):
    def castSpell(self, victim):
        spell = input("Would you like to curse your opponent, attack your opponent, or heal yourself? (c/a/h):")
        while spell != "c" and spell != "a" and spell != "h":
            spell = input("Please enter a valid option (c/a/h):")
        
        if spell == "c":
            victim.takeDamage(2)
            self.heal(2)
            return f"{self.name} has cursed {victim.name} and taken 2 health! {self.name}'s current health is {self.health} {victim.name}'s current health is {victim.health}."    
        elif spell == "a":
            victim.takeDamage(5)
            return f"{self.name} has attacked {victim.name}! {victim.name}'s current health is {victim.health}."
        elif spell == "h":
            self.heal(5)
            return f"{self.name} has healed 5 health! {self.name}'s current health is {self.health}."
    