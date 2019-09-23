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
# DITO SA CASE NA TO, UNG BEEF_TYPE AY VARCHAR, SO DAPAT NAKA \" \" SA LOOB NG STRING NA YAN
query = "UPDATE beef SET price = %f, quantity = %d WHERE beef_type = \"%s\"" %(beef_price, beef_quantity, beef_type)
cursor.execute(query) # I EEXECUTE NYA UNG COMMAND NA GUSTO MO GALING SA query
conn.commit() # ICOCOMMIT NYA NA SA DATABASE PARA MAY MAGBAGO
cursor.close() # CLOSE MO UNG CURSOR, DAPAT MERON YAN
input("VALUE UPDATED!") # WAIT KEY
