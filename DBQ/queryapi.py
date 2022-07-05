import sqlite3 as sql
import numpy as np
import pandas as pd

class QueryAPI():
    SERVER_DIR = "C:\\Users\mwfre\OneDrive\\Desktop\\_GitHub\\Akatsuki\\DBQ\\server\\"
    # DB list
    DB_LIST = [ "MAIN.db", "BACKUP.db", "ADHOC.db" ]
    
    def __init__(self, db_name) -> None:

        if db_name not in self.DB_LIST:
            raise Exception(f"{db_name} is not a recognized db.")             

        self.conn = sql.connect(self.SERVER_DIR + db_name)
        self.cursor = self.conn.cursor()

    def type_map(self, dt: str, py_to_sql=True) -> str:

        if py_to_sql:           
            if dt.startswith('float'):
                ret = 'REAL'
            elif dt.startswith('int'):
                ret = 'INTEGER'
            else:
                ret = 'TEXT'
        else:
            if dt == 'TEXT':
                ret = 'string'
            elif dt == "INTEGER":
                ret = 'int'
            elif dt == "REAL":
                ret = 'float'                                 
            else:
                ret = None                

        return ret                                    


    def upload_df(self, df, table: str) -> None:

        # Create table if not exists; A bit redundant...and ugly
        header = df.dtypes.to_dict()
        num_cols = len(header)
        header = [ "{} {}".format(x, self.type_map(str(header[x]))) for x in header]
        header = ", ".join(header)
        
        query = f"Create Table If Not Exists {table} ({header})"
        self.cursor.execute(query)

        # upload the data
        query = ['?']*num_cols
        query = ', '.join(query)
        query = f"Insert Into {table} Values ({query})"
        self.cursor.executemany(query, df.to_numpy())

        self.conn.commit()


    def fetch_df(self, table):                    

        # collecting table info            
        info = self.get_table_info(table)
        cols = [ x[1] for x in info ]
        dts = [ self.type_map( x[2], False) for x in info ]            

        # fetching data
        query = f"Select * From {table}"
        self.cursor.execute(query)
        df = self.cursor.fetchall()                
        
        # parse to DataFrame
        df = pd.DataFrame(df, columns=cols)
        df = df.astype(dict(zip(cols, dts)))
        
        return df


    def get_table_info(self, table):

        query = f"PRAGMA table_info( {table} )"
        self.cursor.execute(query)
        return self.cursor.fetchall()



