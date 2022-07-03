import sqlite3 as sql

print('='*35, 'Start', '='*35)

# in memory setup
print(">> Connecting ...")

db_file = ":memory:"
conn = sql.connect(db_file)
cursor = conn.cursor()

print(">> Create Table")
query = """
    Create Table If Not Exists dummy_01 (
        id TEXT Primary KEY,
        class TEXT Not NULL,
        value REAL Not NULL
    )
"""
cursor.execute(query)

print(">> Insert Data")
data = [
    ('a1', 'A', 1),
    ('a2', 'A', 2),
    ('b1', 'B', 3)
]

query = """
    Insert Into dummy_01 Values (?, ?, ?)
"""
cursor.executemany(query, data)

print(">> Fetch Data")

query = """
    Select * From dummy_01
"""
cursor.execute(query)

out = cursor.fetchall()
print(out)

conn.commit()
conn.close()

print('='*78)