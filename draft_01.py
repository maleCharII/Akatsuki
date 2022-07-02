import pandas as pd
import datetime
from dateutil.parser import parse

print('\n', "-"*70, '\n')

path = "C:\\Users\\mwfre\\OneDrive\\Desktop\\"
name = "SPY.csv"

df = pd.read_csv(path + name, parse_dates=[0], index_col=[0])
df.index = df.index.date

sample = df.iloc[0].name
print(type(sample))
print(sample)

r = df.loc[sample]

print(r)

print('\n', "-"*70, '\n')