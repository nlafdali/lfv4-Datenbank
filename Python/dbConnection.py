import sqlite3

def getConnection():
    connection = sqlite3.connect('northwind.db')
    return connection

def getCustomerData():
    con = getConnection()
    cursor = con.cursor()
    params = ('Germany', )
    sqlStatement = 'SELECT CustomerID, CompanyName, Address, City ' \
                'FROM Customers ' \
                'WHERE Country = ?'
    cursor.execute(sqlStatement, params)

    dataList = cursor.fetchall()

    con.close()

    return dataList

def getDataList(sql, params):
    con = getConnection()
    cursor = con.cursor()
    cursor.execute(sql, params)
    dataList = cursor.fetchall()
    con.close()
    return dataList


dataSet = getDataList()
for row in dataSet:
    print(row)
