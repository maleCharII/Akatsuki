import sqlite3 as sql

conn = sql.connect("C:\\Users\mwfre\OneDrive\\Desktop\\_GitHub\\Akatsuki\\dummy\\dummy.db")
cursor = conn.cursor() # generate an cursor

# sql statement
query = '''
    Create Table If Not Exists
    adhoc
    ( Key TEXT, Value REAL )
'''
cursor.execute(query)

# query = '''
#     Insert Into adhoc Values ('a1', 100)
# '''

# cursor.execute(query)

query = '''
    Select * From adhoc
'''

cursor.execute(query)

data = cursor.fetchall()
print(data)

conn.commit()
conn.close()