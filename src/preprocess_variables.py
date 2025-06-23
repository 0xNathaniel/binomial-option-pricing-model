import os
import numpy as np
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta

# Fungsi untuk fetch data harga saham

def fetch_data(ticker, start_date, end_date):
    data = yf.download(
        ticker,
        start=start_date.strftime('%Y-%m-%d'),
        end=end_date.strftime('%Y-%m-%d'),
    )
    return data

# Choice of Equity, Historical Data Length, and RFF

TICKERS         = ["TSLA", "AAPL"]          # Desired equity options
HISTORY_DAYS    = 175                       # 27 Jun 2025 to 19 Dec 2025
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
        
        if data.empty or "Close" not in data.columns:
            print(f"No valid data for {ticker}. Skipping...")
            continue
        
        close_prices = data["Close"].dropna()
        
        # Check if we have enough data points
        if len(close_prices) < 2:
            print(f"Insufficient data for {ticker} (only {len(close_prices)} data points). Skipping...")
            continue

        # Spot Price (S_0)
        spot_price = float(close_prices.iloc[-1])

        # Log Return: rt = ln(P_t / P_t-1)
        log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
        if len(log_returns) < 2:
            print(f"Insufficient log returns for {ticker}. Skipping...")
            continue

        # Volatility: std(log return) × sqrt(252) (Annualized Historical Volatility)
        volatility = float(log_returns.std() * np.sqrt(252))

        # Calculate dividend yield
        ticker_obj = yf.Ticker(ticker)
        dividends = ticker_obj.dividends
        if dividends.empty:
            dividend_yield = 0.00
        else:
            div_index = dividends.index.tz_localize(None)
            recent_div = dividends[div_index > (END_DATE - timedelta(days=365))]
            annual_div = recent_div.sum()
            dividend_yield = annual_div / spot_price if spot_price > 0 else 0.00

        df = pd.DataFrame([{
            "ticker": ticker,
            "spot_price": spot_price,
            "volatility": volatility,
            "risk_free_rate": RISK_FREE_RATE,
            "dividend_yield": dividend_yield
        }])

        df.to_csv(f"{OUTPUT_DIR}/variables_{ticker}.csv", index=False)
        print(f"[{ticker}] Spot: {spot_price:.2f}, Vol: {volatility:.4f}, Dividend Yield: {dividend_yield:.4f}")

    except Exception as e:
        print(f"Error processing {ticker}: {e}")
        continue
