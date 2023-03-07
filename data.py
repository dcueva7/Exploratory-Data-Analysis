# %%
import pandas as pd
import seaborn as sns
from pygments import highlight

file_name = r"C:\Users\dcueva\projects\Pandas\Exploratory-Data-Analysis\bitcoin.csv"
sns.set_style("darkgrid")

# ~~~~~Data Prep and Cleaning~~~~~~~
# Load file using Pandas
# Discover File
# Fix any incorrect/missing values

df = pd.read_csv(file_name)

#Data Frame Columns: Timestamp, Open, High, Low, Close, Volume (BTC), Volume (Currency), Weighted Price

# print(df.describe())

#Questions:
# 1. What time of the day did most transcations occur?
# 2. What were the average opening, closing, highs, and lows each year?
# 3. Which year had the most volume?
# 4. Monthly volume trends?

#plot percentage of missing values per column
percentage = (df.isna().sum().sort_values(ascending=False) / len(df))*100

# percentage[percentage != 0].plot(kind='barh')


#drop rows with at least one missing value
df = df.dropna()

#convert timestamp from unix to datetime
df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='s')


## Exploratory Analysis and Visualization (columns to analyze)
# 1. High 
# 2. Low 
# 3. Volume (BTC)
# 4. Open

#get series for average high per month
average_high_month = df.groupby(pd.PeriodIndex(df['Timestamp'], freq= "M"))['High'].mean()

#get series for average high per year
average_high_year = df.groupby(pd.PeriodIndex(df['Timestamp'], freq= "Y"))['High'].mean()

#get series for volume per month
volume_per_month = df.groupby(pd.PeriodIndex(df['Timestamp'], freq='M'))['Volume_(BTC)'].mean()

average_high_month.plot()

average_high_year.plot()

volume_per_month.plot()

# %%
