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

# This will select a specific move from the Character's move list
def select_move(character, target):
    move_list = get_moves(character)

    if len(move_list) == 1:
        return move_list[0]
    
    # Character picks Physical
    if character.strength > character.magic_power:
        return move_list[move_list.index("Physical")]
    
    # Character picks Magical
    if character.strength < character.magic_power:
        return move_list[move_list.index("Magical")]
    
    # Character has same strength and magic power stat, so now they will check their target's stats
    if character.strength == character.magic_power:
        # If target has a lower defense, then use Physical
        if target.defense < target.magic_defense:
            return move_list[move_list.index("Physical")]
        
        # If target has a lower magic defense, then use Magical
        if target.defense < target.magic_defense:
            return move_list[move_list.index("Magical")]
        
        # If the target has same defense and magic defense stat, then use Physical
        if target.defense == target.magic_defense:
            return move_list[move_list.index("Physical")]
