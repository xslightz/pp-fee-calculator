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
        amount = self.ui.Amount.text()
        try:
            amount = float(amount)  # convert to a float
        except ValueError as e:
            QtGui.QMessageBox.about(self, 'Error', 'Input can only be a number')
            # print(e)  # optional, only for verbosity
            return

        # Define the different functions for calculation
        SaleswithintheUS = lambda x: ((x * 0.029) + 0.30) + x
        Discountedrateforeligiblenonprofits = lambda x: ((x * 0.022) + 0.30) + x
        Internationalsales = lambda x: ((x * 0.039) + 0.30) + x
        PayPalHereTMcardreaderSWIPE = lambda x: ((x * 0.027)) + x
        PayPalHereTMcardreaderMANUAL = lambda x: ((x * 0.035) + 0.15) + x

        options = {
            self.ui.radioButton1: SaleswithintheUS,
            self.ui.radioButton2: Discountedrateforeligiblenonprofits,
            self.ui.radioButton3: Internationalsales,
            self.ui.radioButton4: PayPalHereTMcardreaderSWIPE,
            self.ui.radioButton5: PayPalHereTMcardreaderMANUAL,
        }

        calculate = options.get(self.ui.radioButtonGroup.checkedButton(), lambda x: x)  # get the calculation formula
        total = calculate(amount)  # don't use ints, use floats!
        fee = total - amount

        def prec_format(val, prec=2):  # this will return a formatted float value with a desired precision
            return "{:.{precision}f}".format(float(val), precision=prec)

        self.ui.Total.setText(prec_format(total))
        self.ui.Fee.setText(prec_format(fee))

        print("\nTotal amount : {0} Fee : {1}".format(total, fee))


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())