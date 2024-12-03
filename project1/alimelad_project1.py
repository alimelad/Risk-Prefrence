
import pygambit
import math

# Define the game
game = pygambit.Game.new_table([2, 2])
game.title = "Stag Hunt Game with Risk Aversion"

# Label players and strategies
game.players[0].label = "Player 1"
game.players[1].label = "Player 2"
game.players[0].strategies[0].label = "Stag"
game.players[0].strategies[1].label = "Hare"
game.players[1].strategies[0].label = "Stag"
game.players[1].strategies[1].label = "Hare"

# Assign payoffs
game[0, 0][game.players[0]] = 4  # Player 1 payoff for (Stag, Stag)
game[0, 0][game.players[1]] = 4  # Player 2 payoff for (Stag, Stag)
game[0, 1][game.players[0]] = 1  # Player 1 payoff for (Stag, Hare)
game[0, 1][game.players[1]] = 3  # Player 2 payoff for (Stag, Hare)
game[1, 0][game.players[0]] = 3  # Player 1 payoff for (Hare, Stag)
game[1, 0][game.players[1]] = 1  # Player 2 payoff for (Hare, Stag)
game[1, 1][game.players[0]] = 2  # Player 1 payoff for (Hare, Hare)
game[1, 1][game.players[1]] = 2  # Player 2 payoff for (Hare, Hare)

# Define a utility function for risk aversion
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

# Transform monetary payoffs into utilities
risk_aversion_param = 0.5
for outcome in game.contingencies:
    for player in game.players:
        original_payoff = game[outcome][player]
        game[outcome][player] = utility(original_payoff, risk_aversion_param)

# Solve for Nash equilibria
print("Nash Equilibria (Pure Strategies):")
pure_result = pygambit.nash.enumpure_solve(game)  # Get pure strategy results

# Access equilibria using the appropriate attribute or method
if hasattr(pure_result, "equilibria") and pure_result.equilibria:
    for eq in pure_result.equilibria:
        print(eq)
else:
    print("No pure strategy Nash equilibria found.")

print("\nNash Equilibria (Mixed Strategies):")
mixed_result = pygambit.nash.enummixed_solve(game)  # Get mixed strategy results

if hasattr(mixed_result, "equilibria") and mixed_result.equilibria:
    for eq in mixed_result.equilibria:
        for player in game.players:
            probabilities = [eq[player][strategy] for strategy in player.strategies]
            strategy_labels = [strategy.label for strategy in player.strategies]
            print(f"{player.label}: {dict(zip(strategy_labels, probabilities))}")
else:
    print("No mixed strategy Nash equilibria found.")
