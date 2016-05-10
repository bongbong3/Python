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

        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 621, 341))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 350, 621, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))

        self.lineEdit_data01 = QtGui.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_data01.setObjectName(_fromUtf8("lineEdit_data01"))
        self.horizontalLayout.addWidget(self.lineEdit_data01)

        # Set the lineEdit
        self.lineEdit_data01.setText('1 2 5 7 10 11 15')
        # End

        self.pushButton_draw = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_draw.setObjectName(_fromUtf8("pushButton_draw"))
        self.horizontalLayout.addWidget(self.pushButton_draw)

        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 390, 621, 41))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))

        self.lineEdit_data02 = QtGui.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_data02.setObjectName(_fromUtf8("lineEdit_data02"))
        self.horizontalLayout_3.addWidget(self.lineEdit_data02)

        # Set the lineEdit
        self.lineEdit_data02.setText('3 7 9 2 5 4 10')
        # End

        self.pushButton_draw2 = QtGui.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_draw2.setObjectName(_fromUtf8("pushButton_draw2"))
        self.horizontalLayout_3.addWidget(self.pushButton_draw2)

        self.pushButton_clear = QtGui.QPushButton('clear')
        self.pushButton_clear.setObjectName(_fromUtf8('clear'))
        self.horizontalLayout_3.addWidget(self.pushButton_clear)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton_draw.setText(_translate("MainWindow", "Draw", None))
        self.pushButton_draw2.setText(_translate("MainWindow", "Draw", None))