import pandas as pd
import numpy as np

msg = "=" * 35 + ' Start ' + '=' *35
print(msg)

schema = {
    'id': 'string',
    'class': 'string',
    'value': np.float16
}

data = [
    ('a1', 'A', 2),
    ('a1', 'A', 3),
    ('b1', 'B', -1),
]

df = pd.DataFrame(data, columns=[*schema])
df = df.astype(schema)
# df.set_index(['id'], inplace=True) # index is not necessarily unique

print(df, "\n")
print(df.dtypes, "\n")
print([*df.columns] )

sample = df.iat[0,1]
print(type(sample))
print(sample)

print('='*len(msg))