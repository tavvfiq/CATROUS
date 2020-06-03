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
        Rekam.resize(980, 660)
        Rekam.setMinimumSize(QtCore.QSize(980, 660))
        Rekam.setMaximumSize(QtCore.QSize(980, 660))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../../../../.designer/backup/resource/teeth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Rekam.setWindowIcon(icon)
        Rekam.setStyleSheet("background-color:#0bb6e4;")
        self.play_btn = QtWidgets.QPushButton(Rekam)
        self.play_btn.setGeometry(QtCore.QRect(20, 602, 41, 41))
        self.play_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:#ffffff;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#5555ff;\n"
"color:#ffffff;\n"
"}")
        self.play_btn.setText("")
        self.play_btn.setDefault(False)
        self.play_btn.setFlat(True)
        self.play_btn.setObjectName("play_btn")
        self.save_btn = QtWidgets.QPushButton(Rekam)
        self.save_btn.setGeometry(QtCore.QRect(120, 602, 41, 41))
        self.save_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:#ffffff;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#5555ff;\n"
"color:#ffffff;\n"
"}")
        self.save_btn.setText("")
        self.save_btn.setFlat(True)
        self.save_btn.setObjectName("save_btn")
        self.stop_btn = QtWidgets.QPushButton(Rekam)
        self.stop_btn.setGeometry(QtCore.QRect(70, 602, 41, 41))
        self.stop_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:#ffffff;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:#5555ff;\n"
"color:#ffffff;\n"
"}")
        self.stop_btn.setText("")
        self.stop_btn.setFlat(True)
        self.stop_btn.setObjectName("stop_btn")
        self.imageLabel = QtWidgets.QLabel(Rekam)
        self.imageLabel.setGeometry(QtCore.QRect(10, 10, 980, 640))
        self.imageLabel.setMinimumSize(QtCore.QSize(640, 480))
        self.imageLabel.setMaximumSize(QtCore.QSize(1280, 720))
        self.imageLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.imageLabel.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.imageLabel.setLineWidth(1)
        self.imageLabel.setText("")
        self.imageLabel.setObjectName("imageLabel")
        self.label = QtWidgets.QLabel(Rekam)
        self.label.setGeometry(QtCore.QRect(0, 0, 1044, 660))
        self.label.setStyleSheet("background-color:#0bb6e4;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.exit_btn = QtWidgets.QPushButton(Rekam)
        self.exit_btn.setGeometry(QtCore.QRect(919, 599, 41, 41))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    background-color:rgba(255, 85, 0, 100);\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}")
        self.exit_btn.setText("")
        self.exit_btn.setFlat(True)
        self.exit_btn.setObjectName("exit_btn")
        self.rekam_label = QtWidgets.QLabel(Rekam)
        self.rekam_label.setGeometry(QtCore.QRect(980, 0, 220, 41))
        self.rekam_label.setStyleSheet("QLabel{\n"
"background-color:#4b4b4b;\n"
"color:#ffffff;\n"
"}")
        self.rekam_label.setAlignment(QtCore.Qt.AlignCenter)
        self.rekam_label.setObjectName("rekam_label")
        self.label.raise_()
        self.imageLabel.raise_()
        self.play_btn.raise_()
        self.save_btn.raise_()
        self.stop_btn.raise_()
        self.exit_btn.raise_()
        self.rekam_label.raise_()

        self.retranslateUi(Rekam)
        QtCore.QMetaObject.connectSlotsByName(Rekam)

    def retranslateUi(self, Rekam):
        _translate = QtCore.QCoreApplication.translate
        Rekam.setWindowTitle(_translate("Rekam", "Rekam"))
        self.rekam_label.setText(_translate("Rekam", "Merekam..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Rekam = QtWidgets.QWidget()
    ui = Ui_Rekam()
    ui.setupUi(Rekam)
    Rekam.show()
    sys.exit(app.exec_())

