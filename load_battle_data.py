import os
import json
import pandas as pd
from collections import defaultdict

# Define path
DATA_FOLDER = "data"
BATTLE_LOG_FILE = os.path.join(DATA_FOLDER, "battle_data.json")
BATTLE_LOG_PREVIEW_FILE = os.path.join(DATA_FOLDER, "battle_data_preview.csv")
CHARACTER_RESULTS_FILE = os.path.join(DATA_FOLDER, "character_performance.csv")

# Load existing data
if os.path.exists(BATTLE_LOG_FILE):
    with open(BATTLE_LOG_FILE, "r") as f:
        try:
            battle_log = json.load(f)
        except json.JSONDecodeError:
            print("ERROR: battle_data.json is corrupted or empty")
            battle_log = []
else:
    print("ERROR: battle_data.json cannot be found")
    battle_log = []

# Convert to DataFrame
df = pd.DataFrame(battle_log)

# Display the first few rows in terminal
print(df)

# Save a copy to review
df.to_csv(BATTLE_LOG_PREVIEW_FILE)
print("Battle Data saved to", BATTLE_LOG_PREVIEW_FILE)

# Initialize character results
character_results = defaultdict(lambda: {"battles": 0, "wins": 0, "survived": 0})

# Initialize Elo ratings
elo_ratings = defaultdict(lambda: 1000)
K = 32

# Process each battle in the log
for _, battle in df.iterrows():
    team1 = battle["team1"]
    team2 = battle["team2"]
    winner_team = set(battle["winner"])
    survivors = set(battle["survivor"])

    for team in ["team1", "team2"]:
        for character in battle[team]:
            character_results[character]["battles"] += 1
            if character in winner_team:
                character_results[character]["wins"] += 1
            if character in survivors:
                character_results[character]["survived"] += 1

    # Calculate team average Elos
    team1_elo = sum(elo_ratings[character] for character in team1) / len(team1)
    team2_elo = sum(elo_ratings[character] for character in team2) / len(team2)

    # Calculate expected scores (this formula could be SO wrong)
    E1 = 1 / (1 + 10 ** ((team2_elo - team1_elo) / 400))
    E2 = 1 - E1

    # Determine actual results
    S1 = 1 if set(team1) & winner_team else 0
    S2 = 1 if set(team2) & winner_team else 0

    # Update Elo scores
    for character in team1:
        elo_ratings[character] += K * (S1 - E1)
    for character in team2:
        elo_ratings[character] += K * (S2 - E2)

# Convert stats to a DataFrame
character_df = pd.DataFrame.from_dict(character_results, orient="index")

# Calculate Win and Survival rates
character_df["win_rate"] = character_df["wins"] / character_df["battles"]
character_df["survival_rate"] = character_df["survived"] / character_df["battles"]

# Calculate Contribution Score
character_df["contribution_score"] = (
    (character_df["survived"] / character_df["wins"].replace(0, 1)) +
    (character_df["wins"] / character_df["battles"].replace(0, 1))
) / 2

print("\nCharacter Contribution Score")
print(character_df[["contribution_score"]].sort_values(by="contribution_score", ascending=False))

# Character Classes/Roles
character_roles = {
    "Jinxx": "Mage",
    "Peachy": "Mage",
    "Gold": "Mage",
    "Night": "Rogue",
    "Shortie": "Mage",
    "Sun": "Warrior",
    "Moon": "Cleric",
    "Lotus": "Rogue",
    "Stone": "Rogue",
    "Goat": "Archer",
    "Fury": "Archer",
    "Ghost": "Rogue",
    "Beastie": "Cleric",
    "Galaxy": "Archer",
    "Akame": "Warrior",
    "Emron": "Warrior"
}

# Add the character names
character_df["name"] = character_df.index

# Map classes/roles
character_df["role"] = character_df.index.map(character_roles)

# Group and calculate roles average
role_analysis = character_df.groupby("role")[["win_rate", "survival_rate", "contribution_score"]].mean()

print("\nRole Performance Analysis")
print(role_analysis)

# Save Elo ratings to DataFrame
elo_df = pd.DataFrame.from_dict(elo_ratings, orient="index", columns=["elo_rating"])

# Merge with character_df
character_df = character_df.merge(elo_df, left_index=True, right_index=True)

print("\nCharacter Elo Ratings")
print(character_df[["elo_rating"]].sort_values(by="elo_rating", ascending=False))

# Sort by Strongest (highest win rate)
strongest_characters = character_df.sort_values(by="win_rate", ascending=False)

# Sort by Weakest (lowest win rate)
weakest_characters = character_df.sort_values(by="win_rate", ascending=True)

# Display win rate
print("\nTop 5 Strongest Characters")
print(strongest_characters.head(5))

print("\nTop 5 Weakest Characters")
print(weakest_characters.head(5))

# Rank characters from best to worst based on win rate
character_df = character_df.sort_values(by="win_rate", ascending=False)
character_df["rank"] = range(1, len(character_df) + 1)

# Display the full ranking list
print("\nFull Ranking from 1st to Last")
print(character_df[["rank", "win_rate"]])

# Save updated character performance data
character_df.to_csv(CHARACTER_RESULTS_FILE)
print("Updated Character Performance saved to", CHARACTER_RESULTS_FILE)

print(character_df)
