# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'studentManagement.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(640, 480)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.table_studentList = QtGui.QTableView(self.centralwidget)
        self.table_studentList.setGeometry(QtCore.QRect(10, 50, 271, 381))
        self.table_studentList.setObjectName(_fromUtf8("table_studentList"))
        self.label_number = QtGui.QLabel(self.centralwidget)
        self.label_number.setGeometry(QtCore.QRect(290, 50, 61, 25))
        self.label_number.setMinimumSize(QtCore.QSize(30, 25))
        self.label_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number.setObjectName(_fromUtf8("label_number"))
        self.label_name = QtGui.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(290, 80, 61, 21))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.lineEdit_number = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_number.setGeometry(QtCore.QRect(360, 50, 141, 21))
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.lineEdit_name = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(360, 80, 141, 21))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.label_address = QtGui.QLabel(self.centralwidget)
        self.label_address.setGeometry(QtCore.QRect(290, 110, 61, 21))
        self.label_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_address.setObjectName(_fromUtf8("label_address"))
        self.lineEdit_address1 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_address1.setGeometry(QtCore.QRect(360, 110, 91, 21))
        self.lineEdit_address1.setObjectName(_fromUtf8("lineEdit_address1"))
        self.lineEdit_address2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_address2.setGeometry(QtCore.QRect(360, 140, 261, 21))
        self.lineEdit_address2.setObjectName(_fromUtf8("lineEdit_address2"))
        self.label_phone = QtGui.QLabel(self.centralwidget)
        self.label_phone.setGeometry(QtCore.QRect(290, 170, 61, 25))
        self.label_phone.setMinimumSize(QtCore.QSize(30, 25))
        self.label_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phone.setObjectName(_fromUtf8("label_phone"))
        self.lineEdit_phone = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_phone.setGeometry(QtCore.QRect(360, 170, 141, 21))
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.lineEdit_group = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_group.setGeometry(QtCore.QRect(360, 200, 51, 21))
        self.lineEdit_group.setObjectName(_fromUtf8("lineEdit_group"))
        self.label_group = QtGui.QLabel(self.centralwidget)
        self.label_group.setGeometry(QtCore.QRect(290, 200, 61, 25))
        self.label_group.setMinimumSize(QtCore.QSize(30, 25))
        self.label_group.setAlignment(QtCore.Qt.AlignCenter)
        self.label_group.setObjectName(_fromUtf8("label_group"))
        self.label_major = QtGui.QLabel(self.centralwidget)
        self.label_major.setGeometry(QtCore.QRect(430, 200, 61, 25))
        self.label_major.setMinimumSize(QtCore.QSize(30, 25))
        self.label_major.setAlignment(QtCore.Qt.AlignCenter)
        self.label_major.setObjectName(_fromUtf8("label_major"))
        self.lineEdit_major = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_major.setGeometry(QtCore.QRect(500, 200, 121, 21))
        self.lineEdit_major.setObjectName(_fromUtf8("lineEdit_major"))
        self.label_grade = QtGui.QLabel(self.centralwidget)
        self.label_grade.setGeometry(QtCore.QRect(290, 230, 61, 25))
        self.label_grade.setMinimumSize(QtCore.QSize(30, 25))
        self.label_grade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_grade.setObjectName(_fromUtf8("label_grade"))
        self.lineEdit_grade = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_grade.setGeometry(QtCore.QRect(360, 230, 51, 21))
        self.lineEdit_grade.setText(_fromUtf8(""))
        self.lineEdit_grade.setObjectName(_fromUtf8("lineEdit_grade"))
        self.label_etc = QtGui.QLabel(self.centralwidget)
        self.label_etc.setGeometry(QtCore.QRect(290, 260, 61, 25))
        self.label_etc.setMinimumSize(QtCore.QSize(30, 25))
        self.label_etc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_etc.setObjectName(_fromUtf8("label_etc"))
        self.textBrowser_etc = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_etc.setGeometry(QtCore.QRect(300, 290, 321, 141))
        self.textBrowser_etc.setObjectName(_fromUtf8("textBrowser_etc"))
        self.Btn_studentInf = QtGui.QPushButton(self.centralwidget)
        self.Btn_studentInf.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.Btn_studentInf.setObjectName(_fromUtf8("Btn_studentInf"))
        self.Btn_Update = QtGui.QPushButton(self.centralwidget)
        self.Btn_Update.setGeometry(QtCore.QRect(90, 10, 75, 31))
        self.Btn_Update.setObjectName(_fromUtf8("Btn_Update"))
        self.Btn_Grade = QtGui.QPushButton(self.centralwidget)
        self.Btn_Grade.setGeometry(QtCore.QRect(170, 10, 75, 31))
        self.Btn_Grade.setObjectName(_fromUtf8("Btn_Grade"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.table_studentList, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.lineEdit_number.show)
        QtCore.QObject.connect(self.table_studentList, QtCore.SIGNAL(_fromUtf8("clicked(QModelIndex)")), self.lineEdit_name.show)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label_number.setText(_translate("MainWindow", "Number", None))
        self.label_name.setText(_translate("MainWindow", "Name", None))
        self.label_address.setText(_translate("MainWindow", "Address", None))
        self.label_phone.setText(_translate("MainWindow", "Phone", None))
        self.label_group.setText(_translate("MainWindow", "Group", None))
        self.label_major.setText(_translate("MainWindow", "Major", None))
        self.label_grade.setText(_translate("MainWindow", "Grade", None))
        self.label_etc.setText(_translate("MainWindow", "etc", None))
        self.Btn_studentInf.setText(_translate("MainWindow", "Student Inf", None))
        self.Btn_Update.setText(_translate("MainWindow", "Update", None))
        self.Btn_Grade.setText(_translate("MainWindow", "Grade", None))

