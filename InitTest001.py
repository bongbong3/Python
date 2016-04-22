import layoutTest001
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from scipy.interpolate import spline
import numpy as np
from pylab import title, xlabel, ylabel

class StartUi(QMainWindow):
    def doChange(self):
        # Extract Number to textbox
        originalData = unicode(self.ui.lineEdit_data01.text())
        data01 = map(int, originalData.split())

        # draw graph
        self.dpi = 60
        self.fig = Figure((5.0, 5.0), dpi=self.dpi)
        self.canvas = FigureCanvas(self.fig)
        self.axes = self.fig.add_subplot(111)

        # Spline
        x = np.array(range(len(data01)))
        power = np.array(data01)
        xnew = np.linspace(x.min(), x.max(), 300)
        power_smooth = spline(x, power, xnew)

        # Add xlabel, ylabel
        self.axes.set_title('Pipeline Network')
        self.axes.set_xlabel('Day')
        self.axes.set_ylabel('The amount used')
        self.axes.grid()
        self.axes.plot(xnew, power_smooth)

        #self.axes.plot(data01)
        self.canvas.draw()

        if self.ui.verticalLayout.count() < 1:
            self.ui.verticalLayout.addWidget(self.canvas)
        elif self.ui.verticalLayout.count() > 0:
            for cnt in reversed(range(self.ui.verticalLayout.count())):
                widget = self.ui.verticalLayout.takeAt(cnt).widget()

                if widget is not None:
                    widget.deleteLater()

            self.ui.verticalLayout.addWidget(self.canvas)


    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.ui = layoutTest001.Ui_MainWindow()
        self.ui.setupUi(self)

        QObject.connect(self.ui.lineEdit_data01, SIGNAL('editingFinished()'), self.doChange)
        self.count = 0


    def sortData(self, data):
        packagingData = map(int, data.split())
        return packagingData

def main():
    app = QApplication(sys.argv)
    form = StartUi()
    form.show()
    app.exec_()

if __name__ == "__main__":
    main()