import pandas as pd

# Load data
df = pd.read_csv("data/matches.csv")

# Preview data
print(df.head())

# Create total goals column
df["total_goals"] = df["home_goals"] + df["away_goals"]

# Average goals per match
avg_goals = df["total_goals"].mean()
print("Average goals per match:", round(avg_goals, 2))

# Home vs Away wins
home_wins = df[df["home_goals"] > df["away_goals"]].shape[0]
away_wins = df[df["away_goals"] > df["home_goals"]].shape[0]
draws = df[df["home_goals"] == df["away_goals"]].shape[0]

print("Home wins:", home_wins)
print("Away wins:", away_wins)
print("Draws:", draws)
