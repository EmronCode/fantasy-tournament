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

        def __str__(self):
            return self.name
        