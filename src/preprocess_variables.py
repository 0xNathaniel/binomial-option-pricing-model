import os
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

from fetch_data import fetch_data

# Choice of Equity, Historical Data Length, and RFF

TICKERS         = ["TSLA", "AAPL", "MSFT"]  # Desired equity options
HISTORY_DAYS    = 180       
RISK_FREE_RATE  = 0.04273                   # Jun 24, 2025 US 3 Month Treasury Yield

END_DATE = datetime.today()
START_DATE = END_DATE - timedelta(days=HISTORY_DAYS)

OUTPUT_DIR = "../data/variables_output" # Executed within the src folder
os.makedirs(OUTPUT_DIR, exist_ok=True)

for ticker in TICKERS:
    print(f"Attempting to download data for {ticker} from {START_DATE.strftime('%Y-%m-%d')} to {END_DATE.strftime('%Y-%m-%d')}")
    
    try:
        # Try downloading with basic parameters
        data = fetch_data(ticker, START_DATE, END_DATE)
        
        print(f"Downloaded data shape: {data.shape}")
        print(f"Columns: {list(data.columns)}")
        
        # Check if data was downloaded successfully
        if data.empty:
            print(f"No data found for {ticker}. Trying alternative approach...")
            
        if data.empty or "Close" not in data.columns:
            print(f"Still no valid data found for {ticker}. Skipping...")
            continue
            
        close_prices = data["Close"].dropna()
        
        # Check if we have enough data points
        if len(close_prices) < 2:
            print(f"Insufficient data for {ticker} (only {len(close_prices)} data points). Skipping...")
            continue

        # Spot Price (S_0)
        spot_price = close_prices.iloc[-1]

        # Log Return: rt = ln(P_t / P_t-1)
        log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
        
        # Check if we have enough log returns for volatility calculation
        if len(log_returns) < 2:
            print(f"Insufficient data for volatility calculation for {ticker}. Skipping...")
            continue

        # Volatility: std(log return) × sqrt(252) (Annualized Historical Volatility)
        volatility = log_returns.std() * np.sqrt(252)

        df = pd.DataFrame([{
            "ticker": ticker,
            "spot_price": spot_price,
            "volatility": volatility,
            "risk_free_rate": RISK_FREE_RATE
        }])

        df.to_csv(f"{OUTPUT_DIR}/variables_{ticker}.csv", index=False)
        print(f"Successfully processed {ticker}: Spot Price = {spot_price:.2f}, Volatility = {volatility:.4f}")
        
    except Exception as e:
        print(f"Error processing {ticker}: {e}")
        continue
