import sqlite3
import db_init
import select_all
from shutil import copyfile


#/home/user/Downloads/johann-siemens-EPy0gBJzzZU-unsplash.jpg


        
#The functions to insert the product / create product

def update_product(conn, product):

    sql = ''' UPDATE products
              SET name = ? ,
                  price = ? ,
                  descriptiom = ? , 
                  image = ? 
              WHERE id = ?'''
    
    cur = conn.cursor()
    cur.execute(sql, product)
    conn.commit()

    



#execute all functions
if __name__ == '__main__':
    id = input('update product id: ')  

    name = input("Please enter a name :\n")
    price = input("Please enter a price :\n")
    description = input("Please enter a description :\n")
    image = input("Please enter a imagepath :\n")

    des =  "/home/user/Documents/Python_projects/E-Commerce/stage_1/"+str(id)+".jpg"
       
    #copy product image to folder   
    copyfile(image, des) 

    product = (name, price, description, image, id)  
    
    
    
    conn = db_init.create_connection()
    update_product(conn,product)


    
    select_all.select_all_products(conn)
      
        
        
