# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'progressbar.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(190, 390, 341, 91))
        self.progressBar.setMaximum(10)
        self.progressBar.setProperty("value", 2)
        self.progressBar.setObjectName("progressBar")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(100, 460, 581, 121))
        self.progressBar_2.setProperty("value", 24)
        self.progressBar_2.setObjectName("progressBar_2")
        self.start = QtWidgets.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(190, 330, 113, 32))
        self.start.setObjectName("start")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 70, 59, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(250, 100, 59, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 140, 59, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 170, 59, 16))
        self.label_5.setObjectName("label_5")
        self.set = QtWidgets.QPushButton(self.centralwidget)
        self.set.setGeometry(QtCore.QRect(280, 200, 113, 32))
        self.set.setObjectName("set")
        self.spinmin1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinmin1.setGeometry(QtCore.QRect(330, 70, 42, 22))
        self.spinmin1.setObjectName("spinmin1")
        self.spinmax1 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinmax1.setGeometry(QtCore.QRect(330, 100, 42, 22))
        self.spinmax1.setObjectName("spinmax1")
        self.spinmin2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinmin2.setGeometry(QtCore.QRect(330, 140, 42, 22))
        self.spinmin2.setObjectName("spinmin2")
        self.spinmax2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinmax2.setGeometry(QtCore.QRect(330, 170, 42, 22))
        self.spinmax2.setObjectName("spinmax2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.set.clicked.connect(self.setProgress)

        self.start.clicked.connect(self.addProgress)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def setProgress(self):
        self.progressBarMin = int(self.spinmin1.text())
        self.progressBarMax = int(self.spinmax1.text())
        self.progressBar2Min = int(self.spinmin2.text())
        self.progressBar2Max = int(self.spinmax2.text())
        self.progressBar.setValue(0)
        self.progressBar_2.setValue(0)
        self.progressBar.setMinimum(self.progressBarMin)
        self.progressBar.setMaximum(self.progressBarMax)
        self.progressBar_2.setMinimum(self.progressBar2Min)
        self.progressBar_2.setMaximum(self.progressBar2Max)

    def addProgress(self):
        if self.progressBar.value() != self.progressBarMax:
            self.progressBar.setValue(self.progressBar.value()+1)
        elif self.progressBar_2.value() != self.progressBar2Max:
            self.progressBar.setValue(0)
            self.progressBar_2.setValue(self.progressBar_2.value()+1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.start.setText(_translate("MainWindow", "start"))
        self.label_2.setText(_translate("MainWindow", "min1"))
        self.label_3.setText(_translate("MainWindow", "max1"))
        self.label_4.setText(_translate("MainWindow", "min2"))
        self.label_5.setText(_translate("MainWindow", "max2"))
        self.set.setText(_translate("MainWindow", "set"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
