import sqlite3
import db_init
import select_all
from shutil import copyfile


#/home/user/Downloads/johann-siemens-EPy0gBJzzZU-unsplash.jpg


        
#The functions to insert the product / create product

def create_product(conn, product):
    
    sql = ''' INSERT INTO products (name, price, descriptiom, image)
              VALUES(?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql, product)
    conn.commit()
    
    
        
    return cur.lastrowid
    



#execute all functions
if __name__ == '__main__':


    name = input("Please enter a name :\n")
    price = input("Please enter a price :\n")
    description = input("Please enter a description :\n")
    image = input("Please enter a imagepath :\n")

    product = (name, price, description, image)  
    
    conn = db_init.create_connection()
    id = create_product(conn,product)

    des =  "/home/user/Documents/Python_projects/E-Commerce/stage_1/"+str(id)+".jpg"
       
    copyfile(image, des)
    
    select_all.select_all_products(conn)
      
        
        
