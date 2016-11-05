# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client_example1.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(898, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cameraScrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.cameraScrollArea.setWidgetResizable(True)
        self.cameraScrollArea.setObjectName("cameraScrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 806, 656))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.cameraScrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout.addWidget(self.cameraScrollArea)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rangeMaxLabel = QtWidgets.QLabel(self.centralwidget)
        self.rangeMaxLabel.setMinimumSize(QtCore.QSize(60, 0))
        self.rangeMaxLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeMaxLabel.setObjectName("rangeMaxLabel")
        self.verticalLayout.addWidget(self.rangeMaxLabel)
        self.rangeSlider = QVRangeSlider(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.rangeSlider.sizePolicy().hasHeightForWidth())
        self.rangeSlider.setSizePolicy(sizePolicy)
        self.rangeSlider.setObjectName("rangeSlider")
        self.verticalLayout.addWidget(self.rangeSlider)
        self.rangeMinLabel = QtWidgets.QLabel(self.centralwidget)
        self.rangeMinLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.rangeMinLabel.setObjectName("rangeMinLabel")
        self.verticalLayout.addWidget(self.rangeMinLabel)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.raLabel = QtWidgets.QLabel(self.centralwidget)
        self.raLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.raLabel.setObjectName("raLabel")
        self.horizontalLayout_2.addWidget(self.raLabel)
        self.raLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.raLineEdit.sizePolicy().hasHeightForWidth())
        self.raLineEdit.setSizePolicy(sizePolicy)
        self.raLineEdit.setObjectName("raLineEdit")
        self.horizontalLayout_2.addWidget(self.raLineEdit)
        self.decLabel = QtWidgets.QLabel(self.centralwidget)
        self.decLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.decLabel.setObjectName("decLabel")
        self.horizontalLayout_2.addWidget(self.decLabel)
        self.decLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decLineEdit.sizePolicy().hasHeightForWidth())
        self.decLineEdit.setSizePolicy(sizePolicy)
        self.decLineEdit.setObjectName("decLineEdit")
        self.horizontalLayout_2.addWidget(self.decLineEdit)
        self.exposureTimeLabel = QtWidgets.QLabel(self.centralwidget)
        self.exposureTimeLabel.setObjectName("exposureTimeLabel")
        self.horizontalLayout_2.addWidget(self.exposureTimeLabel)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.doubleSpinBox.setMinimumSize(QtCore.QSize(100, 0))
        self.doubleSpinBox.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.horizontalLayout_2.addWidget(self.doubleSpinBox)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.capturePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.capturePushButton.setObjectName("capturePushButton")
        self.horizontalLayout_2.addWidget(self.capturePushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 898, 25))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.menuFile.addAction(self.actionQuit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.rangeMaxLabel.setText(_translate("MainWindow", "NA"))
        self.rangeMinLabel.setText(_translate("MainWindow", "NA"))
        self.raLabel.setText(_translate("MainWindow", "RA:"))
        self.decLabel.setText(_translate("MainWindow", "DEC:"))
        self.exposureTimeLabel.setText(_translate("MainWindow", "Exposure Time (s):"))
        self.capturePushButton.setText(_translate("MainWindow", "Capture"))
        self.menuFile.setTitle(_translate("MainWindow", "Fi&le"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))

from qt5RangeSlider import QVRangeSlider
