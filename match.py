# Will return a list from fastest to slowest Characters
def set_turn_list(t1, t2):
    character_list = t1 + t2
    turn_list = []
    list_length = len(character_list)

    temp_character = character_list[0]

    while len(turn_list) < list_length and character_list:
        temp_character = max(character_list, key=lambda character: character.speed)

        temp_character = next((character for character in character_list if character == temp_character), None)
        if temp_character:
            character_list.remove(temp_character)

        turn_list.append(temp_character)

    print(turn_list)
    return turn_list

# Will play a simulation of a single fight
def play(whole_t1, whole_t2):
    set_turn_list(whole_t1, whole_t2)