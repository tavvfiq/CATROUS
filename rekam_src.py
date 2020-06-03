# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videoWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Rekam(object):
    def setupUi(self, Rekam):
        Rekam.setObjectName("Rekam")
        Rekam.resize(640, 480)
        Rekam.setMinimumSize(QtCore.QSize(640, 480))
        Rekam.setMaximumSize(QtCore.QSize(640, 480))
        self.playButton = QtWidgets.QPushButton(Rekam)
        self.playButton.setGeometry(QtCore.QRect(10, 450, 78, 27))
        self.playButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(224, 224, 224,200);\n"
"    border: 1px rgb(0,0,0,150);\n"
"}")
        self.playButton.setDefault(False)
        self.playButton.setFlat(True)
        self.playButton.setObjectName("playButton")
        self.saveButton = QtWidgets.QPushButton(Rekam)
        self.saveButton.setGeometry(QtCore.QRect(165, 450, 78, 27))
        self.saveButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(85, 85, 255,200);\n"
"    border: 1px rgb(0,0,0,150);\n"
"}")
        self.saveButton.setFlat(True)
        self.saveButton.setObjectName("saveButton")
        self.stopButton = QtWidgets.QPushButton(Rekam)
        self.stopButton.setGeometry(QtCore.QRect(87, 450, 78, 27))
        self.stopButton.setStyleSheet("QPushButton{\n"
"    background-color:rgb(228, 76, 0,250);\n"
"    border: 1px rgb(0,0,0,150);\n"
"}")
        self.stopButton.setFlat(True)
        self.stopButton.setObjectName("stopButton")
        self.imageLabel = QtWidgets.QLabel(Rekam)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.imageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.imageLabel.setMaximumSize(QtCore.QSize(640, 480))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.Panel)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageLabel.setLineWidth(1)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.raise_()
        self.playButton.raise_()
        self.saveButton.raise_()
        self.stopButton.raise_()

        self.retranslateUi(Rekam)
        QtCore.QMetaObject.connectSlotsByName(Rekam)

    def retranslateUi(self, Rekam):
        _translate = QtCore.QCoreApplication.translate
        Rekam.setWindowTitle(_translate("Rekam", "Rekam"))
        self.playButton.setText(_translate("Rekam", "Play"))
        self.saveButton.setText(_translate("Rekam", "Save"))
        self.stopButton.setText(_translate("Rekam", "Stop"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rekam = QtWidgets.QWidget()
    ui = Ui_Rekam()
    ui.setupUi(Rekam)
    Rekam.show()
    sys.exit(app.exec_())

