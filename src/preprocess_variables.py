import os
import yfinance as yf
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

TICKERS = ["TSLA"]
HISTORY_DAYS = 180
RISK_FREE_RATE = 0.05

END_DATE = datetime.today()
START_DATE = END_DATE - timedelta(days=HISTORY_DAYS)

OUTPUT_DIR = "output"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for ticker in TICKERS:
    data = yf.download(ticker, start=START_DATE.strftime('%Y-%m-%d'), end=END_DATE.strftime('%Y-%m-%d'))
    close_prices = data["Close"].dropna()
    spot_price = close_prices.iloc[-1]
    log_returns = np.log(close_prices / close_prices.shift(1)).dropna()
    volatility = log_returns.std() * np.sqrt(252)

    df = pd.DataFrame([{
        "ticker": ticker,
        "spot_price": spot_price,
        "volatility": volatility,
        "risk_free_rate": RISK_FREE_RATE
    }])

    df.to_csv(f"{OUTPUT_DIR}/variables_{ticker}.csv", index=False)
