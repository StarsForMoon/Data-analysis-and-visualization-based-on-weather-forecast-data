# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(695, 390)
        MainWindow.setMinimumSize(QtCore.QSize(695, 390))
        MainWindow.setMaximumSize(QtCore.QSize(710, 695))
        MainWindow.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 695, 315))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("img/背景图.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setAcceptDrops(True)
        self.toolBar.setIconSize(QtCore.QSize(48, 48))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.btn_1 = QtWidgets.QAction(MainWindow)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("img/图标-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_1.setIcon(icon)
        self.btn_1.setObjectName("btn_1")
        self.btn_2 = QtWidgets.QAction(MainWindow)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("img/图标-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_2.setIcon(icon1)
        self.btn_2.setObjectName("btn_2")
        self.btn_3 = QtWidgets.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("img/图标-3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_3.setIcon(icon2)
        self.btn_3.setObjectName("btn_3")
        self.btn_4 = QtWidgets.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("img/图标-4.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_4.setIcon(icon3)
        self.btn_4.setObjectName("btn_4")
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_1)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_2)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_3)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.btn_4)
        self.toolBar.addSeparator()
        self.toolBar.addSeparator()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.btn_1.setText(_translate("MainWindow", "温度变化可视化"))
        self.btn_1.setToolTip(_translate("MainWindow", "温度变化可视化"))
        self.btn_2.setText(_translate("MainWindow", "相对湿度变化可视化"))
        self.btn_2.setToolTip(_translate("MainWindow", "相对湿度变化可视化"))
        self.btn_3.setText(_translate("MainWindow", "降雨量变化可视化"))
        self.btn_3.setToolTip(_translate("MainWindow", "降雨量变化可视化"))
        self.btn_4.setText(_translate("MainWindow", "风向雷达图"))
        self.btn_4.setToolTip(_translate("MainWindow", "风向雷达图"))

