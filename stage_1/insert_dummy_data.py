import sqlite3
import db_init

def insert_dummy_data(conn):
    cur = conn.cursor()

    #records or rows in a list
    records = [(1, 'chair', 100, 'living room chairs', "1.jpg"),
		        (2, 'table', 200, 'living room table', "2.jpg")
			    ]

    #insert multiple records in a single query
    cur.executemany('INSERT INTO products VALUES(?,?,?,?,?);',records);

    print('We have inserted', cur.rowcount, 'records to the table.')

    #commit the changes to db			
    conn.commit()
    #close the connection
    conn.close()

#execute all functions
if __name__ == '__main__':  
    conn = db_init.create_connection()
    insert_dummy_data(conn) 
  
    
