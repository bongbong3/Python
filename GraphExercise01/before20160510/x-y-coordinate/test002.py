import test002Layout
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class StartUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = test002Layout.Ui_MainWindow()
        self.ui.setupUi(self)

        self.dpi = 55
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        self.axes.set_title('Gas Pipeline Network System')
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Amounted used')

        self.axes.grid(True)

        QObject.connect(self.ui.pushButton_draw, SIGNAL('clicked()'), self.onDraw)
        #QObject.connect(self.ui.pushButton_draw2, SIGNAL('clicked()'), self.onDraw2)
        QObject.connect(self.ui.pushButton_clear, SIGNAL('clicked()'), self.clear)

        self.count = 0

        self.ui.verticalLayout.addWidget(self.canvas)

    def onDraw(self):
        # Add QMessageBox
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText('Warning. Match the x value and y value')
        msg.setWindowTitle('MessageBox')


        originalData = unicode(self.ui.lineEdit_data01.text())
        convertData = map(int, originalData.split())

        yData = unicode(self.ui.lineEdit_data02.text())
        yConfirm = map(int, yData.split())

        self.axes.set_title('Gas Pipeline Network System')
        self.axes.set_xlabel('Time')
        self.axes.set_ylabel('Amounted used')

        self.axes.grid(True)

        try:
            self.axes.plot(convertData, yConfirm)
            #self.axes.plot(range(10), convertData)
            self.canvas.draw()
        except:
            msg
            msg.exec_()


    def clear(self):
        self.axes.clear()
        self.canvas.draw()

def main():
    app = QApplication(sys.argv)
    form = StartUi()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()
