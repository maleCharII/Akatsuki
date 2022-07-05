import sys
sys.path.insert(0, "c:\\Users\\mwfre\\OneDrive\\Desktop\\_GitHub\\Akatsuki")

import pandas as pd
from dbq.queryapi import QueryAPI

msg = '='*35 + ' example: dbq_01 '+ '='*35
print(msg)

print('>> write up a sample dataframe')
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


try:
    api = QueryAPI("ADHOC.db")

    print('>> upload a df')
    table = 'dummy_01'
    query = f"Drop Table If Exists {table}"
    api.cursor.execute(query)
    api.conn.commit()

    api.upload_df(df, table)

    print('>> get table info')
    info = api.get_table_info(table)
    print(info)

    print('>> get table as a df')
    df = api.fetch_df(table)
    print(df)
    
except Exception as e:
    print(e.args)
finally:
    api.conn.close()    


print( '='*len(msg) )