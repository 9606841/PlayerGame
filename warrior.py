from player import Player

class Warrior(Player):
    def swingSword(self, victim):
        attack = input("Would you like to stab or slash your opponent? (s/sl):")
        while attack != "s" and attack != "sl":
            attack = input("Please enter a valid option (s/sl):")
        
        if attack == "s":
            victim.takeDamage(2)
            return f"{self.name} has stabbed {victim.name}! {victim.name}'s current health is {victim.health}."
        elif attack == "sl":
            victim.takeDamage(5)
            self.takeDamage(3)
            return f"{self.name} has slashed {victim.name}, but they've gotten tired! {victim.name}'s current health is {victim.health}. {self.name}'s current health is {self.health}."
        