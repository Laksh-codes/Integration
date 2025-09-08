import mysql.connector
from contract import dictonary
class save_to_db:
    def __init__(self, dictonary):
        self.dict = dictonary
        self.conn = mysql.connector.connect(
            host = 'q',
            user = 'r',
            password = 'w'
        )        
        if self.conn.is_connected():
            print("Connected to MySQL server")
        self.cursor = self.conn.cursor()

    def create_db(self, db_name):
        self.cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        print("Database Created.")
        self.conn.database = db_name
        print("Database Selected.")
    
    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Contract(
                a INTEGER PRIMARY KEY,
                b TEXT,
                c TEXT,
                d TEXT,
                e TEXT,
                f TEXT,
                g TEXT,
                h TEXT,
                i TEXT
                            )
        """)
        print("Table Ready.")
    def drop_table(self):
        self.cursor.execute('''DROP TABLE Contract''')
        self.conn.commit()
        self.conn.close()
        print("Database Dropped.")
    def insert_values(self):
        """Insert multiple rows into the table"""
        sql ="""
            INSERT IGNORE INTO Contract () VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for i in range(1, len(self.values), 200):
            batch = self.values[i:i+200]
            self.cursor.executemany(sql, batch)
            self.conn.commit()
            print(f"Inserted batch {i//200 + 1}")
        self.conn.commit()
        self.conn.close()

    def extract_values(self):
        self.values = []
        for i, (key, value) in enumerate(self.dict.items()):
            if i == 0:
                continue

            self.values.append()
            print(self.values)
        return self.values
    def update_data(self):
        self.cursor.execute("""UPDATE Contract SET '""")
        self.conn.commit()
        self.conn.close()
obj = save_to_db(dictonary)
obj.create_db("ContractDB")
obj.create_table()
obj.extract_values()
obj.insert_values()
# obj.update_data()
# obj.drop_table()
