# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'form.ui'
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
        Dialog.resize(270, 260)
        Dialog.setMinimumSize(QtCore.QSize(270, 260))
        Dialog.setMaximumSize(QtCore.QSize(270, 260))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("pp.gif")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.widget = QtGui.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(10, 0, 252, 261))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox = QtGui.QGroupBox(self.widget)
        self.groupBox.setMinimumSize(QtCore.QSize(250, 140))
        self.groupBox.setMaximumSize(QtCore.QSize(250, 140))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.layoutWidget = QtGui.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 231, 111))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.radioButton1 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton1.setChecked(True)
        self.radioButton1.setObjectName(_fromUtf8("radioButton1"))
        self.verticalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton2.setObjectName(_fromUtf8("radioButton2"))
        self.verticalLayout.addWidget(self.radioButton2)
        self.radioButton3 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton3.setObjectName(_fromUtf8("radioButton3"))
        self.verticalLayout.addWidget(self.radioButton3)
        self.radioButton4 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton4.setObjectName(_fromUtf8("radioButton4"))
        self.verticalLayout.addWidget(self.radioButton4)
        self.radioButton5 = QtGui.QRadioButton(self.layoutWidget)
        self.radioButton5.setMaximumSize(QtCore.QSize(16777215, 20))
        self.radioButton5.setObjectName(_fromUtf8("radioButton5"))
        self.verticalLayout.addWidget(self.radioButton5)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.pplogo = QtGui.QLabel(self.widget)
        self.pplogo.setMinimumSize(QtCore.QSize(60, 76))
        self.pplogo.setMaximumSize(QtCore.QSize(60, 76))
        self.pplogo.setBaseSize(QtCore.QSize(80, 0))
        self.pplogo.setText(_fromUtf8(""))
        self.pplogo.setPixmap(QtGui.QPixmap(_fromUtf8("pp.gif")))
        self.pplogo.setScaledContents(True)
        self.pplogo.setObjectName(_fromUtf8("pplogo"))
        self.horizontalLayout_4.addWidget(self.pplogo)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.labelAmount = QtGui.QLabel(self.widget)
        self.labelAmount.setMinimumSize(QtCore.QSize(40, 16))
        self.labelAmount.setMaximumSize(QtCore.QSize(40, 16))
        self.labelAmount.setObjectName(_fromUtf8("labelAmount"))
        self.horizontalLayout_2.addWidget(self.labelAmount)
        self.Amount = QtGui.QLineEdit(self.widget)
        self.Amount.setMinimumSize(QtCore.QSize(80, 20))
        self.Amount.setMaximumSize(QtCore.QSize(80, 20))
        self.Amount.setAutoFillBackground(False)
        self.Amount.setInputMethodHints(QtCore.Qt.ImhDigitsOnly | QtCore.Qt.ImhPreferNumbers)
        self.Amount.setObjectName(_fromUtf8("Amount"))
        self.horizontalLayout_2.addWidget(self.Amount)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.labelFee = QtGui.QLabel(self.widget)
        self.labelFee.setMinimumSize(QtCore.QSize(40, 16))
        self.labelFee.setMaximumSize(QtCore.QSize(40, 16))
        self.labelFee.setObjectName(_fromUtf8("labelFee"))
        self.horizontalLayout_3.addWidget(self.labelFee)
        self.Fee = QtGui.QLineEdit(self.widget)
        self.Fee.setMinimumSize(QtCore.QSize(80, 20))
        self.Fee.setMaximumSize(QtCore.QSize(80, 20))
        self.Fee.setObjectName(_fromUtf8("Fee"))
        self.horizontalLayout_3.addWidget(self.Fee)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.labelTotal = QtGui.QLabel(self.widget)
        self.labelTotal.setMinimumSize(QtCore.QSize(40, 16))
        self.labelTotal.setMaximumSize(QtCore.QSize(40, 16))
        self.labelTotal.setObjectName(_fromUtf8("labelTotal"))
        self.horizontalLayout.addWidget(self.labelTotal)
        self.Total = QtGui.QLineEdit(self.widget)
        self.Total.setMinimumSize(QtCore.QSize(80, 20))
        self.Total.setMaximumSize(QtCore.QSize(80, 20))
        self.Total.setObjectName(_fromUtf8("Total"))
        self.horizontalLayout.addWidget(self.Total)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.calcButton = QtGui.QPushButton(self.widget)
        self.calcButton.setMinimumSize(QtCore.QSize(60, 20))
        self.calcButton.setMaximumSize(QtCore.QSize(60, 25))
        self.calcButton.setObjectName(_fromUtf8("calcButton"))
        self.verticalLayout_3.addWidget(self.calcButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "PayPal Fee Calculator", None))
        self.groupBox.setTitle(_translate("Dialog", "Type", None))
        self.radioButton1.setText(_translate("Dialog", "Sales within the US", None))
        self.radioButton2.setText(_translate("Dialog", "Discounted rate for eligible nonprofits", None))
        self.radioButton3.setText(_translate("Dialog", "International sales", None))
        self.radioButton4.setText(_translate("Dialog", "PayPal HereTM card reader - swipe", None))
        self.radioButton5.setText(_translate("Dialog", "PayPal HereTM card reader - manual entry", None))
        self.labelAmount.setText(_translate("Dialog", "Amount", None))
        self.labelFee.setText(_translate("Dialog", "Fee", None))
        self.labelTotal.setText(_translate("Dialog", "Total", None))
        self.calcButton.setText(_translate("Dialog", "Calculate", None))
