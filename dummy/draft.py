import pandas as pd

data = [
    ('a1', 'A', 1), 
    ('a2', 'A', 3), 
    ('b1', 'B', 3), 
]

df = pd.DataFrame(data, columns=['Key', 'Class', 'Value'])
print(df)

print(df.columns.values)
