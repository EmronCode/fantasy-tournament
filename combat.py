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

# This will determine the targeting order of a Character
def determine_target(character_list, targeter):
    priority_order = targeter.targeting_order
    index = 0
    
    while index < len(targeter.targeting_order):
        target_list = [character for character in character_list if
                       character.role == priority_order[index] and
                       character.health > 0]
        
        if target_list:
            break

        index += 1

    if len(target_list) == 1:
        return target_list[0]
    elif target_list:
        # Sort by highest health, then by highest speed
        target_list.sort(key=lambda character: (character.health, character.speed), reverse=True)
        return target_list[0]
    else:
        return None
    