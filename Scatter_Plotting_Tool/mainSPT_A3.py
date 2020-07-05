# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 21:00:36 2018

@author: 307010381
"""

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import sys
from ui_file import dptGUIMainWindow2
import pandas as pd
import matplotlib.pyplot as plt

#IMPORTING LIBRARIES TO INCLUDE THE GRAPHICS AREA
#============================================================================
from matplotlib.backends.qt_compat import QtCore, QtWidgets, is_pyqt5
if is_pyqt5():
    from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
else:
    from matplotlib.backends.backend_qt4agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
#============================================================================

class dptMain(QMainWindow,dptGUIMainWindow2.Ui_mainWindow):
    
    def __init__(self,parent=None):
        super(dptMain,self).__init__(parent)
        self.setupUi(self)      
#        SETTING UP FIGURE IN THE GUI
        self.mainGraphicsView = FigureCanvas(plt.figure())
        self.mainGraphicsView.setGeometry(QtCore.QRect(5,100, 790, 300))
        self.mainGraphicsView.setObjectName("mainGraphicsView")
        self.layout().addWidget(self.mainGraphicsView)
        self.naviagationbar = NavigationToolbar(self.mainGraphicsView, self)
        self.addToolBar(self.naviagationbar)
        self.centralwidget.setMaximumSize(801, 650)
        self.centralwidget.setMinimumSize(801, 650)
        self.csvDataRead = {}

        
#        CALLING THE METHODS
        self.mainImportCSV.clicked.connect(self.import_csv_files)
        self.mainPlotSingleChartButton.clicked.connect(self.plot_single_variable)
        self.mainPlotAllButton.clicked.connect(self.plot_all_variables)
        self.mainSaveAllButton.clicked.connect(self.save_all_variables)
        self.mainSelectAll.clicked.connect(self.select_all_csv_files)
        

        
    def import_csv_files(self):
        self.fname = QFileDialog.getOpenFileNames(None,"Select CSV files"
                                                 ,"","CSV files (*.csv)")
        self.legend = 0
        for filenames in self.fname[0]:
            self.legendName = self.fname[0][self.legend].split('/')[-1].split('.csv')[0]
            currentRowCount = self.mainTable.rowCount()
            self.mainTable.insertRow(currentRowCount)
            self.mainTable.setItem(currentRowCount,0,QTableWidgetItem(self.legendName))            
            self.csvDataRead[self.legendName]= pd.read_csv(self.fname[0][self.legend])
            self.legend +=1
        self.csvHeaderList = list(self.csvDataRead[self.legendName].columns.values)
        self.csvHeaderListInitial = self.csvHeaderList.copy()
        del self.csvHeaderList[0]
        self.mainComboBox.clear()
        self.mainComboBox.addItems(self.csvHeaderList)

        
    def select_all_csv_files(self):
        totalRowCount= self.mainTable.rowCount()
        self.mainTable.selectAll()
        self.mainTable.setFocus()
        print(self.mainTable.selectedIndexes())
        
    
    def plot_single_variable(self):
        selectedCsvs = self.mainTable.selectedItems()
        selectedCsvNameList =[]
        for sel in selectedCsvs:
            selectedCsvNameList.append(sel.text())
        self.plotwindow()
        for keys, values in self.csvDataRead.items():
            if keys in selectedCsvNameList:
                self.x = values.iloc[:,0]
                self.y = values.loc[:,self.mainComboBox.currentText()]
                plt.plot(self.x,self.y,label=keys)
                plt.ylabel(self.mainComboBox.currentText(),weight='bold')
                plt.xlabel(self.csvHeaderListInitial[0],weight='bold')   
        plt.legend()
        plt.title(self.mainComboBox.currentText(),weight='bold')
        #plt.show()
        
    
    def plot_all_variables(self):
        selectedCsvs = self.mainTable.selectedItems()
        selectedCsvNameList =[]
        for sel in selectedCsvs:
            selectedCsvNameList.append(sel.text())
        self.plotwindow()
        self.mainComboBoxVariableCount = self.mainComboBox.count()
        for keys, values in self.csvDataRead.items():
            if keys in selectedCsvNameList:
                self.x = values.iloc[:,0]
                self.y = values.loc[:,self.mainComboBox.currentText()]
                plt.plot(self.x,self.y,label=keys)
                plt.ylabel(self.mainComboBox.currentText(),weight='bold')
                plt.xlabel(self.csvHeaderListInitial[0],weight='bold')   
        plt.legend()
        plt.title(self.mainComboBox.currentText(),weight='bold')                     
            
        QMessageBox.information(self,"Saving all plots","DONE!")
    
    def save_single_variable(self):
        self.x = self.csvDataRead.iloc[:,0]
        self.y = self.csvDataRead.loc[:,self.mainComboBox.currentText()]
        plt.figure()
        plt.plot(self.x,self.y)
        plt.ylabel(self.mainComboBox.currentText())
        plt.xlabel(self.csvHeaderListInitial[0])
        plt.legend(self.legendName)
        plt.savefig(str(self.mainComboBox.currentText())+'.png')
    
    def save_all_variables(self):
        self.mainComboBoxVariableCount = self.mainComboBox.count()
        for eachVariable in range(self.mainComboBoxVariableCount):
            self.eachx = self.csvDataRead.iloc[:,0]
            self.eachy = self.csvDataRead.loc[:,self.csvHeaderList[eachVariable]]
            plt.figure()
            plt.plot(self.eachx,self.eachy)
            plt.ylabel(self.csvHeaderList[eachVariable])
            plt.xlabel(self.csvHeaderListInitial[0])
            plt.legend(self.legendName)
            plt.savefig(str(self.csvHeaderList[eachVariable])+'.png')
        
    def plotwindow(self):
        self.layout().removeWidget(self.mainGraphicsView)
        self.removeToolBar(self.naviagationbar)
        
        self.mainGraphicsView = FigureCanvas(plt.figure())
        self.mainGraphicsView.setGeometry(QtCore.QRect(5,100, 790, 300))
        self.mainGraphicsView.setObjectName("mainGraphicsView")
        self.layout().addWidget(self.mainGraphicsView)
        self.naviagationbar = NavigationToolbar(self.mainGraphicsView, self)
        self.addToolBar(self.naviagationbar)
        self.centralwidget.setMaximumSize(801, 650)
        self.centralwidget.setMinimumSize(801, 650)
        
if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    '''
    if not QApplication.instance():
        app = QApplication.instance(sys.argv)
    else:
        app = QApplication.instance()
    '''
    DPT = dptMain()
    DPT.show()
    sys.exit(app.exec_())