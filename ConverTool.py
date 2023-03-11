# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ConverTool.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from number_formatter import num_format

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
<<<<<<< HEAD
=======
        MainWindow.resize(650, 600)
>>>>>>> diffStyle
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setIconSize(QtCore.QSize(32, 32))
        MainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainSelector = QtWidgets.QComboBox(self.centralwidget)
<<<<<<< HEAD
        self.mainSelector.setGeometry(QtCore.QRect(70, 30, 361, 71))
=======
        self.mainSelector.setGeometry(QtCore.QRect(70, 30, 350, 71))

        self.status = QtWidgets.QLineEdit(self.centralwidget)
        self.status.setGeometry(QtCore.QRect(440, 30, 190, 71))
        self.status.setText("Good")
        self.status.setStyleSheet("color:lightgreen; font-family:'Fira Code'; font-weight:bold; font-size:20pt;")
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setReadOnly(True)

>>>>>>> diffStyle
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.mainSelector.setFont(font)
        self.mainSelector.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mainSelector.setObjectName("mainSelector")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.addItem("")
        self.mainSelector.currentIndexChanged.connect(self.mainClick)
        self.firstOption = QtWidgets.QComboBox(self.centralwidget)
<<<<<<< HEAD
        self.firstOption.setGeometry(QtCore.QRect(440, 290, 150, 61))
        self.firstOption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firstOption.setObjectName("firstOption")
        self.secondOption = QtWidgets.QComboBox(self.centralwidget)
        self.secondOption.setGeometry(QtCore.QRect(440, 390, 150, 61))
=======
        self.firstOption.setGeometry(QtCore.QRect(440, 290, 190, 61))
        self.firstOption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.firstOption.setObjectName("firstOption")
        self.secondOption = QtWidgets.QComboBox(self.centralwidget)
        self.secondOption.setGeometry(QtCore.QRect(440, 390, 190, 61))
>>>>>>> diffStyle
        self.secondOption.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.secondOption.setObjectName("secondOption")
        self.firstInput = QtWidgets.QLineEdit(self.centralwidget)
        self.firstInput.setGeometry(QtCore.QRect(80, 290, 350, 61))

        
        self.firsterase = QtWidgets.QPushButton(self.centralwidget)
        self.firsterase.setText("⌫")
        self.firsterase.setGeometry(QtCore.QRect(12, 290, 70, 61))
        self.firsterase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))


        self.seconderase = QtWidgets.QPushButton(self.centralwidget)
        self.seconderase.setText("⌫")
        self.seconderase.setGeometry(QtCore.QRect(12, 390, 70, 61))
        self.seconderase.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        
        self.firsterase.clicked.connect(self.clear1)
        self.seconderase.clicked.connect(self.clear2)

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.firstInput.setFont(font)
        self.firstInput.setObjectName("firstInput")
        self.firstInput.textChanged.connect(self.firstValue)
        self.secondInput = QtWidgets.QLineEdit(self.centralwidget)
        self.secondInput.setGeometry(QtCore.QRect(80, 390, 350, 61))
        self.secondInput.setReadOnly(True)
        self.firstOption.addItem("Feet (Ft)")
        self.secondOption.addItem("Feet (Ft)")
        self.firstOption.addItem("Yards (Yd)")
        self.secondOption.addItem("Yards (Yd)")
        self.firstOption.addItem("Kilometer (Km)")
        self.secondOption.addItem("Kilometer (Km)")
        self.firstOption.addItem("Miles (Mi)")
        self.secondOption.addItem("Miles (Mi)")

        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(False)
        font.setWeight(50)
        self.secondInput.setFont(font)
        self.secondInput.setProperty("value", 0)
        self.secondInput.setObjectName("secondInput")
        self.secondInput.setPlaceholderText("//Output")
        self.swapBtn = QtWidgets.QPushButton(self.centralwidget)
        self.swapBtn.setGeometry(QtCore.QRect(180, 480, 141, 61))
        self.swapBtn.clicked.connect(self.swap)
        self.swapBtn.setFont(font)

        font = QtGui.QFont()
        font.setPointSize(15)
        self.swapBtn.setFont(font)
        self.swapBtn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.swapBtn.setObjectName("swapBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.firstOption.currentIndexChanged.connect(self.firstValue)
        self.secondOption.currentIndexChanged.connect(self.firstValue)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def clear1(self):
        try:
            self.firstInput.setText("")
        except:
            pass
    
    def clear2(self):
        try:
            self.secondInput.setText("")
        except:
            pass
    
    def swap(self):
        first = self.firstOption.currentIndex()
        second = self.secondOption.currentIndex()

        self.firstOption.setCurrentIndex(second)
        self.secondOption.setCurrentIndex(first)

    def mainClick(self, index):
        if index == 0:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Feet")
            self.secondOption.addItem("Feet")
            self.firstOption.addItem("Yards")
            self.secondOption.addItem("Yards")
            self.firstOption.addItem("Kilometer")
            self.secondOption.addItem("Kilometer")
            self.firstOption.addItem("Miles")
            self.secondOption.addItem("Miles")
        elif index == 1:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Centimeter (cm)")
            self.secondOption.addItem("Centimeter (cm)")
            self.firstOption.addItem("Meter (m)")
            self.secondOption.addItem("Meter (m)")
            self.firstOption.addItem("Inches (in)")
            self.secondOption.addItem("Inches (in)")
            self.firstOption.addItem("Millimeter (mm)")
            self.secondOption.addItem("Millimeter (mm)")
            self.firstOption.addItem("Decimeter (dm)")
            self.secondOption.addItem("Decimeter (dm)")
        elif index == 2:
            self.firstOption.clear()
            self.secondOption.clear()
<<<<<<< HEAD
            self.firstOption.addItem("Square Centimeter (cm²)")
            self.secondOption.addItem("Square Centimeter (cm²)")
            self.firstOption.addItem("Square Meter (m²)")
            self.secondOption.addItem("Square Meter (m²)")
            self.firstOption.addItem("Square Inch (in²)")
            self.secondOption.addItem("Square Inch (in²)")
            self.firstOption.addItem("Square Millimeter (mm²)")
            self.secondOption.addItem("Square Millimeter (mm²)")
            self.firstOption.addItem("Square Decimeter (dm²)")
            self.secondOption.addItem("Square Decimeter (dm²)")
        elif index == 3:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Cubic Centimeter (cm³)")
            self.secondOption.addItem("Cubic Centimeter (cm³)")
            self.firstOption.addItem("Cubic Meter (m³)")
            self.secondOption.addItem("Cubic Meter (m³)")
            self.firstOption.addItem("Cubic Inch (in)")
            self.secondOption.addItem("Cubic Inch (in)")
            self.firstOption.addItem("Cubic Millimeter (mm³)")
            self.secondOption.addItem("Cubic Millimeter (mm³)")
            self.firstOption.addItem("Cubic Decimeter (dm³)")
            self.secondOption.addItem("Cubic Decimeter (dm³)")
=======
            self.firstOption.addItem("Square Centimeter (cm²)")
            self.secondOption.addItem("Square Centimeter (cm²)")
            self.firstOption.addItem("Square Meter (m²)")
            self.secondOption.addItem("Square Meter (m²)")
            self.firstOption.addItem("Square Inch (in²)")
            self.secondOption.addItem("Square Inch (in²)")
            self.firstOption.addItem("Square Millimeter (mm²)")
            self.secondOption.addItem("Square Millimeter (mm²)")
            self.firstOption.addItem("Square Decimeter (dm²)")
            self.secondOption.addItem("Square Decimeter (dm²)")
        elif index == 3:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Cubic Centimeter (cm³)")
            self.secondOption.addItem("Cubic Centimeter (cm³)")
            self.firstOption.addItem("Cubic Meter (m³)")
            self.secondOption.addItem("Cubic Meter (m³)")
            self.firstOption.addItem("Cubic Inch (in)")
            self.secondOption.addItem("Cubic Inch (in)")
            self.firstOption.addItem("Cubic Millimeter (mm³)")
            self.secondOption.addItem("Cubic Millimeter (mm³)")
            self.firstOption.addItem("Cubic Decimeter (dm³)")
            self.secondOption.addItem("Cubic Decimeter (dm³)")
>>>>>>> diffStyle
        elif index == 4:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Microsecond (μs)")
            self.secondOption.addItem("Microsecond (μs)")
            self.firstOption.addItem("Millisecond (ms)")
            self.secondOption.addItem("Millisecond (ms)")
            self.firstOption.addItem("Seconds (s)")
            self.secondOption.addItem("Seconds (s)")
            self.firstOption.addItem("Minutes (mins)")
            self.secondOption.addItem("Minutes (mins)")
            self.firstOption.addItem("Hours (hrs)")
            self.secondOption.addItem("Hours (hrs)")
        elif index == 5:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Grams (g)")
            self.secondOption.addItem("Grams (g)")
            self.firstOption.addItem("Centigrams (cg)")
            self.secondOption.addItem("Centigrams (cg)")
            self.firstOption.addItem("Milligrams (mg)")
            self.secondOption.addItem("Milligrams (mg)")
            self.firstOption.addItem("Decigrams (dg)")
            self.secondOption.addItem("Decigrams (dg)")
            self.firstOption.addItem("Kilograms (kg)")
            self.secondOption.addItem("Kilograms (kg)")
            self.firstOption.addItem("Pounds")
            self.secondOption.addItem("Pounds")
        elif index == 6:
            self.firstOption.clear()
            self.secondOption.clear()
            self.firstOption.addItem("Celsius (°C)")
            self.secondOption.addItem("Celsius (°C)")
            self.firstOption.addItem("Farenheit (°F)")
            self.secondOption.addItem("Farenheit (°F)")
            self.firstOption.addItem("Kelvin (K)")
            self.secondOption.addItem("Kelvin (K)")

    def firstValue(self):
        manager = dict(
                # Distance
                Feet = [1, 0.33333333, 0.0003048, 0.00018939],
                Yards = [3, 1, 0.000914, 0.000568],
                Kilometer = [0.0003048, 0.000914, 1, 1.609344],
                Miles = [0.00018939, 0.000568, 0.621371, 1],

                # Length
                Centimeter = [1, 0.01, 0.393701, 10, 0.1],
                Meter = [100, 1, 39.3701, 1000, 10],
                Inches = [2.54, 0.0254, 1, 25.4, 0.254],
                Millimeter = [0.1, 0.001, 0.0393701, 1, 0.01],
                Decimeter = [10, 0.1, 3.93701, 100, 1],

                # Area
                sqCentimeter = [1, 0.0001, 0.155, 100, 0.01],
                sqMeter = [10000, 1, 1550.0031, 1000000, 100],
                sqInches = [6.4516, 0.00064516, 1, 645.16, 0.064516],
                sqMillimeter = [0.01, 1e-06, 0.00155, 1, 0.0001],
                sqDecimeter = [100, 0.01, 15.5, 10000, 1],

                # Volume
                cbCentimeter = [1, 1e-06, 0.0610237, 1000, 0.001],
                cbMeter = [1000000, 1, 61023.7, 1000000000, 1000],
                cbInches = [16.3871, 1.63871e-05, 1, 16387.1, 0.0163871],
                cbMillimeter = [0.001, 1e-09, 6.10237e-05, 1, 1e-06],
                cbDecimeter = [1000, 0.001, 61.0237, 1000000, 1],

                # Time
                Microsecond = [1, 0.001, 1e-06, 1.6666667e-08, 2.77778e-10],
                Millisecond = [1000, 1, 0.001, 1.66667e-05, 2.77777778e-07],
                Second = [1000000, 1000, 1, 0.0166667, 0.000277778],
                Minute = [60000000, 60000, 60, 1, 0.0166667],
                Hour = [3600000000, 3600000, 3600, 60, 1],

                # Weight
                Gram = [1, 100, 1000, 10, 0.001, 0.00220462],
                Centigram = [0.01, 1, 10, 0.1, 1e-05, 2.20462e-05],
                Milligram = [0.001, 0.1, 1, 0.01, 1e-06, 2.20462e-06],
                Decigram = [0.1, 10, 100, 1, 0.0001, 0.000220462],
                Kilogram = [1000, 100000, 1000000, 10000, 1, 2.204623],
                Pounds = [453.5924, 45359.24, 453592.4, 4535.924, 0.453592, 1],
                )
        try:
<<<<<<< HEAD
            if self.mainSelector.currentIndex() == 0:
                match self.firstOption.currentIndex():
                    case 0:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Feet"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Yards"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Kilometer"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Miles"][self.secondOption.currentIndex()])))
=======
            self.status.setText("Good")
            self.status.setStyleSheet("color:lightgreen; font-family:'Fira Code'; font-weight:bold; font-size:20pt;")
            if self.mainSelector.currentIndex() == 0:
                match self.firstOption.currentIndex():
                    case 0:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Feet"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Yards"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Kilometer"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Miles"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle
            
            elif self.mainSelector.currentIndex() == 1:
                match self.firstOption.currentIndex():
                    case 0:
<<<<<<< HEAD
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Centimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Meter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Inches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Millimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Decimeter"][self.secondOption.currentIndex()])))
=======
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Centimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Meter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Inches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Millimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Decimeter"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle
                        
                
            elif self.mainSelector.currentIndex() == 2:
                match self.firstOption.currentIndex():
                    case 0:
<<<<<<< HEAD
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqCentimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqMeter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqInches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqMillimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqDecimeter"][self.secondOption.currentIndex()])))
=======
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqCentimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqMeter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqInches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqMillimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqDecimeter"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle

            elif self.mainSelector.currentIndex() == 3:
                match self.firstOption.currentIndex():
                    case 0:
<<<<<<< HEAD
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["cbCentimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["cbMeter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["cbInches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["cbMillimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["sqDecimeter"][self.secondOption.currentIndex()])))
=======
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["cbCentimeter"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["cbMeter"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["cbInches"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["cbMillimeter"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["sqDecimeter"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle

            elif self.mainSelector.currentIndex() == 4:
                match self.firstOption.currentIndex():
                    case 0:
<<<<<<< HEAD
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Microsecond"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Millisecond"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Second"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Minute"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Hour"][self.secondOption.currentIndex()])))
=======
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Microsecond"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Millisecond"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Second"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Minute"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Hour"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle
 
            elif self.mainSelector.currentIndex() == 5:
                match self.firstOption.currentIndex():
                    case 0:
<<<<<<< HEAD
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Gram"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Centigram"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Milligram"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Decigram"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Kilogram"][self.secondOption.currentIndex()])))
                    case 5:
                        self.secondInput.setText(str(int(self.firstInput.text()) * float(manager["Pounds"][self.secondOption.currentIndex()])))
=======
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Gram"][self.secondOption.currentIndex()])))
                    case 1:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Centigram"][self.secondOption.currentIndex()])))
                    case 2:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Milligram"][self.secondOption.currentIndex()])))
                    case 3:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Decigram"][self.secondOption.currentIndex()])))
                    case 4:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Kilogram"][self.secondOption.currentIndex()])))
                    case 5:
                        self.secondInput.setText(str(float(self.firstInput.text()) * float(manager["Pounds"][self.secondOption.currentIndex()])))
>>>>>>> diffStyle

            elif self.mainSelector.currentIndex() == 6:
                match self.firstOption.currentIndex():
                    case 0:
                        if self.secondOption.currentIndex() == 1:
<<<<<<< HEAD
                            self.secondInput.setText(str((int(self.firstInput.text()) * 9 / 5) + 32))
                        elif self.secondOption.currentIndex() == 2:
                            self.secondInput.setText(str(int(self.firstInput.text()) + 274.15))
=======
                            self.secondInput.setText(str((float(self.firstInput.text()) * 9 / 5) + 32))
                        elif self.secondOption.currentIndex() == 2:
                            self.secondInput.setText(str(float(self.firstInput.text()) + 274.15))
>>>>>>> diffStyle
                        else:
                            self.secondInput.setText(str(self.firstInput.text()))
                    case 1:
                        if self.secondOption.currentIndex() == 0:
<<<<<<< HEAD
                            self.secondInput.setText(str((int(self.firstInput.text()) - 32) / 1.8))
                        elif self.secondOption.currentIndex() == 2:
                            value = (int(self.firstInput.text()) - 32) / 1.8
=======
                            self.secondInput.setText(str((float(self.firstInput.text()) - 32) / 1.8))
                        elif self.secondOption.currentIndex() == 2:
                            value = (float(self.firstInput.text()) - 32) / 1.8
>>>>>>> diffStyle
                            self.secondInput.setText(str(value + 273.15))
                        else:
                            self.secondInput.setText(str(self.firstInput.text()))
                    case 2:
                        if self.secondOption.currentIndex() == 0:
<<<<<<< HEAD
                            self.secondInput.setText(str(int(self.firstInput.text()) - 273.15))
                        elif self.secondOption.currentIndex() == 1:
                            value = 1.8 * (int(self.firstInput.text()) - 273.15) + 32
=======
                            self.secondInput.setText(str(float(self.firstInput.text()) - 273.15))
                        elif self.secondOption.currentIndex() == 1:
                            value = 1.8 * (float(self.firstInput.text()) - 273.15) + 32
>>>>>>> diffStyle
                            self.secondInput.setText(str(value))
                        else:
                            self.secondInput.setText(str(self.firstInput.text()))
        except:
<<<<<<< HEAD
            pass
=======
            self.status.setText("Error")
            self.status.setStyleSheet("color:#F32929; font-family:'Fira Code'; font-weight:bold; font-size:20pt;")
>>>>>>> diffStyle

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ConverTool"))
        self.mainSelector.setItemText(0, _translate("MainWindow", "Distance 🚘"))
        self.mainSelector.setItemText(1, _translate("MainWindow", "Length 📏"))
        self.mainSelector.setItemText(2, _translate("MainWindow", "Area 📐"))
        self.mainSelector.setItemText(3, _translate("MainWindow", "Volume 🌊"))
        self.mainSelector.setItemText(4, _translate("MainWindow", "Time 🕒"))
        self.mainSelector.setItemText(5, _translate("MainWindow", "Weight 🏋️"))
        self.mainSelector.setItemText(6, _translate("MainWindow", "Temperature 🌡️"))
        self.swapBtn.setText(_translate("MainWindow", "Swap ⇌"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
