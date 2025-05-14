import os
import json
from combat import take_action, determine_character_list

# Define path
DATA_FOLDER = "data"
BATTLE_LOG_FILE = os.path.join(DATA_FOLDER, "battle_data.json")

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

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

# Will quickly add all the Characters as each other's Team Members
def quick_add_team_member(team):
    team_list = list(team)
    for character in team_list:
        character.add_team_member([member for member in team_list if member != character])

# Will quickly reset all the Characters
def quick_reset_all(team):
    team_list = list(team)
    for character in team_list:
        character.reset()        

# Will check to see if a team has won
def win(t1, t2, whole_team, team):
    log_battle(t1, t2, whole_team, team)
    print("WINNERS: " + ", ".join(str(character) for character in whole_team))
    print("STILL STANDING: " + ", ".join(str(character) for character in team))

# Will play a simulation of a single fight
def play(whole_t1, whole_t2):
    t1 = list(whole_t1)
    t2 = list(whole_t2)

    turn_list = set_turn_list(t1, t2)

    alive_t1 = len(t1)
    alive_t2 = len(t2)

    game_over = False

    quick_reset_all(t1)
    quick_reset_all(t2)

    quick_add_team_member(t1)
    quick_add_team_member(t2)

    while alive_t1 > 0 and alive_t2 > 0:
        for character in turn_list:
            if not game_over:
                if character.health > 0 and alive_t1 > 0 and alive_t2 > 0:
                    take_action(determine_character_list(t1, t2, character), character)

            alive_t1 = len(t1)
            alive_t2 = len(t2)
            game_over = alive_t1 < 1 or alive_t2 < 1

        print("END OF TURNS")
        print(" ")
        print("Character's HEALTH")
        turn_list = set_turn_list(t1, t2)

        for character in turn_list:
            print(character.name + ": " + str(character.health))

        print(" ")
        print(" ")
        print(" ")

    if alive_t1 > 0:
        win(whole_t1, whole_t2, whole_t1, t1)

    if alive_t2 > 0:
        win(whole_t1, whole_t2, whole_t2, t2)

# Logs the battle results
def log_battle(t1, t2, winner, survivor):
    # Load existing data
    if os.path.exists(BATTLE_LOG_FILE):
        with open(BATTLE_LOG_FILE, "r") as f:
            try:
                battle_log = json.load(f)
            except json.JSONDecodeError:
                battle_log = []
    else:
        battle_log = []

    # Append new battle data
    battle_log.append({
        "team1": [character.name for character in t1],
        "team2": [character.name for character in t2],
        "winner": [character.name for character in winner],
        "survivor": [character.name for character in survivor],
    })

    # Save updated battle log
    with open(BATTLE_LOG_FILE, "w") as f:
        json.dump(battle_log, f, indent=4)
