# Character class
class Character:
    def __init__(self, name: str, role: str, health: int, strength: int, magic_power: int,
                 defense: int, magic_defense: int, speed: int, element_1: str, element_2: str):
        self.name = name
        self.role = role
        self.health = health
        self.strength = strength
        self.magic_power = magic_power
        self.defense = defense
        self.magic_defense = magic_defense
        self.speed = speed
        self.element_1 = element_1
        self.element_2 = element_2

    # When a Character Object is printed, it will display their name
    def __str__(self):
        return self.name
    
    # When a list is printed that contains a Character Object, the Character's name will display
    def __repr__(self):
        return self.name
    
    # Dictionary for the Class priority order
    def targeting(self):
        priority_dict = {
            "Warrior": ["Mage", "Warrior", "Rogue", "Cleric", "Archer"],
            "Mage": ["Warrior", "Mage", "Cleric", "Archer", "Rogue"],
            "Rogue": ["Archer", "Cleric", "Mage", "Rogue", "Warrior"],
            "Archer": ["Cleric", "Rogue", "Warrior", "Archer", "Mage"],
            "Cleric": ["Mage", "Warrior", "Rogue", "Archer", "Cleric"]
        }

        return priority_dict[self.role]