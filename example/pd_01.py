import pandas as pd
import numpy as np

msg = "=" * 35 + ' Start ' + '=' *35
print(msg)

dt = {
    'id': 'string',
    'class': 'string',
    'value': 'int'
}

data = [
    ('a1', 'A', 2),
    ('a1', 'A', 3),
    ('b1', 'B', -1),
]

df = pd.DataFrame(data, columns=[*dt])
df = df.astype(dt)
# df.set_index(['id'], inplace=True) # index is not necessarily unique

print(df, "\n")

# print([*df.columns] )

# sample = df.iat[0,1]
# print(type(sample))
# print(sample)
# a = list(map(lambda x : x.name, df.dtypes.items()))
# print(a)

arr = df.to_numpy()
print(arr)


print('='*len(msg))