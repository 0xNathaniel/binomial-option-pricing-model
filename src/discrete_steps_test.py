from binomial_model import binomial_american_call

# Variables for Modeling (AAPL Case)

SPOT_PRICE      = 201.3                 # Current spot price
STRIKE_PRICE    = 250                   # Desired stock option strike price
VOLATILITY      = 0.4126847810715328    # Utilize preprocessed variable calculation
RISK_FREE_RATE  = 0.04273               # Jun 24, 2025 US 3 Month Treasury Yield
T               = 175/365               # Desired time to maturity (in years)
DIVIDEND_YIELD  = 0.005017384626591532  # Dividend yield
N = [10, 100, 1000]                     # List of tested N

# Premium price as of 23 June 2025 is $2.65 (market reference)

if __name__ == "__main__":
    for n in N:
        # Call the function and print results
        print(f"Number of discrete steps (N): {n}")
        result = binomial_american_call(
            SPOT_PRICE, STRIKE_PRICE, VOLATILITY, RISK_FREE_RATE, T, n, DIVIDEND_YIELD)
        european_price, american_price, early_ex_val, exercise_map = result
        print(f"European Call Option Price: {european_price:.4f}")
        print(f"American Call Option Price: {american_price:.4f}")
        print(f"Difference (Early Exercise Value): {early_ex_val:.4f}\n")