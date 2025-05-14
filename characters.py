# Character class
class Character:
    def __init__(self, name: str, role: str, health: int, strength: int, magic_power: int,
                 defense: int, magic_defense: int, speed: int, element_1: str, element_2: str):
        self.name = name
        self.role = role
        self.health = health
        self.max_health = health
        self.strength = strength
        self.magic_power = magic_power
        self.defense = defense
        self.magic_defense = magic_defense
        self.speed = speed
        self.element_1 = element_1
        self.element_2 = element_2
        self.team_members = []
        self.targeting_order = self.targeting()

    # When a Character Object is printed, it will display their name
    def __str__(self):
        return self.name
    
    # When a list is printed that contains a Character Object, the Character's name will display
    def __repr__(self):
        return self.name
    
    # This will reset the Character fully
    def reset(self):
        self.health = self.max_health
        self.team_members = []
    
    # This will add a Character as a Team Member
    def add_team_member(self, ally):
        if isinstance(ally, list):
            self.team_members.extend(ally)
        else:
            self.team_members.append(ally)
    
    # This will deal damage to an opponent
    def deal_damage(self, opponent, attack_type: str):
        attack_type_dict = {
            "strength": "defense",
            "magic_power": "magic_defense"
        }

        attack_stat = getattr(self, attack_type)
        defense_stat = getattr(opponent, attack_type_dict[attack_type])

        # The damage is the difference between the attacker's attack stat and the opponents defense stat
        # The damage will at minimum do 1 point of damage
        damage = max(1, attack_stat - defense_stat)
        opponent.health -= damage

    # This will heal a Character for 10 HP
    def heal(self, ally):
        ally.health += 10

        if ally.health > ally.max_health:
            ally.health = ally.max_health

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
    