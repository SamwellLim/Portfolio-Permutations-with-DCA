import yfinance as yf
import pandas as pd

# List of stock tickers
tickers = ['NVDL', 'BITX', 'BITO', 'FNGU', 'UPRO', 'SPMO', 'BULZ', 'TQQQ', 'SMH', 'XMMO', 'EPI', 'QDV5']

# List to hold dataframes
dataframes = []

# Fetch data for each ticker
for ticker in tickers:
    print(f"Downloading data for {ticker}...")
    data = yf.download(ticker, start="2024-01-01", end="2024-07-01")
    dataframes.append(data)  # Append the dataframe to the list

# Access and print the first few rows of the Apple stock data
print("Displaying data for AAPL:")
print(dataframes[0].head())