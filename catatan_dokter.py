# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'catatan_dokter.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_notesWindow(object):
    def setupUi(self, notesWindow):
        notesWindow.setObjectName("notesWindow")
        notesWindow.resize(360, 270)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(notesWindow.sizePolicy().hasHeightForWidth())
        notesWindow.setSizePolicy(sizePolicy)
        notesWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resource/teeth.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        notesWindow.setWindowIcon(icon)
        notesWindow.setStyleSheet("")
        self.catatanDokter = QtWidgets.QTextEdit(notesWindow)
        self.catatanDokter.setGeometry(QtCore.QRect(10, 60, 341, 161))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.catatanDokter.setFont(font)
        self.catatanDokter.setStyleSheet("QTextEdit{\n"
"background-color: #ffffff;\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}")
        self.catatanDokter.setFrameShape(QtWidgets.QFrame.Box)
        self.catatanDokter.setObjectName("catatanDokter")
        self.save_btn = QtWidgets.QPushButton(notesWindow)
        self.save_btn.setGeometry(QtCore.QRect(100, 230, 78, 27))
        self.save_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border:0px;\n"
"    background-color:#ffffff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(85, 85, 255);\n"
"color:#ffffff;\n"
"}")
        self.save_btn.setObjectName("save_btn")
        self.cancel_btn = QtWidgets.QPushButton(notesWindow)
        self.cancel_btn.setGeometry(QtCore.QRect(190, 230, 78, 27))
        self.cancel_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border:0px;\n"
"    background-color:#ffffff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:rgb(85, 85, 255);\n"
"color:#ffffff;\n"
"}")
        self.cancel_btn.setObjectName("cancel_btn")
        self.label = QtWidgets.QLabel(notesWindow)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 271))
        self.label.setStyleSheet("QLabel{\n"
"background-color:#0bb6e4;\n"
"border-radius:0px;\n"
"}")
        self.label.setText("")
        self.label.setObjectName("label")
        self.nama_dokter = QtWidgets.QLineEdit(notesWindow)
        self.nama_dokter.setGeometry(QtCore.QRect(120, 20, 231, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(False)
        font.setWeight(50)
        self.nama_dokter.setFont(font)
        self.nama_dokter.setStyleSheet("QLineEdit{\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}")
        self.nama_dokter.setObjectName("nama_dokter")
        self.label_3 = QtWidgets.QLabel(notesWindow)
        self.label_3.setGeometry(QtCore.QRect(10, 12, 91, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:#ffffff;")
        self.label_3.setObjectName("label_3")
        self.label.raise_()
        self.catatanDokter.raise_()
        self.save_btn.raise_()
        self.cancel_btn.raise_()
        self.nama_dokter.raise_()
        self.label_3.raise_()

        self.retranslateUi(notesWindow)
        QtCore.QMetaObject.connectSlotsByName(notesWindow)

    def retranslateUi(self, notesWindow):
        _translate = QtCore.QCoreApplication.translate
        notesWindow.setWindowTitle(_translate("notesWindow", "Catatan Dokter"))
        self.save_btn.setText(_translate("notesWindow", "Simpan"))
        self.cancel_btn.setText(_translate("notesWindow", "Batal"))
        self.label_3.setText(_translate("notesWindow", "Nama Dokter:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    notesWindow = QtWidgets.QWidget()
    ui = Ui_notesWindow()
    ui.setupUi(notesWindow)
    notesWindow.show()
    sys.exit(app.exec_())

