import pymysql

# SA BEEF TABLE, GANITO MAGINSERT NG VALUE SA TABLE

# GANITO LANG MAGCONNECT SA MYSQL
# eto ung argument: ("localhost", "user", "password", "database_name")
conn = pymysql.connect("localhost", "root", "", "meat_prices")
cursor = conn.cursor()

beef_type = str(input("BEEF TYPE: ")) # STR
beef_price = float(input("BEEF PRICE: ")) # FLOAT
beef_quantity = int(input("BEEF QUANTITY: ")) # INTEGER

# ITO SA BEEF TABLE YAN
# DAPAT MAY \" \" KAPAG VARCHAR UNG DATA TYPE NG COLUMN
# DITO SA CASE NA TO, UNG BEEF_TYPE AY VARCHAR, SO SA VALUES NAKA \" \" SYA
query = "INSERT INTO beef (beef_type, price, quantity) values (\"%s\", %f, %d)" %(beef_type, beef_price, beef_quantity)
cursor.execute(query) # I EEXECUTE NYA UNG COMMAND NA GUSTO MO GALING SA query
conn.commit() # ICOCOMMIT NYA NA SA DATABASE PARA MAY MAGBAGO
cursor.close() # CLOSE MO UNG CURSOR, DAPAT MERON YAN
input("VALUE ADDED!") # WAIT KEY
