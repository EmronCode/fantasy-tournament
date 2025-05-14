# This will get a list of moves that a Character can do based on their Class/Role
def get_moves(character):
    move_dict = {
        "Warrior": ["Physical"],
        "Mage": ["Magical"],
        "Rogue": ["Physical", "Magical"],
        "Archer": ["Physical", "Magical"],
        "Cleric": ["Heal"]
    }

    return move_dict[character.role]
