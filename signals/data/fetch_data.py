import yfinance as yf
import os

# Create a data folder if it doesn't exist
os.makedirs("../data", exist_ok=True)

# List of tickers you want to fetch
tickers = ["SPY", "QQQ", "AAPL", "VIX"]
start_date = "2018-01-01"
end_date = "2025-05-31"

for ticker in tickers:
    print(f"Downloading {ticker}...")
    df = yf.download(ticker, start=start_date, end=end_date)
    if not df.empty:
        df.to_csv(f"../data/{ticker.lower()}.csv")
        print(f"Saved {ticker.lower()}.csv")
    else:
        print(f"No data found for {ticker}")
