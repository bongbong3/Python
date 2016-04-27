import layoutTest002
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class StartUi(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = layoutTest002.Ui_MainWindow()
        self.ui.setupUi(self)

        self.dpi = 100
        self.fig = Figure((5.0, 4.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        QObject.connect(self.ui.pushButton_draw, SIGNAL('clicked()'), self.onDraw)
        QObject.connect(self.ui.pushButton_draw2, SIGNAL('clicked()'), self.onDraw2)
        QObject.connect(self.ui.pushButton_clear, SIGNAL('clicked()'), self.clear)

        self.count = 0

        self.ui.verticalLayout.addWidget(self.canvas)

    def onDraw(self):
        originalData = unicode(self.ui.lineEdit_data01.text())
        convertData = map(int, originalData.split())

        self.axes.plot(convertData)
        self.canvas.draw()

    def onDraw2(self):
        originalData = unicode(self.ui.lineEdit_data02.text())
        convertData = map(int, originalData.split())

        self.axes.plot(convertData)
        self.canvas.draw()

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
