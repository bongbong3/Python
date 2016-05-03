'''
Created on 2016. 4. 18.

@author: USER
'''
import sys
import StudentManagement as sm
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3
from PyQt4.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery


class startQT4(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = sm.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.table_studentList

        # Call DB
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("studentInformation001.db")
        db.open()
        # End of call DB

        # student info into table view
        projectModel = QSqlQueryModel()
        projectModel.setQuery("SELECT schoolNumber, Name FROM Student ORDER BY schoolNumber ASC",db)
        #projectModel.setQuery("SELECT ROW_NUMBER() OVER(ORDER BY schoolNumber ASC) AS 'NO', schoolNumber, Name FROM Student", db)

        projectView = self.ui.table_studentList
        projectView.setModel(projectModel)
        projectView.show()
        #end of student info into table view

        # QTableView Click Event
        #QObject.connect(self.ui.table_studentList, SIGNAL('clicked'), self.view())
        self.qTableView = self.ui.table_studentList
        self.qTableView.clicked.connect(self.goodMorning)

    def view(self):
        print('clicked')

    def goodMorning(self):
        # Clean the LineEdit
        self.ui.lineEdit_number.clear()
        self.ui.lineEdit_name.clear()
        self.ui.lineEdit_address1.clear()
        self.ui.lineEdit_address2.clear()
        self.ui.lineEdit_grade.clear()
        self.ui.lineEdit_group.clear()
        self.ui.lineEdit_major.clear()
        self.ui.lineEdit_phone.clear()

        # Get QModelIndex
        modelIndex = self.ui.table_studentList.currentIndex()
        #getColumn
        getColumn = modelIndex.column()
        #getRow
        getRow = modelIndex.row()

        # Get specific data
        conn = sqlite3.connect('studentInformation001.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student LIMIT " + str(getRow) + ", 1")

        dataList = cursor.fetchall()

        # Click the schoolNumber
        if getColumn == 0:
            self.ui.lineEdit_number.setText(modelIndex.data().toString())
        # Click the Name
        elif getColumn == 1:
            self.ui.lineEdit_name.setText(modelIndex.data().toString())
            self.ui.lineEdit_number.setText(str((dataList[0])[0]))
            self.ui.lineEdit_address2.setText(str((dataList[0])[2]))
            self.ui.lineEdit_phone.setText(str((dataList[0])[3]))
            self.ui.lineEdit_group.setText(str((dataList[0])[4]))
            self.ui.lineEdit_major.setText(str((dataList[0])[5]))
            self.ui.lineEdit_grade.setText(str((dataList[0])[6]))


        # Get QVariant
        modelIndexData = modelIndex.data(0)
        #print(modelIndexData.toString())



if __name__ == "__main__":
    app = QApplication(sys.argv)

    myApp = startQT4()
    myApp.show()
    app.exec_()
