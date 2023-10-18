import sqlite3

def getConnection():
    connection = sqlite3.connect("northwind.db")
    return connection

def getCustomerData():
    con = getConnection()
    cursor = con.cursor()
    params = ('Germany', )
    sqlStatement = "select CustomerID, CompanyName, Address, City " \
               "from Customers " \
               "where Country = ?"
    cursor.execute(sqlStatement, params) 
    datalist = cursor.fetchall()

    con.close();

    return datalist

dataset = getCustomerData()

for row in dataset:
    print (row)
