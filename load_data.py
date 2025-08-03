import pandas as pd 

df_prices = pd.read_csv("data/historical_stock_prices.csv")
df_stocks = pd.read_csv("data/historical_stocks.csv")

# keeping 3 cols
df_prices = df_prices[['date', 'ticker', 'adj_close']]
df_prices = df_prices.pivot(index='date', columns='ticker', values='adj_close')

# data cleaning and choosing two tickers

list_of_stock = ['KO', 'PEP'] # can change for any two similar stocks

pair_df = df_prices[list_of_stock].dropna()

pair_df.to_csv("data/pair_ko_pep.csv")