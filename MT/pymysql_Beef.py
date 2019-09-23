import pymysql

# GANITO LANG MAGCONNECT SA MYSQL
# eto ung argument: ("localhost", "user", "password", "database_name")
conn = pymysql.connect("localhost", "root", "", "meat_prices")
cursor = conn.cursor()

# ITO SA CHICKEN TABLE YAN
query = "SELECT * FROM beef"
cursor.execute(query) # I EEXECUTE NYA UNG COMMAND NA GUSTO MO GALING SA query
results = cursor.fetchall() # KUKUNIN NYA LAHAT DATA SA PORK TABLE
# ITO EXAMPLE OUTPUT
# (("beef_type1", 25.3), ("beef_type2", 54.2))
# NAKA TUPLE SYA
print("PORK_PRICE DATA")
print("\n(<beef_type>, <float_price_value>, <int_quantity_value>)\n")
for result in results:
    print(result)
input("") # WAIT KEY
