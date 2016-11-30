import sys

from PyQt4 import QtGui

from form import Ui_Dialog


class MyDialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.calcButton.clicked.connect(self.start)

    def start(self):
        x = self.ui.Amount.text()
        try:
            x = int(x)
        except Exception:
            QtGui.QMessageBox.about(self, 'Error', 'Input can only be a number')
            pass

        SaleswithintheUS = lambda x: ((x * 0.029) + 0.30) + x
        Discountedrateforeligiblenonprofits = lambda x: ((x * 0.022) + 0.30) + x
        Internationalsales = lambda x: ((x * 0.039) + 0.30) + x
        PayPalHereTMcardreaderSWIPE = lambda x: ((x * 0.027)) + x
        PayPalHereTMcardreaderMANUAL = lambda x: ((x * 0.035) + 0.15) + x
        calculate = ""

        if self.ui.radioButton1.isChecked():
            calculate = SaleswithintheUS
        elif self.ui.radioButton2.isChecked():
            calculate = Discountedrateforeligiblenonprofits
        elif self.ui.radioButton3.isChecked():
            calculate = Internationalsales
        elif self.ui.radioButton4.isChecked():
            calculate = PayPalHereTMcardreaderSWIPE
        elif self.ui.radioButton5.isChecked():
            calculate = PayPalHereTMcardreaderMANUAL

        total = calculate(int(x))
        fee = total - int(x)
        self.ui.Total.setText(format(total))
        self.ui.Fee.setText(format(fee))
        print("\nTotal amount : {0} Fee : {1}".format(total, fee))
        # print self.ui.Amount.text()
        # lol = ((x * 0.029) + 0.30) + x
        # print calculate(int(x))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())
