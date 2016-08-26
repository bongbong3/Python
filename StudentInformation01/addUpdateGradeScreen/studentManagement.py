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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(640, 480)
        self.lineEdit_major = QtGui.QLineEdit(Dialog)
        self.lineEdit_major.setGeometry(QtCore.QRect(500, 210, 121, 21))
        self.lineEdit_major.setObjectName(_fromUtf8("lineEdit_major"))
        self.label_name = QtGui.QLabel(Dialog)
        self.label_name.setGeometry(QtCore.QRect(290, 90, 61, 21))
        self.label_name.setAlignment(QtCore.Qt.AlignCenter)
        self.label_name.setObjectName(_fromUtf8("label_name"))
        self.lineEdit_number = QtGui.QLineEdit(Dialog)
        self.lineEdit_number.setGeometry(QtCore.QRect(360, 60, 141, 21))
        self.lineEdit_number.setObjectName(_fromUtf8("lineEdit_number"))
        self.label_grade = QtGui.QLabel(Dialog)
        self.label_grade.setGeometry(QtCore.QRect(290, 240, 61, 25))
        self.label_grade.setMinimumSize(QtCore.QSize(30, 25))
        self.label_grade.setAlignment(QtCore.Qt.AlignCenter)
        self.label_grade.setObjectName(_fromUtf8("label_grade"))
        self.Btn_Update = QtGui.QPushButton(Dialog)
        self.Btn_Update.setGeometry(QtCore.QRect(90, 20, 75, 31))
        self.Btn_Update.setObjectName(_fromUtf8("Btn_Update"))
        self.lineEdit_name = QtGui.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(360, 90, 141, 21))
        self.lineEdit_name.setObjectName(_fromUtf8("lineEdit_name"))
        self.lineEdit_address2 = QtGui.QLineEdit(Dialog)
        self.lineEdit_address2.setGeometry(QtCore.QRect(360, 150, 261, 21))
        self.lineEdit_address2.setObjectName(_fromUtf8("lineEdit_address2"))
        self.lineEdit_group = QtGui.QLineEdit(Dialog)
        self.lineEdit_group.setGeometry(QtCore.QRect(360, 210, 51, 21))
        self.lineEdit_group.setObjectName(_fromUtf8("lineEdit_group"))
        self.textBrowser_etc = QtGui.QTextBrowser(Dialog)
        self.textBrowser_etc.setGeometry(QtCore.QRect(300, 300, 321, 141))
        self.textBrowser_etc.setObjectName(_fromUtf8("textBrowser_etc"))
        self.Btn_Grade = QtGui.QPushButton(Dialog)
        self.Btn_Grade.setGeometry(QtCore.QRect(170, 20, 75, 31))
        self.Btn_Grade.setObjectName(_fromUtf8("Btn_Grade"))
        self.label_number = QtGui.QLabel(Dialog)
        self.label_number.setGeometry(QtCore.QRect(290, 60, 61, 25))
        self.label_number.setMinimumSize(QtCore.QSize(30, 25))
        self.label_number.setAlignment(QtCore.Qt.AlignCenter)
        self.label_number.setObjectName(_fromUtf8("label_number"))
        self.Btn_studentInf = QtGui.QPushButton(Dialog)
        self.Btn_studentInf.setGeometry(QtCore.QRect(10, 20, 75, 31))
        self.Btn_studentInf.setObjectName(_fromUtf8("Btn_studentInf"))
        self.label_phone = QtGui.QLabel(Dialog)
        self.label_phone.setGeometry(QtCore.QRect(290, 180, 61, 25))
        self.label_phone.setMinimumSize(QtCore.QSize(30, 25))
        self.label_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.label_phone.setObjectName(_fromUtf8("label_phone"))
        self.label_group = QtGui.QLabel(Dialog)
        self.label_group.setGeometry(QtCore.QRect(290, 210, 61, 25))
        self.label_group.setMinimumSize(QtCore.QSize(30, 25))
        self.label_group.setAlignment(QtCore.Qt.AlignCenter)
        self.label_group.setObjectName(_fromUtf8("label_group"))
        self.label_address = QtGui.QLabel(Dialog)
        self.label_address.setGeometry(QtCore.QRect(290, 120, 61, 21))
        self.label_address.setAlignment(QtCore.Qt.AlignCenter)
        self.label_address.setObjectName(_fromUtf8("label_address"))
        self.lineEdit_address1 = QtGui.QLineEdit(Dialog)
        self.lineEdit_address1.setGeometry(QtCore.QRect(360, 120, 91, 21))
        self.lineEdit_address1.setObjectName(_fromUtf8("lineEdit_address1"))
        self.label_major = QtGui.QLabel(Dialog)
        self.label_major.setGeometry(QtCore.QRect(430, 210, 61, 25))
        self.label_major.setMinimumSize(QtCore.QSize(30, 25))
        self.label_major.setAlignment(QtCore.Qt.AlignCenter)
        self.label_major.setObjectName(_fromUtf8("label_major"))
        self.label_etc = QtGui.QLabel(Dialog)
        self.label_etc.setGeometry(QtCore.QRect(290, 270, 61, 25))
        self.label_etc.setMinimumSize(QtCore.QSize(30, 25))
        self.label_etc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_etc.setObjectName(_fromUtf8("label_etc"))
        self.table_studentList = QtGui.QTableView(Dialog)
        self.table_studentList.setGeometry(QtCore.QRect(10, 60, 271, 381))
        self.table_studentList.setObjectName(_fromUtf8("table_studentList"))
        self.lineEdit_phone = QtGui.QLineEdit(Dialog)
        self.lineEdit_phone.setGeometry(QtCore.QRect(360, 180, 141, 21))
        self.lineEdit_phone.setObjectName(_fromUtf8("lineEdit_phone"))
        self.lineEdit_grade = QtGui.QLineEdit(Dialog)
        self.lineEdit_grade.setGeometry(QtCore.QRect(360, 240, 51, 21))
        self.lineEdit_grade.setText(_fromUtf8(""))
        self.lineEdit_grade.setObjectName(_fromUtf8("lineEdit_grade"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label_name.setText(_translate("Dialog", "Name", None))
        self.label_grade.setText(_translate("Dialog", "Grade", None))
        self.Btn_Update.setText(_translate("Dialog", "Update", None))
        self.Btn_Grade.setText(_translate("Dialog", "Grade", None))
        self.label_number.setText(_translate("Dialog", "Number", None))
        self.Btn_studentInf.setText(_translate("Dialog", "Student Inf", None))
        self.label_phone.setText(_translate("Dialog", "Phone", None))
        self.label_group.setText(_translate("Dialog", "Group", None))
        self.label_address.setText(_translate("Dialog", "Address", None))
        self.label_major.setText(_translate("Dialog", "Major", None))
        self.label_etc.setText(_translate("Dialog", "etc", None))

