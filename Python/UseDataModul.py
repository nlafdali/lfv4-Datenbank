import DataModul

"""
sqlStatement1 = "select FirstName, Lastname, Country from Employees " \
               "where Country = ?";

sqlStatement2 = "select * from Customers ";

params = ("UK", );
dataset = DataModul.getDataList(sqlStatement1, params);

"""
params = ('Nadusch', 'Nadia Fudies', 'Nadine Maroc');
sqlinsert = "insert into Customers (CustomerID, CompanyName, ContactName) "\
            "values (?,?,?)"

result = DataModul.getDataList(sqlinsert, params)

print(result)
