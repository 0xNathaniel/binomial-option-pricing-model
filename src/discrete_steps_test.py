from binomial_model import binomial_american_call
from visualization import plot_european_price_vs_n

# Variables for Modeling (AAPL Case)

SPOT_PRICE      = 201.425               # Current spot price
STRIKE_PRICE    = 250                   # Desired stock option strike price
VOLATILITY      = 0.4110088081144711    # Utilize preprocessed variable calculation
RISK_FREE_RATE  = 0.04273               # Jun 24, 2025 US 3 Month Treasury Yield
T               = 178/365               # Desired time to maturity (in years)
DIVIDEND_YIELD  = 0.005012406947890819  # Dividend yield
N               = [10,                  # List of tested N
                   50,
                   100,
                   250,
                   500, 
                   1000,
                   2500,
                   5000]       

# Premium price as of 23 June 2025 is $2.65 (market reference)

if __name__ == "__main__":
    european_prices = []
    for n in N:
        print(f"Number of discrete steps (N): {n}")
        result = binomial_american_call(
            SPOT_PRICE, STRIKE_PRICE, VOLATILITY, RISK_FREE_RATE, T, n, DIVIDEND_YIELD)
        european_price, american_price, early_ex_val, exercise_map = result
        european_prices.append(european_price)
        print(f"European Call Option Price: {european_price:.4f}")
        print(f"Difference (Early Exercise Value): {early_ex_val:.4f}\n")
    # Visualize plot
    plot_european_price_vs_n(N, european_prices, save_path="../data/visualization_output/visualization_AAPL.png")