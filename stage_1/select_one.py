import sqlite3
import db_init


def select_product_by_id(conn, id):
    
    cur = conn.cursor()
    cur.execute("SELECT * FROM products WHERE id=?", (id,))

    rows = cur.fetchall()

    for row in rows:
        print(row)
        
#execute all functions
if __name__ == '__main__':
    id = input('choose product id: ')  
    conn = db_init.create_connection()
    select_product_by_id(conn,id)

