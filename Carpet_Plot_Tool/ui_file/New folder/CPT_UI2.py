# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'carpet_plotter1.ui'
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
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(430, 471, 201, 81))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        CarpetPlotMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CarpetPlotMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        CarpetPlotMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CarpetPlotMainWindow)
        self.statusbar.setObjectName("statusbar")
        CarpetPlotMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CarpetPlotMainWindow)
        QtCore.QMetaObject.connectSlotsByName(CarpetPlotMainWindow)

    def retranslateUi(self, CarpetPlotMainWindow):
        _translate = QtCore.QCoreApplication.translate
        CarpetPlotMainWindow.setWindowTitle(_translate("CarpetPlotMainWindow", "Carpet Plotter"))
        self.pushButtonOpen.setText(_translate("CarpetPlotMainWindow", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CarpetPlotMainWindow = QtWidgets.QMainWindow()
    ui = Ui_CarpetPlotMainWindow()
    ui.setupUi(CarpetPlotMainWindow)
    CarpetPlotMainWindow.show()
    sys.exit(app.exec_())

