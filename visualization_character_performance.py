import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

# Load the data
CHARACTER_STATS_FILE = "data/character_performance.csv"
character_df = pd.read_csv(CHARACTER_STATS_FILE)

# Class/Role colors
role_colors = {
    "Warrior": ("#FF6200", "#FD9346"),
    "Mage": ("#2a6f97", "#61a5c2"),
    "Archer": ("#1E8449", "#7DCEA0"),
    "Rogue": ("#5B2C6F", "#AF7AC5"),
    "Cleric": ("#FFDD3C", "#FFF192"),
}

# Apply a gradient for each class/role using role_colors
def assign_color(row):
    role = row["role"]
    colors = role_colors[role]

    # Filter characters of the same role for consistent color mapping
    role_df = character_df[character_df["role"] == role]
    role_rank = role_df.sort_values(by="rank")["rank"].tolist()

    # Calculate the gradient position (0 to 1)
    if len(role_rank) > 1:
        scale = (row["rank"] - min(role_rank)) / (max(role_rank) - min(role_rank))

        # Apply a non-linear scale to emphasize color difference
        adjusted_scale = scale ** 1.5
    else:
        # Center of gradient for a single character (unlikely but just in case for future development)
        adjusted_scale = 0.5

    # Generate color using a linear gradient
    gradient_cmap = LinearSegmentedColormap.from_list("role_gradient", colors)
    return gradient_cmap(adjusted_scale)

character_df["color"] = character_df.apply(assign_color, axis=1)

# Plot all of the Characters
def plot_all_characters(df):
    df_sorted = df.sort_values(by="rank")

    plt.figure(figsize=(16, 8))

    # Plot bars using colors and no gaps
    bars = plt.bar(df_sorted["name"], df_sorted["win_rate"], color=df_sorted["color"], width=1.0)

    # Win Rate Percentages
    for bar, win_rate in zip(bars, df_sorted["win_rate"]):
        plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{win_rate:.1%}",
                 ha="center", va="bottom", fontsize=10)
        
    plt.title("Character Win Rate Comparison")
    plt.xlabel("Character")
    plt.ylabel("Win Rate")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

plot_all_characters(character_df)
