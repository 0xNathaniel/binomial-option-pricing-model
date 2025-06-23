import numpy as np
from visualization import plot_exercise_map

# Variables for Modeling (TSLA Case)

SPOT_PRICE      = 351.70     # S₀ = current spot price
STRIKE_PRICE    = 400        # K = strike price
VOLATILITY      = 0.7784     # σ = annualized historical volatility
RISK_FREE_RATE  = 0.04273    # r = risk-free rate
T               = 175/365    # T = time to maturity (in years)
N               = 100        # N = number of discrete steps
DIVIDEND_YIELD  = 0.0        # q = dividend yield

# Premium price as of 23 June 2025 is $45.30 (market reference)

def binomial_american_call(
    spot_price, strike_price, volatility, risk_free_rate, T, N, dividend_yield
):
    # Δt = T / N
    dt = T / N

    # u = e^{σ√Δt}, d = 1/u
    u = np.exp(volatility * np.sqrt(dt))
    d = 1 / u

    # p = (e^{(r - q)Δt} - d) / (u - d)
    p = (np.exp((risk_free_rate - dividend_yield) * dt) - d) / (u - d)

    # Build asset price tree: S_{i,j} = S₀ * u^j * d^{i-j}
    price_tree = np.zeros((N + 1, N + 1))
    for j in range(N + 1):
        price_tree[N, j] = spot_price * (u ** j) * (d ** (N - j))

    european = np.zeros_like(price_tree)
    american = np.zeros_like(price_tree)
    exercise_map = np.zeros_like(price_tree)

    # Terminal payoff: V_{N,j} = max(S_{N,j} - K, 0)
    for j in range(N + 1):
        european[N, j] = max(price_tree[N, j] - strike_price, 0)
        american[N, j] = european[N, j]

    # Backward induction:
    # V_{i,j} = e^{-rΔt} * (p * V_{i+1,j+1} + (1 - p) * V_{i+1,j})
    for i in range(N - 1, -1, -1):
        for j in range(i + 1):
            cont_val = np.exp(-risk_free_rate * dt) * (
                p * european[i + 1, j + 1] + (1 - p) * european[i + 1, j]
            )
            european[i, j] = cont_val

            cont_val_am = np.exp(-risk_free_rate * dt) * (
                p * american[i + 1, j + 1] + (1 - p) * american[i + 1, j]
            )
            early_ex = max(price_tree[i, j] - strike_price, 0)

            # American-style: V_{i,j} = max(payoff, continuation)
            american[i, j] = max(early_ex, cont_val_am)

            if early_ex > cont_val_am and early_ex > 0:
                exercise_map[i, j] = 1

    return european[0, 0], american[0, 0], american[0, 0] - european[0, 0], exercise_map

if __name__ == "__main__":
    # Call the function and print results
    result = binomial_american_call(
        SPOT_PRICE, STRIKE_PRICE, VOLATILITY,
        RISK_FREE_RATE, T, N, DIVIDEND_YIELD
    )
    european_price, american_price, early_ex_val, exercise_map = result

    print(f"European Call Option Price: {european_price:.4f}")
    print(f"American Call Option Price: {american_price:.4f}")
    print(f"Difference (Early Exercise Value): {early_ex_val:.4f}")

    print("\nGenerating early exercise visualization...")
    plot_exercise_map(exercise_map)
