# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 14:06:01 2019

@author: 307010381
"""
import sys
from ui_file import CPT_UI
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D


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

class cptMain(QMainWindow,CPT_UI.Ui_CarpetPlotMainWindow):
    
    def __init__(self,parent=None):
        super(cptMain,self).__init__(parent)
        self.setupUi(self)   
        
#        CALLING METHODS
        self.startingUpOperations()
        self.settingUpPlottingSpace()
        self.pushButtonOpen.clicked.connect(self.importCSVFile)
        self.XcomboBox.currentTextChanged.connect(self.plottingSurface)
        self.YcomboBox.currentTextChanged.connect(self.plottingSurface)
        self.ZcomboBox.currentTextChanged.connect(self.plottingSurface)
        self.comboBoxSlider1.currentTextChanged.connect(self.assignValuesToSlider)
        self.comboBoxSlider2.currentTextChanged.connect(self.assignValuesToSlider)
        self.comboBoxSlider3.currentTextChanged.connect(self.assignValuesToSlider)
        self.comboBoxSlider4.currentTextChanged.connect(self.assignValuesToSlider)
        

    
    def startingUpOperations(self):
        self.lineEdit.setReadOnly(1)
    
    def settingUpPlottingSpace(self):
        self.axis = Axes3D(plt.figure())
        self.mainGraphicsView = FigureCanvas(plt.figure())
        self.mainGraphicsView.setGeometry(QtCore.QRect(5,100, 790, 400))
        self.mainGraphicsView.setObjectName("mainGraphicsView")
        self.layout().addWidget(self.mainGraphicsView)
        self.naviagationbar = NavigationToolbar(self.mainGraphicsView, self)
        self.addToolBar(self.naviagationbar)
        self.centralwidget.setMaximumSize(1070, 590)
        self.centralwidget.setMinimumSize(1070, 590)

    def importCSVFile(self):
        self.fname = QFileDialog.getOpenFileName(None,"Select CSV files"
                                                 ,"","CSV files (*.csv)")
        self.lineEdit.setText(self.fname[0])
        self.lineEdit.setReadOnly(1)
        self.dataFrameGeneration()
    
    def dataFrameGeneration(self):
        self.df = pd.read_csv(self.fname[0])
        for item in list(self.df.columns):
            self.XcomboBox.addItem(item)
            self.YcomboBox.addItem(item)
            self.ZcomboBox.addItem(item)
        
        self.settingPlottingVariables()   
       
        
    def settingPlottingVariables(self):
        if len(self.df.columns)>4:
            self.XcomboBox.setCurrentIndex(1)
            self.YcomboBox.setCurrentIndex(2)
            self.ZcomboBox.setCurrentIndex(3)        
        else:
            try:
                self.XcomboBox.setCurrentIndex(0)
                self.YcomboBox.setCurrentIndex(0)
                self.ZcomboBox.setCurrentIndex(0)       
            except:
                pass
        self.plottingSurface()
    
    def settingFilters(self):
        self.comboBoxSlider1.addItem('None')
        self.comboBoxSlider2.addItem('None')
        self.comboBoxSlider3.addItem('None')
        self.comboBoxSlider4.addItem('None') 
        
        for item in list(self.df.columns):
            if item not in ([self.XcomboBox.currentText(),self.YcomboBox.currentText(),self.ZcomboBox.currentText()]):
                self.comboBoxSlider1.addItem(item)
                self.comboBoxSlider2.addItem(item)
                self.comboBoxSlider3.addItem(item)
                self.comboBoxSlider4.addItem(item)  
        
        self.assignValuesToSlider()
                
    def assignValuesToSlider(self):
        
#        comboBoxSliderDictionary = {self.comboBoxSlider1 : self.horizontalSlider1,
#                                    self.comboBoxSlider2 : self.horizontalSlider2,
#                                    self.comboBoxSlider3 : self.horizontalSlider3,
#                                    self.comboBoxSlider4 : self.horizontalSlider4}
#        
#        
#                              
#        for comboBoxVar,slider in comboBoxSliderDictionary.items():
            if self.comboBoxSlider1.currentIndex() != 0:
                var = self.comboBoxSlider1.currentText()
#                print(var)
#                print(type(var))
                print(self.df[var].head())
#                print(self.df[self.comboBoxSlider1.currentText()])
                
#                print(self.df[comboBox.currentText()].head())
#                for item in self.df[comboBox.currentText()].unique():
#                    print(item)
#                    slider.setTickPosition(QSlider.TicksAbove)
#                    slider.setFocusPolicy(Qt.StrongFocus)
#                    slider.setTickInterval(item)
            else:
                    pass
#                    slider.setTickPosition(QSlider.TicksAbove)
#                    slider.setFocusPolicy(Qt.StrongFocus)            
        
    
    def plottingSurface(self):
        self.settingFilters()
        self.plotwindow()
        try:
            self.surface = self.axis.plot_trisurf(self.df[self.XcomboBox.currentText()], 
                                              self.df[self.YcomboBox.currentText()], 
                                              self.df[self.ZcomboBox.currentText()],
                                              cmap=cm.jet,shade=False,
                                              antialiased=False)

        
            self.axis.set_xlabel(self.XcomboBox.currentText())
            self.axis.set_ylabel(self.YcomboBox.currentText())
            self.axis.set_zlabel(self.ZcomboBox.currentText())
            self.axis.set_title(self.ZcomboBox.currentText()+' vs '+
                                self.XcomboBox.currentText()+' vs '+
                                self.YcomboBox.currentText())
            self.axis.mouse_init()
        
        except:
            pass


    def plotwindow(self):
        self.layout().removeWidget(self.mainGraphicsView)
        self.removeToolBar(self.naviagationbar)
        self.main_frame = QWidget()
        self.figure = plt.figure()
        self.axis = Axes3D(self.figure)
        self.mainGraphicsView = FigureCanvas(self.figure)
        self.mainGraphicsView.setGeometry(QtCore.QRect(5,100, 790, 400))
        self.mainGraphicsView.setObjectName("mainGraphicsView")
        self.mainGraphicsView.setParent( self.main_frame )
        self.layout().addWidget(self.mainGraphicsView)
        self.naviagationbar = NavigationToolbar(self.mainGraphicsView, self.main_frame)
        self.addToolBar(self.naviagationbar)
        self.centralwidget.setMaximumSize(1070, 590)
        self.centralwidget.setMinimumSize(1070, 590)




if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CPT = cptMain()
    CPT.show()
    sys.exit(app.exec_())