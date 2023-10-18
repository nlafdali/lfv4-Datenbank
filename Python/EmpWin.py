import tkinter as tk;
from tkinter import ttk;
import DataModul;

EmpWin = tk.Tk();

#fenster initialisieren
EmpWin.title("Mitarbeiter");
EmpWin.geometry("300x350");
EmpWin.resizable(False, False);

employeeID = 0;

def getDropdownList():
    sql = "select LastName from Employees";
    list = DataModul.getDataList(sql);
    return list;

def clickSaveButton():
    fname = txtFName.get();
    lname = txtLName.get();
    bday = txtBDay.get();
    sql = "update Employees set FirstName = ?, " \
          "LastName = ?, BirthDate =? where EmployeeID =? " ;
    global employeeID;
    params =(fname, lname, bday, employeeID);
    print(params);
    DataModul.executeQuery(sql, params);
    global cmbEmployees
    cmbEmployees["values"] = getDropdownList();
    cmbEmployees.set("");
    clearForm();
    
def selectEmployee(event):
    emp = cmbEmployees.get();
    clearForm();
    fillForm(emp);

def fillForm(empLastName):

    sql = "select EmployeeID, FirstName, LastName, BirthDate "\
           "from Employees where LastName =?";

     #params[0] = empLastName;
     
    list = DataModul.getDataList(sql, (empLastName, ));

    global employeeID;

    employeeID = list[0][0];
    txtFName.insert(0, list[0][1]);
    txtLName.insert(0, list[0][2]);
    txtBDay.insert(0, list[0][3]);

def clearForm():
    global employeeID;
    employeeID=0;
    txtFName.delete(0, 'end');
    txtLName.delete(0, 'end');
    txtBDay.delete(0, 'end');
def newEmp():
    global btnUpdate;
    btnUpdate.place_forget();
    clearForm();
    global btnInsert;
    btnInsert.place(x=200, y=130, width=80);

def clickInsertButton():
    fname = txtFName.get();
    lname = txtLName.get();
    bday = txtBDay.get();
    sql = "insert into Employees (FirstName, LastName, BirthDate) " \
              "values (?, ?, ?) n   "
    params =(fname, lname, bday, employeeID);
    DataModul.executeQuery(sql, params);
    global btnInsert;
    btnInsert;.place_forget();
    
# Menu initialisieren

menuBar = tk.Menu(EmpWin);
EmpWin.config(menu=menuBar);
fileMen = tk.Menu(menuBar);
menuBar.add_cascade(label="Datei", menu=fileMen);
#fileMen.add_command(label="neuer Mitarbeiter", command-newEmp);
fileMen.add_command(label="neuer Mitarbeiter", command=newEmp);

fileMen.add_command(label="beenden", command=EmpWin.destroy);
    

#Widgets (Controles) iitialisieren
cmbEmployees = ttk.Combobox();
cmbEmployees["values"] =getDropdownList();
cmbEmployees.bind("<<ComboboxSelected>>", selectEmployee);
cmbEmployees.place(x=80, y=10, width=200);
    
lblFName = ttk.Label(text="Vorname");
lblFName.place(x=10, y=40);
txtFName = ttk.Entry();
txtFName.place(x=80, y=40, width =200)

lblLName = ttk.Label(text="Nachname");
lblLName.place(x=10, y=70);
txtLName = ttk.Entry();
txtLName.place(x=80, y=70, width =200)

lblBDay = ttk.Label(text="Geburtstag");
lblBDay.place(x=10, y=100);
txtBDay = ttk.Entry();
txtBDay.place(x=80, y=100, width =200)

btnUpdate = ttk.Button(text = "ändern", command=clickSaveButton);
btnUpdate.place(x=200, y=130, width = 80);
btnInsert=ttk.Button(text= "anlegen", command=clickInsertButton);



EmpWin.mainloop();
