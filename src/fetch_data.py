import yfinance as yf

def fetch_data(ticker, start_date, end_date):
    data = yf.download(
            ticker, 
            start=start_date.strftime('%Y-%m-%d'), 
            end=end_date.strftime('%Y-%m-%d'),
        )
    return data