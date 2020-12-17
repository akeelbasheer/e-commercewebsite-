import sqlite3

#connect to database
def create_db():

    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        #this line will create a ecommerce.db file in this folder
        #Then it will create conn varable with a connection to the DB
        sqlite3.connect("ecommerce.db")
        
    except Error as e:
        print(e)

    


#connect to database
def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect("ecommerce.db")
        return conn
    except Error as e:
        print(e)

    return conn
    


#The functions to create the table
def create_table(conn):
    
    #The SQL neccessary to create the table
    sql = '''CREATE TABLE IF NOT EXISTS products (
	    id integer PRIMARY KEY,
	    name text NOT NULL,
	    price integer NOT NULL,
	    descriptiom text NOT NULL,
        image text NOT NULL
	    
    );'''    
    
    try:
        c = conn.cursor()
        c.execute(sql)
    except Error as e:
        print(e)
     
     
#execute all functions
if __name__ == '__main__':     
    create_db()
    conn = create_connection()       
    create_table(conn)
    
