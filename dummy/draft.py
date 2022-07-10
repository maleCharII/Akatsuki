import pandas as pd

print("="*70)

header = {
    'key': 'string',
    'class': 'string',
    'value': 'float' 
}

data = [
    ('a1', 'A', 2 ),
    ('a2', 'A', 3 )
]

df = pd.DataFrame(data, columns=['key', 'class', 'value'])

print(df)
print(df.shape)

print(">> Appending ...")
df2 = pd.DataFrame(data, columns=[*header])
df2 = df2.astype(header)
adf = pd.concat([df, df2], ignore_index=True, axis=1)


print(">> info")
print(adf.dtypes)
print(">> table")
print(adf)
