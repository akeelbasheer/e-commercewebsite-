import sqlite3
import db_init, select_all


def delete_product_by_id(conn, id):
    
    cur = conn.cursor()
    cur.execute("DELETE FROM products WHERE id=?", (id,))
    
    conn.commit()
        
#execute all functions
if __name__ == '__main__':
    id = input('delete product id: ')  
    conn = db_init.create_connection()
    delete_product_by_id(conn,id)
    select_all.select_all_products(conn)
