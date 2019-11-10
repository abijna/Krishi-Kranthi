import csv, sqlite3
con = sqlite3.connect("Shehack.sqlite3")

def create_table_farmer():

	cur = con.cursor()
	cur.execute("CREATE TABLE Farmers (FarmerId, FarmerName, Latitude, Longitude, LandArea, FarmerRating);") # use your column names here

	with open('Farmer.csv','r') as fin: # `with` statement available in 2.5+
	    # csv.DictReader uses first line in file for column headings by default
	    dr = csv.DictReader(fin) # comma is default delimiter
	    to_db = [(i['FarmerId'], i['FarmerName'], i['Latitude'], i['Longitude'], i['LandArea'], i['FarmerRating']) for i in dr]

	cur.executemany("INSERT INTO Farmers (FarmerId, FarmerName, Latitude, Longitude, LandArea, FarmerRating) VALUES (?,?,?,?,?,?);", to_db)
	con.commit()


def create_table_product():

	cur = con.cursor()
	cur.execute("CREATE TABLE Product (FarmerId, ProductId, ProductName, Price, RemainingQuantity, SoldQuantity, ExpiryDate, Description, Rating);") # use your column names here

	with open('Product.csv','r') as fin: # `with` statement available in 2.5+
	    # csv.DictReader uses first line in file for column headings by default
	    dr = csv.DictReader(fin) # comma is default delimiter
	    to_db = [(i['FarmerId'], i['ProductName'], i['ProductId'], i['Price'], i['RemainingQuantity'], i['SoldQuantity'], i['ExpiryDate'],i['Description'],i['Rating']) for i in dr]

	cur.executemany("INSERT INTO Product (FarmerId, ProductId, ProductName, Price, RemainingQuantity, SoldQuantity, ExpiryDate,Description, Rating) VALUES (?,?,?,?,?,?,?,?,?);", to_db)
	con.commit()

def create_table_transaction():
	cur = con.cursor()
	cur.execute("CREATE TABLE Transaction (TransactionId, ProductId, Quantity, OrderTimestamp);")
	con.commit()



def sql_fetch_farmer(con):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM Farmers')
	rows = cursorObj.fetchall()
	print("Farmer Details-----")
	for row in rows:
		print(row)
	con.commit()

def sql_fetch_product(con):
	cursorObj = con.cursor()
	cursorObj.execute('SELECT * FROM Product')
	rows = cursorObj.fetchall()
	print("Product Details------")
	for row in rows:
		print(row)
	con.commit()

#create tables
create_table_farmer()
create_table_product()
#create_table_transaction()

#show tables
sql_fetch_farmer(con)
sql_fetch_product(con)

con.close()
