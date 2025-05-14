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

# Process each battle in the log
for _, battle in df.iterrows():
    winner_team = set(battle["winner"])
    survivors = set(battle["survivor"])

    for team in ["team1", "team2"]:
        for character in battle[team]:
            character_results[character]["battles"] += 1
            if character in winner_team:
                character_results[character]["wins"] += 1
            if character in survivors:
                character_results[character]["survived"] += 1

# Convert stats to a DataFrame
character_df = pd.DataFrame.from_dict(character_results, orient="index")

# Calculate Win and Survival rates
character_df["win_rate"] = character_df["wins"] / character_df["battles"]
character_df["survival_rate"] = character_df["survived"] / character_df["battles"]

# Save updated character performance data
character_df.to_csv(CHARACTER_RESULTS_FILE)
print("Updated Character Performance saved to", CHARACTER_RESULTS_FILE)

print(character_df)

# Sort by Strongest (highes win rate)
strongest_characters = character_df.sort_values(by="win_rate", ascending=False)

# Display win rate
print(strongest_characters)