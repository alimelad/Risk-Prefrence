
import pygambit
import math

# Step 1: Create a new strategic-form game
game = pygambit.Game.new_table([2, 2])  # 2 strategies for each of 2 players
game.title = "Stag Hunt Game with Risk Aversion"

# Step 2: Label players and strategies
game.players[0].label = "Player 1"
game.players[1].label = "Player 2"
game.players[0].strategies[0].label = "Stag"
game.players[0].strategies[1].label = "Hare"
game.players[1].strategies[0].label = "Stag"
game.players[1].strategies[1].label = "Hare"

# Step 3: Assign payoffs (use Player objects explicitly)
game[0, 0][game.players[0]] = 4  # Player 1 payoff for (Stag, Stag)
game[0, 0][game.players[1]] = 4  # Player 2 payoff for (Stag, Stag)

game[0, 1][game.players[0]] = 1  # Player 1 payoff for (Stag, Hare)
game[0, 1][game.players[1]] = 3  # Player 2 payoff for (Stag, Hare)

game[1, 0][game.players[0]] = 3  # Player 1 payoff for (Hare, Stag)
game[1, 0][game.players[1]] = 1  # Player 2 payoff for (Hare, Stag)

game[1, 1][game.players[0]] = 2  # Player 1 payoff for (Hare, Hare)
game[1, 1][game.players[1]] = 2  # Player 2 payoff for (Hare, Hare)

# Step 4: Define a utility function for risk aversion
def utility(payoff, risk_aversion=0.5):
    """
    Compute the utility of a monetary payoff under risk aversion.
    Args:
        payoff: float, monetary payoff.
        risk_aversion: float, risk aversion parameter (0 = risk-neutral).
    Returns:
        Utility value of the payoff.
    """
    if payoff > 0:
        return (1 - math.exp(-risk_aversion * payoff)) / risk_aversion
    elif payoff == 0:
        return 0
    else:
        return -float("inf")  # Negative infinity for invalid payoffs

# Step 5: Transform monetary payoffs into utilities
risk_aversion_param = 0.5  # Adjust this parameter to test different risk aversion levels
for outcome in game.contingencies:  # Iterate over all pure strategy outcomes
    for player in game.players:  # Transform each player's payoff
        original_payoff = game[outcome][player]
        game[outcome][player] = utility(original_payoff, risk_aversion_param)

# Step 6: Solve for Nash equilibria (pure and mixed)
print("Nash Equilibria (Pure Strategies):")
pure_solver = pygambit.nash.ExternalEnumPureSolver()
pure_equilibria = pure_solver.solve(game)  # Use the external solver
if len(pure_equilibria) == 0:
    print("No pure strategy Nash equilibria found.")
else:
    for eq in pure_equilibria:
        print(eq)

print("\nNash Equilibria (Mixed Strategies):")
mixed_solver = pygambit.nash.ExternalEnumMixedSolver()
mixed_equilibria = mixed_solver.solve(game)  # Use the external solver
if len(mixed_equilibria) == 0:
    print("No mixed strategy Nash equilibria found.")
else:
    for eq in mixed_equilibria:
        for player in game.players:
            probabilities = [eq[player][strategy] for strategy in player.strategies]
            strategy_labels = [strategy.label for strategy in player.strategies]
            print(f"{player.label}: {dict(zip(strategy_labels, probabilities))}")
