# Elisa Tandra
# 8/27/2026

class Player:

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def takeDamage(self, amount):
        self.health = self.health - amount
        return f"{self.name} has lost {amount} health! {self.name}'s current health is {self.health}."

    
    def heal(self, amount):
        self.health = self.health + amount
        return f"{self.name} has healed {amount} health! {self.name}'s current health is {self.health}."
        

    def status(self):
        return f"Player Status for {self.name}: Health of {self.health}."


