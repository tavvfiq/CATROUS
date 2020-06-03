# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_CATROUS(object):
    def setupUi(self, CATROUS):
        CATROUS.setObjectName("CATROUS")
        CATROUS.resize(1024, 640)
        CATROUS.setMinimumSize(QtCore.QSize(1024, 640))
        CATROUS.setMaximumSize(QtCore.QSize(1024, 640))
        CATROUS.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#c2d7e7;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(CATROUS)
        self.centralwidget.setMinimumSize(QtCore.QSize(1024, 640))
        self.centralwidget.setMaximumSize(QtCore.QSize(1024, 640))
        self.centralwidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.daftarPasien_widget = QtWidgets.QWidget(self.centralwidget)
        self.daftarPasien_widget.setGeometry(QtCore.QRect(0, 0, 1031, 641))
        self.daftarPasien_widget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#0bb6e4;\n"
"}")
        self.daftarPasien_widget.setObjectName("daftarPasien_widget")
        self.tabTitle = QtWidgets.QLabel(self.daftarPasien_widget)
        self.tabTitle.setGeometry(QtCore.QRect(390, 60, 221, 49))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.tabTitle.setFont(font)
        self.tabTitle.setStyleSheet("background-color:rgb(0,0,0,0);\n"
"color:#ffffff;")
        self.tabTitle.setObjectName("tabTitle")
        self.simpanData_btn = QtWidgets.QPushButton(self.daftarPasien_widget)
        self.simpanData_btn.setGeometry(QtCore.QRect(380, 520, 121, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.simpanData_btn.setFont(font)
        self.simpanData_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 0px;\n"
"background-color:#ffffff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5555ff;\n"
"border:0px;\n"
"color:#ffffff;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/resource/Add-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.simpanData_btn.setIcon(icon)
        self.simpanData_btn.setObjectName("simpanData_btn")
        self.label_7 = QtWidgets.QLabel(self.daftarPasien_widget)
        self.label_7.setGeometry(QtCore.QRect(380, 130, 251, 25))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridWidget = QtWidgets.QWidget(self.daftarPasien_widget)
        self.gridWidget.setGeometry(QtCore.QRect(300, 200, 401, 217))
        self.gridWidget.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setObjectName("gridLayout")
        self.label_10 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 1, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_17.setFont(font)
        self.label_17.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_17.setObjectName("label_17")
        self.gridLayout.addWidget(self.label_17, 2, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 5, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 6, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 4, 0, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 7, 0, 1, 1)
        self.nomorpasien_label = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.nomorpasien_label.setFont(font)
        self.nomorpasien_label.setStyleSheet("\n"
"    background-color:rgba(0,0,0,0);\n"
"")
        self.nomorpasien_label.setText("")
        self.nomorpasien_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nomorpasien_label.setObjectName("nomorpasien_label")
        self.gridLayout.addWidget(self.nomorpasien_label, 0, 1, 1, 1)
        self.namaTextEdit = QtWidgets.QLineEdit(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.namaTextEdit.setFont(font)
        self.namaTextEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    border-width:0px 0px 1px 0px;\n"
"    border-style:solid;\n"
"    border-color:grey;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border-width:0px 0px 3px 0px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}")
        self.namaTextEdit.setInputMask("")
        self.namaTextEdit.setFrame(True)
        self.namaTextEdit.setClearButtonEnabled(False)
        self.namaTextEdit.setObjectName("namaTextEdit")
        self.gridLayout.addWidget(self.namaTextEdit, 1, 1, 1, 1)
        self.jenisKelamin = QtWidgets.QComboBox(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.jenisKelamin.setFont(font)
        self.jenisKelamin.setStyleSheet("QComboBox{\n"
"background:#63cdda;\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}")
        self.jenisKelamin.setObjectName("jenisKelamin")
        self.jenisKelamin.addItem("")
        self.jenisKelamin.addItem("")
        self.gridLayout.addWidget(self.jenisKelamin, 2, 1, 1, 1)
        self.ttlTextEdit = QtWidgets.QLineEdit(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.ttlTextEdit.setFont(font)
        self.ttlTextEdit.setStyleSheet("QLineEdit\n"
"{\n"
"    border-width:0px 0px 1px 0px;\n"
"    border-style:solid;\n"
"    border-color:grey;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}\n"
"\n"
"QLineEdit:focus\n"
"{\n"
"    border-width:0px 0px 3px 0px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}")
        self.ttlTextEdit.setObjectName("ttlTextEdit")
        self.gridLayout.addWidget(self.ttlTextEdit, 3, 1, 1, 1)
        self.pekerjaanLineEdit = QtWidgets.QLineEdit(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.pekerjaanLineEdit.setFont(font)
        self.pekerjaanLineEdit.setStyleSheet("/*QLineEdit\n"
"{\n"
"    border: 1px solid grey;\n"
"    background-color:#63cdda;\n"
"border-radius: 10px;\n"
"}*/\n"
"QLineEdit\n"
"{\n"
"    border-width:0px 0px 1px 0px;\n"
"    border-style:solid;\n"
"    border-color:grey;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border-width:0px 0px 3px 0px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}")
        self.pekerjaanLineEdit.setObjectName("pekerjaanLineEdit")
        self.gridLayout.addWidget(self.pekerjaanLineEdit, 6, 1, 1, 1)
        self.golongan_darah = QtWidgets.QLineEdit(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.golongan_darah.setFont(font)
        self.golongan_darah.setStyleSheet("QLineEdit\n"
"{\n"
"    border-width:0px 0px 1px 0px;\n"
"    border-style:solid;\n"
"    border-color:grey;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}\n"
"QLineEdit:focus\n"
"{\n"
"    border-width:0px 0px 3px 0px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    background-color:rgba(0,0,0,0);\n"
"border-radius: 0px;\n"
"}")
        self.golongan_darah.setObjectName("golongan_darah")
        self.gridLayout.addWidget(self.golongan_darah, 5, 1, 1, 1)
        self.tanggalupdate_label = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.tanggalupdate_label.setFont(font)
        self.tanggalupdate_label.setStyleSheet("\n"
"    background-color:rgba(0,0,0,0);\n"
"")
        self.tanggalupdate_label.setText("")
        self.tanggalupdate_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tanggalupdate_label.setObjectName("tanggalupdate_label")
        self.gridLayout.addWidget(self.tanggalupdate_label, 7, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hari_combobox = QtWidgets.QComboBox(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setItalic(False)
        self.hari_combobox.setFont(font)
        self.hari_combobox.setStyleSheet("QComboBox{\n"
"background:#63cdda;\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}\n"
"")
        self.hari_combobox.setFrame(False)
        self.hari_combobox.setObjectName("hari_combobox")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.hari_combobox.addItem("")
        self.horizontalLayout.addWidget(self.hari_combobox)
        self.bulan_combobox = QtWidgets.QComboBox(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setItalic(False)
        self.bulan_combobox.setFont(font)
        self.bulan_combobox.setStyleSheet("QComboBox{\n"
"background:#63cdda;\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}")
        self.bulan_combobox.setFrame(False)
        self.bulan_combobox.setObjectName("bulan_combobox")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.bulan_combobox.addItem("")
        self.horizontalLayout.addWidget(self.bulan_combobox)
        self.tahun_combobox = QtWidgets.QComboBox(self.gridWidget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setItalic(False)
        self.tahun_combobox.setFont(font)
        self.tahun_combobox.setStyleSheet("QComboBox{\n"
"background:#63cdda;\n"
"border-radius:10px;\n"
"border: 1px solid grey;\n"
"}")
        self.tahun_combobox.setFrame(False)
        self.tahun_combobox.setObjectName("tahun_combobox")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.tahun_combobox.addItem("")
        self.horizontalLayout.addWidget(self.tahun_combobox)
        self.gridLayout.addLayout(self.horizontalLayout, 4, 1, 1, 1)
        self.unggahFoto_btn = QtWidgets.QPushButton(self.daftarPasien_widget)
        self.unggahFoto_btn.setGeometry(QtCore.QRect(520, 520, 111, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.unggahFoto_btn.setFont(font)
        self.unggahFoto_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border: 0px;\n"
"background-color:#ffffff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color:#5555ff;\n"
"border:0px;\n"
"color:#ffffff;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/img/resource/Image.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.unggahFoto_btn.setIcon(icon1)
        self.unggahFoto_btn.setObjectName("unggahFoto_btn")
        self.exit_btn_2 = QtWidgets.QPushButton(self.daftarPasien_widget)
        self.exit_btn_2.setGeometry(QtCore.QRect(10, 590, 41, 41))
        self.exit_btn_2.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}\n"
"    ")
        self.exit_btn_2.setText("")
        self.exit_btn_2.setFlat(True)
        self.exit_btn_2.setObjectName("exit_btn_2")
        self.back_btn = QtWidgets.QPushButton(self.daftarPasien_widget)
        self.back_btn.setGeometry(QtCore.QRect(60, 590, 41, 41))
        self.back_btn.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}\n"
"    ")
        self.back_btn.setText("")
        self.back_btn.setFlat(True)
        self.back_btn.setObjectName("back_btn")
        self.foto_label = QtWidgets.QLabel(self.daftarPasien_widget)
        self.foto_label.setGeometry(QtCore.QRect(320, 430, 361, 20))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(9)
        self.foto_label.setFont(font)
        self.foto_label.setStyleSheet("background-color:rgb(0,0,0,0);")
        self.foto_label.setText("")
        self.foto_label.setAlignment(QtCore.Qt.AlignCenter)
        self.foto_label.setObjectName("foto_label")
        self.bg1 = QtWidgets.QLabel(self.daftarPasien_widget)
        self.bg1.setGeometry(QtCore.QRect(290, 50, 421, 511))
        self.bg1.setStyleSheet("QLabel{\n"
"    background-color:#18dcff;\n"
"}")
        self.bg1.setText("")
        self.bg1.setObjectName("bg1")
        self.label_22 = QtWidgets.QLabel(self.daftarPasien_widget)
        self.label_22.setGeometry(QtCore.QRect(290, 50, 421, 71))
        self.label_22.setStyleSheet("QLabel{\n"
"background-color:#4b4b4b;\n"
"}")
        self.label_22.setText("")
        self.label_22.setObjectName("label_22")
        self.bg1.raise_()
        self.label_22.raise_()
        self.tabTitle.raise_()
        self.simpanData_btn.raise_()
        self.label_7.raise_()
        self.gridWidget.raise_()
        self.unggahFoto_btn.raise_()
        self.exit_btn_2.raise_()
        self.back_btn.raise_()
        self.foto_label.raise_()
        self.welcomeWidget = QtWidgets.QWidget(self.centralwidget)
        self.welcomeWidget.setGeometry(QtCore.QRect(0, 0, 1031, 641))
        self.welcomeWidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#0bb6e4;\n"
"}")
        self.welcomeWidget.setObjectName("welcomeWidget")
        self.logo = QtWidgets.QLabel(self.welcomeWidget)
        self.logo.setGeometry(QtCore.QRect(250, 210, 131, 121))
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.catrous_label = QtWidgets.QLabel(self.welcomeWidget)
        self.catrous_label.setGeometry(QtCore.QRect(390, 240, 361, 81))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(50)
        font.setBold(True)
        font.setWeight(75)
        self.catrous_label.setFont(font)
        self.catrous_label.setStyleSheet("color:#ffffff;")
        self.catrous_label.setObjectName("catrous_label")
        self.nomor_txtedit = QtWidgets.QLineEdit(self.welcomeWidget)
        self.nomor_txtedit.setGeometry(QtCore.QRect(350, 370, 331, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.nomor_txtedit.setFont(font)
        self.nomor_txtedit.setStyleSheet("QLineEdit{\n"
"background:#ffffff;\n"
"border-radius:10px;\n"
"}")
        self.nomor_txtedit.setText("")
        self.nomor_txtedit.setAlignment(QtCore.Qt.AlignCenter)
        self.nomor_txtedit.setObjectName("nomor_txtedit")
        self.masuk_btn = QtWidgets.QPushButton(self.welcomeWidget)
        self.masuk_btn.setGeometry(QtCore.QRect(407, 420, 91, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.masuk_btn.setFont(font)
        self.masuk_btn.setStyleSheet("QPushButton\n"
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/img/resource/User-1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.masuk_btn.setIcon(icon2)
        self.masuk_btn.setFlat(True)
        self.masuk_btn.setObjectName("masuk_btn")
        self.tambah_btn = QtWidgets.QPushButton(self.welcomeWidget)
        self.tambah_btn.setGeometry(QtCore.QRect(510, 420, 131, 27))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        self.tambah_btn.setFont(font)
        self.tambah_btn.setStyleSheet("QPushButton\n"
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
        self.tambah_btn.setIcon(icon)
        self.tambah_btn.setFlat(True)
        self.tambah_btn.setObjectName("tambah_btn")
        self.exit_btn_3 = QtWidgets.QPushButton(self.welcomeWidget)
        self.exit_btn_3.setGeometry(QtCore.QRect(10, 590, 41, 41))
        self.exit_btn_3.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}\n"
"    ")
        self.exit_btn_3.setText("")
        self.exit_btn_3.setFlat(True)
        self.exit_btn_3.setObjectName("exit_btn_3")
        self.error_label = QtWidgets.QLabel(self.welcomeWidget)
        self.error_label.setGeometry(QtCore.QRect(1030, 600, 301, 41))
        self.error_label.setStyleSheet("QLabel{\n"
"background-color:#4b4b4b;\n"
"color:#ffffff;\n"
"}")
        self.error_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_label.setObjectName("error_label")
        self.label_15 = QtWidgets.QLabel(self.welcomeWidget)
        self.label_15.setGeometry(QtCore.QRect(30, 20, 71, 71))
        self.label_15.setText("")
        self.label_15.setPixmap(QtGui.QPixmap(":/img/resource/ugm_logo.png"))
        self.label_15.setScaledContents(True)
        self.label_15.setObjectName("label_15")
        self.label_28 = QtWidgets.QLabel(self.welcomeWidget)
        self.label_28.setGeometry(QtCore.QRect(110, 20, 71, 71))
        self.label_28.setText("")
        self.label_28.setPixmap(QtGui.QPixmap(":/img/resource/ristekdikti.png"))
        self.label_28.setScaledContents(True)
        self.label_28.setObjectName("label_28")
        self.avatarWidget = QtWidgets.QWidget(self.centralwidget)
        self.avatarWidget.setGeometry(QtCore.QRect(-270, -10, 241, 651))
        self.avatarWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.avatarWidget.setMaximumSize(QtCore.QSize(261, 651))
        self.avatarWidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#252432;\n"
"}")
        self.avatarWidget.setObjectName("avatarWidget")
        self.avatar = QtWidgets.QLabel(self.avatarWidget)
        self.avatar.setGeometry(QtCore.QRect(60, 60, 120, 120))
        self.avatar.setStyleSheet("QLabel\n"
"{\n"
"    background-color:rgba(0,0,0,0);\n"
"    border:0px;\n"
"}")
        self.avatar.setFrameShape(QtWidgets.QFrame.Box)
        self.avatar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.avatar.setLineWidth(2)
        self.avatar.setText("")
        self.avatar.setObjectName("avatar")
        self.tile = QtWidgets.QLabel(self.avatarWidget)
        self.tile.setEnabled(True)
        self.tile.setGeometry(QtCore.QRect(0, 0, 241, 651))
        self.tile.setStyleSheet("QLabel\n"
"{\n"
"    background-color:#252432;\n"
"}")
        self.tile.setText("")
        self.tile.setObjectName("tile")
        self.logOut_btn = QtWidgets.QPushButton(self.avatarWidget)
        self.logOut_btn.setGeometry(QtCore.QRect(70, 600, 41, 41))
        self.logOut_btn.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}\n"
"    ")
        self.logOut_btn.setText("")
        self.logOut_btn.setFlat(True)
        self.logOut_btn.setObjectName("logOut_btn")
        self.exit_btn = QtWidgets.QPushButton(self.avatarWidget)
        self.exit_btn.setGeometry(QtCore.QRect(20, 600, 41, 41))
        self.exit_btn.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgba(255,0,0,200);\n"
"border:0px;\n"
"}\n"
"    ")
        self.exit_btn.setText("")
        self.exit_btn.setFlat(True)
        self.exit_btn.setObjectName("exit_btn")
        self.rekam_btn = QtWidgets.QPushButton(self.avatarWidget)
        self.rekam_btn.setGeometry(QtCore.QRect(120, 600, 41, 41))
        self.rekam_btn.setStyleSheet("QPushButton{\n"
"    background-color:white;\n"
"    border:0px;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color:rgb(85, 170, 0);\n"
"border:0px;\n"
"}\n"
"    ")
        self.rekam_btn.setText("")
        self.rekam_btn.setFlat(True)
        self.rekam_btn.setObjectName("rekam_btn")
        self.about_btn = QtWidgets.QPushButton(self.avatarWidget)
        self.about_btn.setGeometry(QtCore.QRect(170, 550, 41, 41))
        self.about_btn.setStyleSheet("QPushButton\n"
"{\n"
"    border:0px;\n"
"    background-color:white;\n"
"    border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:blue;\n"
"}")
        self.about_btn.setText("")
        self.about_btn.setAutoDefault(False)
        self.about_btn.setFlat(False)
        self.about_btn.setObjectName("about_btn")
        self.notes_btn = QtWidgets.QPushButton(self.avatarWidget)
        self.notes_btn.setGeometry(QtCore.QRect(170, 600, 41, 41))
        self.notes_btn.setStyleSheet("QPushButton\n"
"{\n"
"    background-color:#ffffff;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-color:blue;\n"
"}")
        self.notes_btn.setText("")
        self.notes_btn.setFlat(False)
        self.notes_btn.setObjectName("notes_btn")
        self.informasi = QtWidgets.QPushButton(self.avatarWidget)
        self.informasi.setGeometry(QtCore.QRect(0, 289, 240, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.informasi.setFont(font)
        self.informasi.setStyleSheet("QPushButton\n"
"{\n"
"color:#ffffff;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-width:0px 0px 0px 0px;\n"
"    border-style:solid;\n"
"    color:#5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border-width:0px 0px 0px 4px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    color: #5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}\n"
"QPushButton:focus\n"
"{\n"
"    border-width:0px 0px 0px 4px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    color: #5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}\n"
"")
        self.informasi.setIconSize(QtCore.QSize(32, 32))
        self.informasi.setCheckable(False)
        self.informasi.setFlat(True)
        self.informasi.setObjectName("informasi")
        self.galeri_rekam = QtWidgets.QPushButton(self.avatarWidget)
        self.galeri_rekam.setGeometry(QtCore.QRect(0, 340, 240, 50))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.galeri_rekam.setFont(font)
        self.galeri_rekam.setStyleSheet("QPushButton\n"
"{\n"
"color:#ffffff;\n"
"text-align:left;\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    border-width:0px 0px 0px 1px;\n"
"    border-style:solid;\n"
"    color:#5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}\n"
"QPushButton:pressed\n"
"{\n"
"    border-width:0px 0px 0px 4px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    color: #5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}\n"
"QPushButton:focus\n"
"{\n"
"    border-width:0px 0px 0px 4px;\n"
"    border-style:solid;\n"
"    border-color:#5500ff;\n"
"    color: #5500ff;\n"
"    background-color:rgba(0, 0, 0, 100);\n"
"}")
        self.galeri_rekam.setIconSize(QtCore.QSize(32, 32))
        self.galeri_rekam.setCheckable(False)
        self.galeri_rekam.setChecked(False)
        self.galeri_rekam.setFlat(True)
        self.galeri_rekam.setObjectName("galeri_rekam")
        self.nama_label = QtWidgets.QLabel(self.avatarWidget)
        self.nama_label.setGeometry(QtCore.QRect(0, 210, 241, 39))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.nama_label.setFont(font)
        self.nama_label.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"color:#ffffff;")
        self.nama_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nama_label.setObjectName("nama_label")
        self.tile.raise_()
        self.avatar.raise_()
        self.logOut_btn.raise_()
        self.exit_btn.raise_()
        self.rekam_btn.raise_()
        self.about_btn.raise_()
        self.notes_btn.raise_()
        self.informasi.raise_()
        self.galeri_rekam.raise_()
        self.nama_label.raise_()
        self.mainWidget = QtWidgets.QWidget(self.centralwidget)
        self.mainWidget.setGeometry(QtCore.QRect(0, 0, 1031, 641))
        self.mainWidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#0bb6e4;\n"
"}")
        self.mainWidget.setObjectName("mainWidget")
        self.stackedWidget = StackedWidget(self.mainWidget)
        self.stackedWidget.setGeometry(QtCore.QRect(260, 70, 751, 561))
        self.stackedWidget.setStyleSheet("QWidget\n"
"{\n"
"    background-color:#c2d7e7;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.informasi_widget = QtWidgets.QWidget()
        self.informasi_widget.setStyleSheet("QStackedWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}\n"
"QWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}")
        self.informasi_widget.setObjectName("informasi_widget")
        self.label_21 = QtWidgets.QLabel(self.informasi_widget)
        self.label_21.setGeometry(QtCore.QRect(0, 270, 159, 40))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label_21.setObjectName("label_21")
        self.horizontalWidget_2 = QtWidgets.QWidget(self.informasi_widget)
        self.horizontalWidget_2.setGeometry(QtCore.QRect(0, 0, 491, 281))
        self.horizontalWidget_2.setStyleSheet("background-color:#0bb6e4;")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.widget = QtWidgets.QWidget(self.horizontalWidget_2)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setText("Nomor :")
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.label_19 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setText("Tempat Lahir :")
        self.label_19.setObjectName("label_19")
        self.verticalLayout_2.addWidget(self.label_19)
        self.label_20 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setText("Tanggal, Tahun Lahir : ")
        self.label_20.setObjectName("label_20")
        self.verticalLayout_2.addWidget(self.label_20)
        self.label_8 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setText("Umur : ")
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.label_6 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setText("Jenis Kelamin : ")
        self.label_6.setObjectName("label_6")
        self.verticalLayout_2.addWidget(self.label_6)
        self.label_18 = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setText("Pekerjaan :")
        self.label_18.setObjectName("label_18")
        self.verticalLayout_2.addWidget(self.label_18)
        self.label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_3.addWidget(self.widget)
        self.widget1 = QtWidgets.QWidget(self.horizontalWidget_2)
        self.widget1.setObjectName("widget1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.nomor_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.nomor_label.setFont(font)
        self.nomor_label.setObjectName("nomor_label")
        self.verticalLayout_3.addWidget(self.nomor_label)
        self.tempat_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.tempat_label.setFont(font)
        self.tempat_label.setObjectName("tempat_label")
        self.verticalLayout_3.addWidget(self.tempat_label)
        self.ttl_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.ttl_label.setFont(font)
        self.ttl_label.setObjectName("ttl_label")
        self.verticalLayout_3.addWidget(self.ttl_label)
        self.umur_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.umur_label.setFont(font)
        self.umur_label.setObjectName("umur_label")
        self.verticalLayout_3.addWidget(self.umur_label)
        self.jenis_kelamin_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.jenis_kelamin_label.setFont(font)
        self.jenis_kelamin_label.setObjectName("jenis_kelamin_label")
        self.verticalLayout_3.addWidget(self.jenis_kelamin_label)
        self.pekerjaan_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.pekerjaan_label.setFont(font)
        self.pekerjaan_label.setObjectName("pekerjaan_label")
        self.verticalLayout_3.addWidget(self.pekerjaan_label)
        self.gol_darah_label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(12)
        self.gol_darah_label.setFont(font)
        self.gol_darah_label.setObjectName("gol_darah_label")
        self.verticalLayout_3.addWidget(self.gol_darah_label)
        self.horizontalLayout_3.addWidget(self.widget1)
        self.catatan_dokter_txtedit = QtWidgets.QTextEdit(self.informasi_widget)
        self.catatan_dokter_txtedit.setGeometry(QtCore.QRect(0, 310, 751, 251))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setItalic(False)
        self.catatan_dokter_txtedit.setFont(font)
        self.catatan_dokter_txtedit.setStyleSheet("QTextEdit{\n"
"    background:#82ccdd;\n"
"}")
        self.catatan_dokter_txtedit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.catatan_dokter_txtedit.setLineWidth(1)
        self.catatan_dokter_txtedit.setAutoFormatting(QtWidgets.QTextEdit.AutoAll)
        self.catatan_dokter_txtedit.setReadOnly(True)
        self.catatan_dokter_txtedit.setObjectName("catatan_dokter_txtedit")
        self.label_2 = QtWidgets.QLabel(self.informasi_widget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 751, 561))
        self.label_2.setStyleSheet("background-color:#0bb6e4;")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_2.raise_()
        self.horizontalWidget_2.raise_()
        self.label_21.raise_()
        self.catatan_dokter_txtedit.raise_()
        self.stackedWidget.addWidget(self.informasi_widget)
        self.rekam_widget = QtWidgets.QWidget()
        self.rekam_widget.setStyleSheet("QStackedWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}\n"
"QWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}")
        self.rekam_widget.setObjectName("rekam_widget")
        self.label_kosong = QtWidgets.QLabel(self.rekam_widget)
        self.label_kosong.setGeometry(QtCore.QRect(280, 220, 171, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_kosong.setFont(font)
        self.label_kosong.setAutoFillBackground(False)
        self.label_kosong.setStyleSheet("background-color: rgba(0,0,0,0%);")
        self.label_kosong.setObjectName("label_kosong")
        self.galeriView = QtWidgets.QTableWidget(self.rekam_widget)
        self.galeriView.setGeometry(QtCore.QRect(50, 30, 660, 490))
        self.galeriView.setMinimumSize(QtCore.QSize(660, 0))
        self.galeriView.setStyleSheet("QTableWidget{\n"
"background:#82ccdd;\n"
"}")
        self.galeriView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.galeriView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.galeriView.setTabKeyNavigation(False)
        self.galeriView.setProperty("showDropIndicator", False)
        self.galeriView.setDragDropOverwriteMode(False)
        self.galeriView.setIconSize(QtCore.QSize(320, 240))
        self.galeriView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.galeriView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.galeriView.setGridStyle(QtCore.Qt.NoPen)
        self.galeriView.setObjectName("galeriView")
        self.galeriView.setColumnCount(0)
        self.galeriView.setRowCount(0)
        self.galeriView.horizontalHeader().setVisible(False)
        self.galeriView.horizontalHeader().setDefaultSectionSize(325)
        self.galeriView.verticalHeader().setVisible(False)
        self.galeriView.verticalHeader().setDefaultSectionSize(245)
        self.label_3 = QtWidgets.QLabel(self.rekam_widget)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 751, 561))
        self.label_3.setStyleSheet("background-color:#0bb6e4;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.foto1 = qlabel_extended(self.rekam_widget)
        self.foto1.setGeometry(QtCore.QRect(270, -1, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.foto1.setFont(font)
        self.foto1.setStyleSheet("QLabel{\n"
"background-color:#82ccdd;\n"
"}")
        self.foto1.setAlignment(QtCore.Qt.AlignCenter)
        self.foto1.setObjectName("foto1")
        self.video1 = qlabel_extended(self.rekam_widget)
        self.video1.setGeometry(QtCore.QRect(360, -1, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setBold(True)
        font.setWeight(75)
        self.video1.setFont(font)
        self.video1.setStyleSheet("QLabel:hover{\n"
"background-color:#18dcff;\n"
"}")
        self.video1.setAlignment(QtCore.Qt.AlignCenter)
        self.video1.setObjectName("video1")
        self.label_3.raise_()
        self.galeriView.raise_()
        self.label_kosong.raise_()
        self.foto1.raise_()
        self.video1.raise_()
        self.stackedWidget.addWidget(self.rekam_widget)
        self.video_widget = QtWidgets.QWidget()
        self.video_widget.setStyleSheet("QStackedWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}\n"
"QWidget\n"
"{\n"
"    background-color:#3498db;\n"
"}")
        self.video_widget.setObjectName("video_widget")
        self.videoView = QtWidgets.QTableWidget(self.video_widget)
        self.videoView.setGeometry(QtCore.QRect(50, 30, 660, 490))
        self.videoView.setMinimumSize(QtCore.QSize(660, 0))
        self.videoView.setStyleSheet("QTableWidget{\n"
"background:#82ccdd;\n"
"}")
        self.videoView.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.videoView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.videoView.setTabKeyNavigation(False)
        self.videoView.setProperty("showDropIndicator", False)
        self.videoView.setDragDropOverwriteMode(False)
        self.videoView.setIconSize(QtCore.QSize(320, 240))
        self.videoView.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.videoView.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.videoView.setGridStyle(QtCore.Qt.NoPen)
        self.videoView.setObjectName("videoView")
        self.videoView.setColumnCount(0)
        self.videoView.setRowCount(0)
        self.videoView.horizontalHeader().setVisible(False)
        self.videoView.horizontalHeader().setDefaultSectionSize(325)
        self.videoView.verticalHeader().setVisible(False)
        self.videoView.verticalHeader().setDefaultSectionSize(245)
        self.label_4 = QtWidgets.QLabel(self.video_widget)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 751, 561))
        self.label_4.setStyleSheet("background-color:#0bb6e4;")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.no_video = QtWidgets.QLabel(self.video_widget)
        self.no_video.setGeometry(QtCore.QRect(270, 220, 201, 71))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.no_video.setFont(font)
        self.no_video.setStyleSheet("background-color:rgba(0,0,0,0);\n"
"")
        self.no_video.setObjectName("no_video")
        self.video2 = qlabel_extended(self.video_widget)
        self.video2.setGeometry(QtCore.QRect(360, -1, 91, 31))
        self.video2.setStyleSheet("QLabel{\n"
"background-color:#82ccdd;\n"
"}\n"
"")
        self.video2.setAlignment(QtCore.Qt.AlignCenter)
        self.video2.setObjectName("video2")
        self.foto2 = qlabel_extended(self.video_widget)
        self.foto2.setGeometry(QtCore.QRect(270, -1, 91, 31))
        self.foto2.setStyleSheet("QLabel:hover{\n"
"background-color:#18dcff;\n"
"}")
        self.foto2.setAlignment(QtCore.Qt.AlignCenter)
        self.foto2.setObjectName("foto2")
        self.label_4.raise_()
        self.videoView.raise_()
        self.no_video.raise_()
        self.video2.raise_()
        self.foto2.raise_()
        self.stackedWidget.addWidget(self.video_widget)
        self.label_23 = QtWidgets.QLabel(self.mainWidget)
        self.label_23.setGeometry(QtCore.QRect(240, 0, 791, 61))
        self.label_23.setStyleSheet("background-color:#485460;")
        self.label_23.setText("")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(self.mainWidget)
        self.label_24.setGeometry(QtCore.QRect(250, 5, 71, 65))
        self.label_24.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label_24.setText("")
        self.label_24.setPixmap(QtGui.QPixmap(":/img/resource/teeth.png"))
        self.label_24.setScaledContents(True)
        self.label_24.setObjectName("label_24")
        self.label_25 = QtWidgets.QLabel(self.mainWidget)
        self.label_25.setGeometry(QtCore.QRect(330, 10, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Trebuchet MS")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet("color:#ffffff;\n"
"background-color:rgba(0,0,0,0);")
        self.label_25.setObjectName("label_25")
        self.label_26 = QtWidgets.QLabel(self.mainWidget)
        self.label_26.setGeometry(QtCore.QRect(870, 0, 60, 60))
        self.label_26.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label_26.setText("")
        self.label_26.setPixmap(QtGui.QPixmap(":/img/resource/ugm_logo.png"))
        self.label_26.setScaledContents(True)
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(self.mainWidget)
        self.label_27.setGeometry(QtCore.QRect(930, 0, 91, 60))
        self.label_27.setStyleSheet("background-color:rgba(0,0,0,0);")
        self.label_27.setText("")
        self.label_27.setPixmap(QtGui.QPixmap(":/img/resource/ristekdikti.png"))
        self.label_27.setScaledContents(True)
        self.label_27.setObjectName("label_27")
        self.daftarPasien_widget.raise_()
        self.welcomeWidget.raise_()
        self.mainWidget.raise_()
        self.avatarWidget.raise_()
        CATROUS.setCentralWidget(self.centralwidget)

        self.retranslateUi(CATROUS)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(CATROUS)

    def retranslateUi(self, CATROUS):
        _translate = QtCore.QCoreApplication.translate
        CATROUS.setWindowTitle(_translate("CATROUS", "CATROUS"))
        self.tabTitle.setText(_translate("CATROUS", "Data Pasien"))
        self.simpanData_btn.setText(_translate("CATROUS", "Tambah Data"))
        self.label_7.setText(_translate("CATROUS", "Tambah Data Pasien"))
        self.label_10.setText(_translate("CATROUS", "Tempat Lahir"))
        self.label_16.setText(_translate("CATROUS", "Nama"))
        self.label_17.setText(_translate("CATROUS", "Jenis Kelamin"))
        self.label_14.setText(_translate("CATROUS", "Golongan Darah"))
        self.label_12.setText(_translate("CATROUS", "Pekerjaan"))
        self.label_11.setText(_translate("CATROUS", "Tanggal, Tahun lahir"))
        self.label_13.setText(_translate("CATROUS", "Tanggal penambahan :"))
        self.jenisKelamin.setItemText(0, _translate("CATROUS", "Laki-laki"))
        self.jenisKelamin.setItemText(1, _translate("CATROUS", "Perempuan"))
        self.label_9.setText(_translate("CATROUS", "Nomor Pasien"))
        self.hari_combobox.setItemText(0, _translate("CATROUS", "1"))
        self.hari_combobox.setItemText(1, _translate("CATROUS", "2"))
        self.hari_combobox.setItemText(2, _translate("CATROUS", "3"))
        self.hari_combobox.setItemText(3, _translate("CATROUS", "4"))
        self.hari_combobox.setItemText(4, _translate("CATROUS", "5"))
        self.hari_combobox.setItemText(5, _translate("CATROUS", "6"))
        self.hari_combobox.setItemText(6, _translate("CATROUS", "7"))
        self.hari_combobox.setItemText(7, _translate("CATROUS", "8"))
        self.hari_combobox.setItemText(8, _translate("CATROUS", "9"))
        self.hari_combobox.setItemText(9, _translate("CATROUS", "10"))
        self.hari_combobox.setItemText(10, _translate("CATROUS", "11"))
        self.hari_combobox.setItemText(11, _translate("CATROUS", "12"))
        self.hari_combobox.setItemText(12, _translate("CATROUS", "13"))
        self.hari_combobox.setItemText(13, _translate("CATROUS", "14"))
        self.hari_combobox.setItemText(14, _translate("CATROUS", "15"))
        self.hari_combobox.setItemText(15, _translate("CATROUS", "16"))
        self.hari_combobox.setItemText(16, _translate("CATROUS", "17"))
        self.hari_combobox.setItemText(17, _translate("CATROUS", "18"))
        self.hari_combobox.setItemText(18, _translate("CATROUS", "19"))
        self.hari_combobox.setItemText(19, _translate("CATROUS", "20"))
        self.hari_combobox.setItemText(20, _translate("CATROUS", "21"))
        self.hari_combobox.setItemText(21, _translate("CATROUS", "22"))
        self.hari_combobox.setItemText(22, _translate("CATROUS", "23"))
        self.hari_combobox.setItemText(23, _translate("CATROUS", "24"))
        self.hari_combobox.setItemText(24, _translate("CATROUS", "25"))
        self.hari_combobox.setItemText(25, _translate("CATROUS", "26"))
        self.hari_combobox.setItemText(26, _translate("CATROUS", "27"))
        self.hari_combobox.setItemText(27, _translate("CATROUS", "28"))
        self.hari_combobox.setItemText(28, _translate("CATROUS", "29"))
        self.hari_combobox.setItemText(29, _translate("CATROUS", "30"))
        self.hari_combobox.setItemText(30, _translate("CATROUS", "31"))
        self.bulan_combobox.setItemText(0, _translate("CATROUS", "1"))
        self.bulan_combobox.setItemText(1, _translate("CATROUS", "2"))
        self.bulan_combobox.setItemText(2, _translate("CATROUS", "3"))
        self.bulan_combobox.setItemText(3, _translate("CATROUS", "4"))
        self.bulan_combobox.setItemText(4, _translate("CATROUS", "5"))
        self.bulan_combobox.setItemText(5, _translate("CATROUS", "6"))
        self.bulan_combobox.setItemText(6, _translate("CATROUS", "7"))
        self.bulan_combobox.setItemText(7, _translate("CATROUS", "8"))
        self.bulan_combobox.setItemText(8, _translate("CATROUS", "9"))
        self.bulan_combobox.setItemText(9, _translate("CATROUS", "10"))
        self.bulan_combobox.setItemText(10, _translate("CATROUS", "11"))
        self.bulan_combobox.setItemText(11, _translate("CATROUS", "12"))
        self.tahun_combobox.setItemText(0, _translate("CATROUS", "2018"))
        self.tahun_combobox.setItemText(1, _translate("CATROUS", "2017"))
        self.tahun_combobox.setItemText(2, _translate("CATROUS", "2016"))
        self.tahun_combobox.setItemText(3, _translate("CATROUS", "2015"))
        self.tahun_combobox.setItemText(4, _translate("CATROUS", "2014"))
        self.tahun_combobox.setItemText(5, _translate("CATROUS", "2013"))
        self.tahun_combobox.setItemText(6, _translate("CATROUS", "2012"))
        self.tahun_combobox.setItemText(7, _translate("CATROUS", "2011"))
        self.tahun_combobox.setItemText(8, _translate("CATROUS", "2010"))
        self.tahun_combobox.setItemText(9, _translate("CATROUS", "2009"))
        self.tahun_combobox.setItemText(10, _translate("CATROUS", "2008"))
        self.tahun_combobox.setItemText(11, _translate("CATROUS", "2007"))
        self.tahun_combobox.setItemText(12, _translate("CATROUS", "2006"))
        self.tahun_combobox.setItemText(13, _translate("CATROUS", "2005"))
        self.tahun_combobox.setItemText(14, _translate("CATROUS", "2004"))
        self.tahun_combobox.setItemText(15, _translate("CATROUS", "2003"))
        self.tahun_combobox.setItemText(16, _translate("CATROUS", "2002"))
        self.tahun_combobox.setItemText(17, _translate("CATROUS", "2001"))
        self.tahun_combobox.setItemText(18, _translate("CATROUS", "2000"))
        self.tahun_combobox.setItemText(19, _translate("CATROUS", "1999"))
        self.tahun_combobox.setItemText(20, _translate("CATROUS", "1998"))
        self.tahun_combobox.setItemText(21, _translate("CATROUS", "1997"))
        self.tahun_combobox.setItemText(22, _translate("CATROUS", "1996"))
        self.tahun_combobox.setItemText(23, _translate("CATROUS", "1995"))
        self.tahun_combobox.setItemText(24, _translate("CATROUS", "1994"))
        self.tahun_combobox.setItemText(25, _translate("CATROUS", "1993"))
        self.tahun_combobox.setItemText(26, _translate("CATROUS", "1992"))
        self.tahun_combobox.setItemText(27, _translate("CATROUS", "1991"))
        self.tahun_combobox.setItemText(28, _translate("CATROUS", "1990"))
        self.tahun_combobox.setItemText(29, _translate("CATROUS", "1989"))
        self.tahun_combobox.setItemText(30, _translate("CATROUS", "1988"))
        self.tahun_combobox.setItemText(31, _translate("CATROUS", "1987"))
        self.unggahFoto_btn.setText(_translate("CATROUS", "Unggah Foto"))
        self.exit_btn_2.setToolTip(_translate("CATROUS", "<html><head/><body><p>Keluar</p></body></html>"))
        self.back_btn.setToolTip(_translate("CATROUS", "<html><head/><body><p>Kembali</p></body></html>"))
        self.catrous_label.setText(_translate("CATROUS", "CATROUS"))
        self.masuk_btn.setText(_translate("CATROUS", "Masuk"))
        self.tambah_btn.setText(_translate("CATROUS", "Tambah Pasien"))
        self.exit_btn_3.setToolTip(_translate("CATROUS", "<html><head/><body><p>Keluar</p></body></html>"))
        self.error_label.setText(_translate("CATROUS", "Nomor Pasien Tidak Ditemukan"))
        self.logOut_btn.setToolTip(_translate("CATROUS", "<html><head/><body><p>Ganti pasien</p></body></html>"))
        self.exit_btn.setToolTip(_translate("CATROUS", "<html><head/><body><p>Keluar</p></body></html>"))
        self.rekam_btn.setToolTip(_translate("CATROUS", "<html><head/><body><p>Rekam</p></body></html>"))
        self.about_btn.setToolTip(_translate("CATROUS", "<html><head/><body><p>Tentang</p></body></html>"))
        self.informasi.setText(_translate("CATROUS", "  Informasi"))
        self.galeri_rekam.setText(_translate("CATROUS", "  Galeri Rekam"))
        self.nama_label.setText(_translate("CATROUS", "Taufiq Widi Nugroho"))
        self.label_21.setText(_translate("CATROUS", "Catatan Dokter :"))
        self.label.setText(_translate("CATROUS", "Gol. Darah :"))
        self.nomor_label.setText(_translate("CATROUS", "TextLabel"))
        self.tempat_label.setText(_translate("CATROUS", "TextLabel"))
        self.ttl_label.setText(_translate("CATROUS", "TextLabel"))
        self.umur_label.setText(_translate("CATROUS", "TextLabel"))
        self.jenis_kelamin_label.setText(_translate("CATROUS", "TextLabel"))
        self.pekerjaan_label.setText(_translate("CATROUS", "TextLabel"))
        self.gol_darah_label.setText(_translate("CATROUS", "TextLabel"))
        self.label_kosong.setText(_translate("CATROUS", "Galeri Kosong"))
        self.foto1.setText(_translate("CATROUS", "Foto"))
        self.video1.setText(_translate("CATROUS", "Video"))
        self.no_video.setText(_translate("CATROUS", "Tidak ada video"))
        self.video2.setText(_translate("CATROUS", "Video"))
        self.foto2.setText(_translate("CATROUS", "Foto"))
        self.label_25.setText(_translate("CATROUS", "CATROUS"))

from StackedWidget import StackedWidget
from qlabel_extended import qlabel_extended
import resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CATROUS = QtWidgets.QMainWindow()
    ui = Ui_CATROUS()
    ui.setupUi(CATROUS)
    CATROUS.show()
    sys.exit(app.exec_())

