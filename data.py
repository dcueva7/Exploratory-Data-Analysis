import pandas as pd

file_name = r"C:\Users\dcueva\projects\Pandas\Exploratory-Data-Analysis\bitcoin.csv"

# ~~~~~Data Prep and Cleaning~~~~~~~
# Load file using Pandas
# Discover File
# Fix any incorrect/missing values

df = pd.read_csv(file_name)

print(df)
