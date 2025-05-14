import os
import json
import random
import copy
from itertools import combinations
from characters import Character
from match import play

Jinxx = Character("Jinxx", "Mage", 75, 15, 31, 10, 15, 10, "Light", "Dark")
Peachy = Character("Peachy", "Mage", 75, 18, 25, 10, 15, 11, "Fire", "Light")
Gold = Character("Gold", "Mage", 93, 15, 25, 10, 12, 12, "Water", "Air")
Night = Character("Night", "Rogue", 100, 20, 25, 10, 7, 16, "Earth", "Air")
Shortie = Character("Shortie", "Mage", 75, 15, 25, 12, 15, 9, "Earth", "Light")
Sun = Character("Sun", "Warrior", 125, 31, 15, 12, 10, 5, "Fire", "Water")
Moon = Character("Moon", "Cleric", 75, 1, 1, 18, 18, 7, "Earth", "Light")
Lotus = Character("Lotus", "Rogue", 125, 20, 25, 10, 7, 12, "Water", "Earth")
Stone = Character("Stone", "Rogue", 125, 20, 31, 7, 7, 14, "Water", "Dark")
Goat = Character("Goat", "Archer", 125, 31, 20, 7, 10, 2, "Fire", "Air")
Fury = Character("Fury", "Archer", 125, 25, 20, 10, 12, 1, "Earth", "Light")
Ghost = Character("Ghost", "Rogue", 100, 20, 31, 7, 7, 15, "Air", "Dark")
Beastie = Character("Beastie", "Cleric", 93, 1, 1, 15, 18, 8, "Water", "Light")
Galaxy = Character("Galaxy", "Archer", 125, 25, 25, 7, 10, 3, "Air", "Dark")
Akame = Character("Akame", "Warrior", 100, 31, 20, 12, 10, 6, "Fire", "Dark")
Emron = Character("Emron", "Warrior", 100, 31, 15, 15, 10, 4, "Fire", "Earth")

# Define path
DATA_FOLDER = "data"
BATTLE_LOG_FILE = os.path.join(DATA_FOLDER, "battle_data.json")

# Ensure data folder exists
os.makedirs(DATA_FOLDER, exist_ok=True)

# Load existing data
if os.path.exists(BATTLE_LOG_FILE):
    with open(BATTLE_LOG_FILE, "r") as f:
        try:
            battle_log = json.load(f)
        except json.JSONDecodeError:
            battle_log = []
else:
    battle_log = []

# List of all characters
character_list = [Jinxx, Peachy, Gold, Night, Shortie, Sun, Moon, Lotus,
                  Stone, Goat, Fury, Ghost, Beastie, Galaxy, Akame, Emron]

# Simulate 1000 random battles (no repeats)
def simulate_battle(num_battles=1000):
    # Store past matchups to avoid repeats
    used_matchups = set()

    for _ in range(num_battles):
        # Generate unique team1
        team1 = random.sample(character_list, 4)

        # Generate unique team2 (no using Characters that are on team1)
        remaining_characters = [character for character in character_list if character not in team1]
        team2 = random.sample(remaining_characters, 4)

        # Clone characters to reset their health and stats before battle
        team1 = [copy.deepcopy(character) for character in team1]
        team2 = [copy.deepcopy(character) for character in team2]

        # Store the matchup to used_matchups
        matchup = frozenset([tuple(team1), tuple(team2)])

        # Ensure variety in matchups
        if matchup not in used_matchups:
            used_matchups.add(matchup)

            # Simulate a battle
            play(team1, team2)

# Simulate every single battle (avoid repeat matchs and no match should have the same two or more Characters)
def simulate_all_battles():
    # Store past matchups to avoid repeats
    used_matchups = set()

    # Generate all possible unique teams of 4 characters
    all_possible_teams = list(combinations(character_list, 4))

    # Iterate through all possible team1-team2 matchups
    for team1 in all_possible_teams:
        remaining_characters = [char for char in character_list if char not in team1]

        # Generate valid team2 options
        for team2 in combinations(remaining_characters, 4):  
            matchup = frozenset([tuple(team1), tuple(team2)])

            # Ensure no repeat battles
            if matchup not in used_matchups:
                used_matchups.add(matchup)

                # Clone teams to reset character stats before battle
                team1_copy = [copy.deepcopy(char) for char in team1]
                team2_copy = [copy.deepcopy(char) for char in team2]

                # Simulate the battle
                play(team1_copy, team2_copy)

# Run simulate_battle()
# simulate_battle(1000)

# Run simulate_all_battles()
simulate_all_battles()