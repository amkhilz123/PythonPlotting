# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carpet_plotter2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CarpetPlotMainWindow(object):
    def setupUi(self, CarpetPlotMainWindow):
        CarpetPlotMainWindow.setObjectName("CarpetPlotMainWindow")
        CarpetPlotMainWindow.setEnabled(True)
        CarpetPlotMainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CarpetPlotMainWindow.sizePolicy().hasHeightForWidth())
        CarpetPlotMainWindow.setSizePolicy(sizePolicy)
        CarpetPlotMainWindow.setMaximumSize(QtCore.QSize(800, 600))
        CarpetPlotMainWindow.setToolTipDuration(0)
        self.centralwidget = QtWidgets.QWidget(CarpetPlotMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonOpen = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonOpen.setGeometry(QtCore.QRect(10, 530, 75, 23))
        self.pushButtonOpen.setObjectName("pushButtonOpen")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 500, 351, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.XcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.XcomboBox.setGeometry(QtCore.QRect(418, 465, 121, 22))
        self.XcomboBox.setObjectName("XcomboBox")
        self.YcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.YcomboBox.setGeometry(QtCore.QRect(418, 505, 121, 22))
        self.YcomboBox.setObjectName("YcomboBox")
        self.ZcomboBox = QtWidgets.QComboBox(self.centralwidget)
        self.ZcomboBox.setGeometry(QtCore.QRect(418, 545, 121, 22))
        self.ZcomboBox.setObjectName("ZcomboBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(368, 470, 47, 13))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(368, 509, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(368, 548, 47, 13))
        self.label_3.setObjectName("label_3")
        CarpetPlotMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarpetPlotMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CarpetPlotMainWindow.setMenuBar(self.menubar)

        self.retranslateUi(CarpetPlotMainWindow)
        QtCore.QMetaObject.connectSlotsByName(CarpetPlotMainWindow)

    def retranslateUi(self, CarpetPlotMainWindow):
        _translate = QtCore.QCoreApplication.translate
        CarpetPlotMainWindow.setWindowTitle(_translate("CarpetPlotMainWindow", "Carpet Plotter"))
        self.pushButtonOpen.setText(_translate("CarpetPlotMainWindow", "Open"))
        self.label.setText(_translate("CarpetPlotMainWindow", "X axis"))
        self.label_2.setText(_translate("CarpetPlotMainWindow", "Y axis"))
        self.label_3.setText(_translate("CarpetPlotMainWindow", "Z axis"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarpetPlotMainWindow = QtWidgets.QMainWindow()
    ui = Ui_CarpetPlotMainWindow()
    ui.setupUi(CarpetPlotMainWindow)
    CarpetPlotMainWindow.show()
    sys.exit(app.exec_())

