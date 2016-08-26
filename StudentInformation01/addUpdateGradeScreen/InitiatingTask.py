'''
Created on 2016. 4. 18.

@author: USER
'''
import sys
import studentManagement as sm
import AnotherInitiating01 as ai01
import Update as up
import Grade as gr
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sqlite3
from PyQt4.QtSql import QSqlQueryModel, QSqlDatabase, QSqlQuery
import UpdateDataBase


class StartGrade(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.uigr = gr.Ui_Dialog()
        self.uigr.setupUi(self)
        
        self.uigr.Btn_studentInf.clicked.connect(self.cont)
        self.uigr.Btn_Update.clicked.connect(self.contUpdate)
        
        
        
    def cont(self):
        sqt = startQT4()
        sqt.open()
        self.close()        
        sqt.exec_()
        
    def contUpdate(self):
        sut = StartUpdate()
        sut.open()
        self.close()        
        sut.exec_()

class StartUpdate(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        #self.setAttribute(Qt.WA_DeleteOnClose)
        self.uiup = up.Ui_Dialog()
        self.a = self.uiup.setupUi(self)
        
        self.uiup.Btn_studentInf.clicked.connect(self.cont)                
        self.uiup.Btn_Grade.clicked.connect(self.contGrade)
        
    def cont(self):
        sqt = startQT4()
        sqt.open()
        self.close()        
        sqt.exec_()
    
    def contGrade(self):
        self.sgr = StartGrade()
        self.sgr.open()
        self.close()   
        self.sgr.exec_()
        # end
        

class startQT4(QDialog):
    def __init__(self, parent=None):
        QDialog.__init__(self, parent)
        self.ui = sm.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.table_studentList

        # Call DB
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("studentInformation001.db")
        self.db.open()
        # End of call DB

        # student info into table view
        projectModel = QSqlQueryModel()
        projectModel.setQuery("SELECT schoolNumber, Name FROM Student ORDER BY schoolNumber ASC",self.db)

        projectView = self.ui.table_studentList
        projectView.setModel(projectModel)
        projectView.show()
        #end of student info into table view

        # QTableView Click Event
        self.qTableView = self.ui.table_studentList
        self.qTableView.clicked.connect(self.showInfo)
        
        # click and connection update
        self.ui.Btn_Update.clicked.connect(self.cont)
        
        # click and connection grade
        self.ui.Btn_Grade.clicked.connect(self.contGrade)
        
    def cont(self):
        self.sup = StartUpdate()
        self.sup.open()
        # this not working.
        self.db.close()
        # end
        # close before QDialog
        self.close()        
        # end
        # maintain new Qdialog
        self.sup.exec_()
        # end
    
    def contGrade(self):
        self.sgr = StartGrade()
        self.sgr.open()
        # this not working.
        self.db.close()
        # end
        # close before QDialog
        self.close()        
        # end
        # maintain new Qdialog
        self.sgr.exec_()
        # end

    def showInfo(self):
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

        # Get strSchoolNumber
        school01 = str((modelIndex.data()).toString())                    

        # Get specific data
        conn = sqlite3.connect('studentInformation001.db')
        cursor = conn.cursor()
        dataList = []
        dataList2 = []        
        if getColumn == 1:
            cursor.execute("SELECT * FROM Student LIMIT " + str(getRow) + ", 1")
            dataList = cursor.fetchall()
        elif getColumn == 0:        
            cursor.execute("SELECT * FROM Student WHERE schoolNumber = " + school01)
            dataList2 = cursor.fetchall()

        # Click the schoolNumber
        if getColumn == 0:
            self.ui.lineEdit_number.setText(modelIndex.data().toString())            
            self.ui.lineEdit_name.setText(str((dataList2[0])[1]))
            #self.ui.lineEdit_address2.setText(str((dataList[0])[2]))
            self.ui.lineEdit_phone.setText(str((dataList2[0])[3]))
            self.ui.lineEdit_group.setText(str((dataList2[0])[4]))
            self.ui.lineEdit_major.setText(str((dataList2[0])[5]))
            self.ui.lineEdit_grade.setText(str((dataList2[0])[6]))
            
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
    sys.exit(app.exec_())
