'''
Created on 2016. 4. 19.

@author: USER
'''
import sqlite3
from PyQt4.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery

'''
class GetConnection():
    con = QSqlDatabase.addDatabase('QSQLITE')
    con.setDatabaseName('studentInformation001.db')
    con.open()
'''
class GetConnection():
    con = sqlite3.connect('studentInformation001.db')
    cursor = con.cursor()

'''
class SearchAll():
    def doSearchAll(self):
        self.data = GetConnection.cursor.execute("SELECT * FROM Student")
        return self.data
'''

'''
class SearchTable():
    def doSearchTable(self):
        tableView = QSqlQueryModel()
        data = tableView.setQuery("SELECT schoolNumber, Name FROM Student", GetConnection.con)
        return data
'''


class SearchTable():
    def doSearchTable(self):
        #SELECT schoolNumber, Name FROM Student
        self.data = GetConnection.cursor.execute("SELECT schoolNumber, Name FROM Student")
        return self.data


class Getclose():
    def doClose(self):
        GetConnection.cursor.close()
        GetConnection.con.close()
'''
con = Getconnection()
con.con
con.cursor
inputTable = SearchTable()
data = (inputTable.doSearchTable()).fetchall()
print(data)
Getclose().doClose()
'''