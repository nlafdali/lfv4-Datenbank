import sqlite3;

connection = sqlite3.connect("northwind.de");

cursor = connection.cursor();

# Selectstatement
country = ("Germany",);
sqlStatement = "select CustomerID, CompanyName, Address, City " \
               "from Customers" \
               #"where Contry = '" +country + "'";
               "where Contry = ?";


cursor.execute(sqlStatement, country ); # schickt Selectstatement an DB

for dataset in cursor:
    print("Kunden-Nr.: ", dataset[0]);
    print("Kunde: ", dataset[1]);
    print("Straße: ", dataset[2]);
    print("Stadt: ", dataset[3]);

Connection.close();
