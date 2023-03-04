import pandas as pd

file_name = r"C:\Users\dcueva\projects\Pandas\Exploratory-Data-Analysis\bitcoin.csv"

# ~~~~~Data Prep and Cleaning~~~~~~~
# Load file using Pandas
# Discover File
# Fix any incorrect/missing values

df = pd.read_csv(file_name)

#Data Frame Columns: Timestamp, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price

print(df[['High', 'Close']].describe())

#Questions:
# 1. What time of the day did most transcations occur?
# 2. What were the average opening, closing, highs, and lows each year?
# 3. Which year had the most volume?
# 4. Monthly volume trends?

