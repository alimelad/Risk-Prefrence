# Stag Hunt Game with Risk Aversion

## **Overview**

This project implements a Stag Hunt game with modifications to account for player risk aversion. The implementation includes a utility transformation step to study how risk aversion affects strategic behavior and Nash equilibria.

### **Setup Methodology**

1. **Strategic-Form Game Creation**:
   - Two players with two strategies each: `"Stag"` and `"Hare"`.
   - Monetary payoffs represent the benefits of cooperation (`"Stag"`) versus individual safety (`"Hare"`).

2. **Utility Transformation**:
   - Payoffs are transformed into utility values using an exponential utility function to model risk aversion.
   - A tunable risk-aversion parameter allows experimentation with different levels of player risk aversion.

3. **Nash Equilibria Analysis**:
   - Solves for both pure and mixed strategy Nash equilibria.
   - Explores how risk preferences affect equilibrium outcomes.

---

### 1. **Risk Aversion Transformation**
**Description**: Applies risk aversion to the payoffs of a Stag Hunt game using a customizable utility function.
- **Features**:
  - Supports variable risk aversion parameters.
  - Transforms payoffs to utility values based on the exponential utility function.
  - Handles both positive and zero payoffs.
- **Code**:
  - Defines a `utility` function that computes utility values from raw payoffs using a risk aversion coefficient.
  - Transforms all payoffs in the game using the `utility` function.

---

### 2. **Game Definition**
**Description**: Models a two-player Stag Hunt game with defined strategies and payoffs.
- **Features**:
  - Two players with strategies `"Stag"` and `"Hare"`.
  - Payoffs are defined based on the standard Stag Hunt payoff matrix.
  - Players' labels and strategies are clearly set for interpretability.
- **Code**:
  - `pygambit.Game.new_table`: Initializes a new game in normal form.
  - Player and strategy labels are assigned using `game.players` and `game.players[i].strategies`.

---

### 3. **Nash Equilibria Computation**
**Description**: Computes pure and mixed strategy Nash equilibria for the game.
- **Features**:
  - Uses the Gambit library to compute both pure and mixed strategy equilibria.
  - Outputs probabilities for each player's strategies in mixed equilibria.
  - Identifies all equilibria, including deterministic (pure) and probabilistic (mixed).
- **Code**:
  - `pygambit.nash.enumpure_solve`: Computes pure strategy Nash equilibria.
  - `pygambit.nash.enummixed_solve`: Computes mixed strategy Nash equilibria.
  - Iterates over equilibria and prints probabilities for each strategy.

---

### 4. **Behavioral Rules**
**Description**: Incorporates behavioral rules through risk aversion.
- **Features**:
  - Risk aversion transforms players' payoffs, altering equilibrium outcomes.
  - Utility values reflect aversion to risk, changing the strategy dynamics.
- **Code**:
  - `utility`: Implements exponential risk aversion transformation.
  - All payoffs in the game are replaced with their utility equivalents.

---

### 5. **Game Details**
**Description**: Simulates a standard Stag Hunt game with modifications for risk preference.
- **Features**:
  - Models player decisions based on transformed utility values.
  - Computes equilibria to analyze strategy adjustments under risk aversion.
- **Code**:
  - `pygambit.Game.new_table`: Constructs the game matrix.
  - Payoff transformations and Nash equilibria computations integrated.

---

## **How to Run the Project**
1. **Install Dependencies**
   Install the required Python packages:
   pip install pygambit


