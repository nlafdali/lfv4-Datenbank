import sqlite3

def getConnection():
    connection = sqlite3.connect("northwind.db");
    return connection;

def getCustomerData():
    con = getConnection();
    cursor = con.cursor();
    params = ('Germany', );
    sqlStatement = "select CustomerID, CompanyName, Address, City " \
               "from Customers " \
               "where Country = ?"
    cursor.execute(sqlStatement, params);
    
    datalist = cursor.fetchall();

    con.close();

    return datalist;

def getDataList (sql, params = ()):
    con = getConnection ();
    cursor = con.cursor();
    cursor.execute(sql, params);
    datalist = cursor.fetchall();
    con.close();
    return datalist;

def executeQuery(sql, params = ()):
    con = getConnection();
    cursor = con.cursor();
    cursor.execute(sql, params);
    con.commit();
    con.close();

sqlStatement1 = "select FirstName, Lastname, Country from Employees " \
               "where Country = ?";

sqlStatement2 = "select * from Customers ";

params = ("UK", );
#dataset = getDataList (sqlStatement1, params);

dataset = getDataList (sqlStatement2);
for row in dataset:
    print (row)

