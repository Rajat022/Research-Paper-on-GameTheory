from itertools import combinations
from math import factorial

# Define the data for the players
player_data = {
    "PC1": {"profit": 25000, "tolerable_reduction": 0.03, "expected_profit": 10000},
    "PC2": {"profit": 15000, "tolerable_reduction": 0.1, "expected_profit": 5000},
    "PC3": {"profit": 20000, "tolerable_reduction": 0.2, "expected_profit": 8000},
    "PC4": {"profit": 14000, "tolerable_reduction": 0.05, "expected_profit": 5000},
    "PC5": {"profit": 22000, "tolerable_reduction": 0.1, "expected_profit": 7000},
    "PC6": {"profit": 24000, "tolerable_reduction": 0.1, "expected_profit": 9000},
}

# Define a function to calculate the value of a coalition
def coalition_value(coalition):
    total_profit = sum(player_data[player]["profit"] for player in coalition)
    if len(coalition) > 0:
        total_tolerable_reduction = min(player_data[player]["tolerable_reduction"] for player in coalition)
    else:
        total_tolerable_reduction = 0
    total_expected_profit = sum(player_data[player]["expected_profit"] for player in coalition)
    return total_profit - total_tolerable_reduction * total_profit + total_expected_profit

# Define a function to calculate the Shapley value
def shapley_value(players):
    n = len(players)
    shapley_values = {player: 0 for player in players}

    # Define the number of players
    print(f"Number of players: {n}")
    
    # Define the set of possible coalitions
    coalitions = [set(), *[set(comb) for i in range(1, n+1) for comb in combinations(players, i)]]
    print(f"Possible coalitions: {coalitions}")
    
    # Determine the value of each coalition
    coalition_values = {tuple(c): coalition_value(c) for c in coalitions}
    print(f"Coalition values: {coalition_values}")

    for coalition_size in range(1, n+1):
        for coalition in combinations(players, coalition_size):
            for player in coalition:
                coalition_value_diff = coalition_value(coalition) - coalition_value(set(coalition) - {player})
                shapley_values[player] += coalition_value_diff * factorial(len(coalition) - 1) * factorial(n - len(coalition)) / factorial(n)

    # Print the Shapley values for each player
    print("Shapley values:")
    for player, value in shapley_values.items():
        print(f"{player}: {value}")

players = list(player_data.keys())
shapley_value(players)
