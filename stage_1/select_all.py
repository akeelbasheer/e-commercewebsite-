import sqlite3
import db_init

def select_all_products(conn):
    
    select_products = "SELECT * FROM products;"
    
    cur = conn.cursor()
    cur.execute(select_products)
    
    records = cur.fetchall()
    print("Total col are:  ", len(records))
    for col in records:
            print("Id: ", col[0])
            print("name: ", col[1]) 
            print("price: ", col[2])
            print("description: ", col[3]) 
            print("image: ", col[4])
            


#execute all functions
if __name__ == '__main__':     
    conn = db_init.create_connection()
    select_all_products(conn)

