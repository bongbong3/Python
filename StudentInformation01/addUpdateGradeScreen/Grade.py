# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Grade.ui'
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
        self.Btn_Grade = QtGui.QPushButton(Dialog)
        self.Btn_Grade.setGeometry(QtCore.QRect(170, 10, 75, 31))
        self.Btn_Grade.setObjectName(_fromUtf8("Btn_Grade"))
        self.Btn_Update = QtGui.QPushButton(Dialog)
        self.Btn_Update.setGeometry(QtCore.QRect(90, 10, 75, 31))
        self.Btn_Update.setObjectName(_fromUtf8("Btn_Update"))
        self.comboBox_2 = QtGui.QComboBox(Dialog)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 50, 31, 22))
        self.comboBox_2.setMaxVisibleItems(3)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.label_Level = QtGui.QLabel(Dialog)
        self.label_Level.setGeometry(QtCore.QRect(10, 50, 51, 21))
        self.label_Level.setFrameShape(QtGui.QFrame.Box)
        self.label_Level.setFrameShadow(QtGui.QFrame.Plain)
        self.label_Level.setLineWidth(2)
        self.label_Level.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Level.setObjectName(_fromUtf8("label_Level"))
        self.Btn_studentInf = QtGui.QPushButton(Dialog)
        self.Btn_studentInf.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.Btn_studentInf.setObjectName(_fromUtf8("Btn_studentInf"))
        self.tableView = QtGui.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(10, 80, 191, 391))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(70, 50, 31, 22))
        self.comboBox.setMaxVisibleItems(3)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label_Class = QtGui.QLabel(Dialog)
        self.label_Class.setGeometry(QtCore.QRect(110, 50, 51, 21))
        self.label_Class.setFrameShape(QtGui.QFrame.Box)
        self.label_Class.setFrameShadow(QtGui.QFrame.Plain)
        self.label_Class.setLineWidth(2)
        self.label_Class.setAlignment(QtCore.Qt.AlignCenter)
        self.label_Class.setObjectName(_fromUtf8("label_Class"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.Btn_Grade.setText(_translate("Dialog", "Grade", None))
        self.Btn_Update.setText(_translate("Dialog", "Update", None))
        self.label_Level.setText(_translate("Dialog", "Level", None))
        self.Btn_studentInf.setText(_translate("Dialog", "Student Inf", None))
        self.label_Class.setText(_translate("Dialog", "Class", None))

