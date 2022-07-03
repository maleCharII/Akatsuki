import sqlite3 as sql

# in memory setup
db_name = ":memory:"
conn = sql.connect(db_name)
cursor = conn.cursor()
