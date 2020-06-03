from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.uic import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from mainUI import *
from rekamWindow import *
from catatan_dokter import *
from shutil import *
import resource_rc
import sys, os, io
from datetime import datetime
import numpy as np
import cv2
import random, glob
from PIL import Image
import time
#from ffvideo import VideoStream
from ffmpy import FFmpeg
import six
import appdirs

class captureVideo(QThread):
    changePixmap = pyqtSignal(QPixmap)
    global filename, video_name
    Port = 0

    def __init__(self, parent=None):
        QThread.__init__(self, parent=parent)
        self.karies = np.array([0, 0, 90])
        self.threshold = 40
        self.karies_lowerBound = np.array([self.karies[0] - self.threshold, self.karies[1] - self.threshold, self.karies[2] - self.threshold])
        self.karies_upperBound = np.array([self.karies[0] + self.threshold, self.karies[1] + self.threshold, self.karies[2] + self.threshold])
        self.font = cv2.FONT_HERSHEY_SIMPLEX
        self.kernelOpen=np.ones((5,5))
        self.kernelClose=np.ones((20,20))
        self.isSaving = False
        self.isRecording = False
        self.keluar = False

    def trigSaveFrame(self):
        self.isSaving = True

    def trigKeluar(self):
        self.keluar = True

    def stopRecord(self):
        if self.isRecording == True:
            self.out.release()
            self.isRecording = False
        else:
            pass

    def trigStartRecord(self):
        self.out = cv2.VideoWriter(self.video_name,cv2.VideoWriter_fourcc('M','J','P','G'), 7, (self.frame_width,self.frame_height), True)
        self.isRecording = True

    def recordVideo(self, frame):
        #delay = 1/self.fps
        #time.sleep(delay)
        self.out.write(frame)

    def saveFrame(self, image):
        path = self.filename
        if self.filename:
            cv2.imwrite(path, image)
            self.isSaving = False
        else:
            print ("ERROR")

    def deteksi_karies(self, image):
        mask_karies = cv2.inRange(image, self.karies_lowerBound,self.karies_upperBound)
        maskOpen=cv2.morphologyEx(mask_karies,cv2.MORPH_OPEN,self.kernelOpen)
        maskClose=cv2.morphologyEx(maskOpen,cv2.MORPH_CLOSE,self.kernelClose)
        _, conts, h = cv2.findContours(maskClose, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
        for i in range(len(conts)):
            x,y,w,h=cv2.boundingRect(conts[i])
            area = cv2.contourArea(conts[i])
            if area > 300:
                cv2.rectangle(image,(x,y),(x+w,y+h),(0,0,255), 2)
                cv2.putText(image, "karies",(x,y+h),self.font,0.7, (0,255,255))

    def run(self):
        self.cap = cv2.VideoCapture(self.Port)
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.cap.set(cv2.CAP_PROP_FPS, self.fps)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,1280)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,720)
        self.frame_width = int(self.cap.get(3))
        self.frame_height = int(self.cap.get(4))
        print(self.frame_width)
        print(self.frame_height)
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            #flippedImg = cv2.flip(frame, 1)
            vflip = cv2.flip(frame, 0)
            #if self.keluar == True:
            #    self.keluar = False
            #    break
            if self.isRecording == True:
                self.recordVideo(vflip)
            if self.isSaving == True:
                self.isSaving = False
                self.saveFrame(vflip)
            #self.deteksi_karies(flippedImg)
            rgbImage = cv2.cvtColor(vflip, cv2.COLOR_BGR2RGB)
            convertToQtFormat = QImage(rgbImage.data, rgbImage.shape[1], rgbImage.shape[0], QImage.Format_RGB888)
            convertToQtFormat = QPixmap.fromImage(convertToQtFormat)
            p = convertToQtFormat.scaled(1280, 720, Qt.KeepAspectRatio)
            self.changePixmap.emit(p)
        #self.exec_()

class video_window(QWidget):
    def __init__(self, path):
        super(video_window, self).__init__()
        self.createVideoWindow(path)

    def createVideoWindow(self, path):
        self.video = QWidget()
        self.video.setGeometry(0, 0, 640, 480)
        self.video.setWindowTitle(str(path))
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.viewer = QVideoWidget(self.video)
        self.play_button = QPushButton()
        self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.play_button.clicked.connect(self.play)
        self.label_duration = QLabel()
        self.pos_slider = QSlider(Qt.Horizontal)
        self.pos_slider.setRange(0,0)
        self.pos_slider.sliderMoved.connect(self.setPos)
        self.control_layout = QHBoxLayout()
        self.control_layout.setContentsMargins(10,0,10,5)
        self.control_layout.addWidget(self.play_button)
        self.control_layout.addWidget(self.pos_slider)
        self.control_layout.addWidget(self.label_duration)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(self.viewer)
        self.layout.addLayout(self.control_layout)
        self.video.setLayout(self.layout)
        self.player.stateChanged.connect(self.mediaStateChanged)
        self.player.positionChanged.connect(self.positionChanged)
        self.player.durationChanged.connect(self.durationChanged)
        url= QUrl.fromLocalFile(str(path))
        content= QMediaContent(url)
        self.player.setVideoOutput(self.viewer)
        self.player.setMedia(content)
        self.player.play()
        self.video.show()

    def play(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def mediaStateChanged(self, state):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.play_button.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.pos_slider.setValue(position)
        time = position/1000
        self.label_duration.setText(str(time))

    def durationChanged(self, duration):
        self.pos_slider.setRange(0, duration)

    def setPos(self, position):
        self.player.setPosition(position)

class App(QMainWindow):
    global style_awal, style_akhir, avatar_ico_default
    avatar_ico_default = ':/img/resource/user_ico.png'
    style_awal = "QPushButton{color:#FFFFFF;text-align:left;}QPushButton:hover{color:#5500ff;background-color:rgba(0, 0, 0, 100);}"
    style_akhir = "QPushButton{border-width:0px 0px 0px 4px;border-style:solid;border-color:#5500ff;color: #5500ff;background-color:rgba(0, 0, 0, 100);}"

    def __init__(self):
        super(App, self).__init__()
        self.makedir_and_file()
        self.init_mainUI()
        self.init_rekamUI()
        self.init_catatan_dokter()

    def init_mainUI(self):
        self.CATROUS = QMainWindow()
        self.main_UI = Ui_CATROUS()
        self.main_UI.setupUi(self.CATROUS)
        self.CATROUS.setWindowIcon(QIcon(QPixmap(':img/resource/teeth.png')))
        #self.CATROUS.setWindowFlag(Qt.FramelessWindowHint, True)
        self.main_UI.daftarPasien_widget.setVisible(False)
        self.main_UI.mainWidget.setVisible(False)
        self.main_UI.avatarWidget.setVisible(False)
        self.show_welcomeWidget_content()
        self.main_UI.logOut_btn.setIcon(QIcon(QPixmap(':/img/resource/exit.png')))
        self.main_UI.about_btn.setIcon(QIcon(QPixmap(':/img/resource/information-button.png')))
        self.main_UI.notes_btn.setIcon(QIcon(QPixmap(':/img/resource/notes.png')))
        self.main_UI.exit_btn.setIcon(QIcon(QPixmap(':img/resource/clear-button.png')))
        self.main_UI.exit_btn_2.setIcon(QIcon(QPixmap(':img/resource/clear-button.png')))
        self.main_UI.exit_btn_3.setIcon(QIcon(QPixmap(':img/resource/clear-button.png')))
        self.main_UI.rekam_btn.setIcon(QIcon(QPixmap(':img/resource/rekam.png')))
        self.main_UI.back_btn.setIcon(QIcon(QPixmap(':img/resource/back.png')))
        self.main_UI.informasi.setIcon(QIcon(QPixmap(':img/resource/user_mime.png')))
        self.main_UI.galeri_rekam.setIcon(QIcon(QPixmap(':img/resource/folder_mime.png')))
        self.main_UI.galeriView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.main_UI.videoView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.main_UI.logOut_btn.clicked.connect(self.show_welcomeWidget_content)
        self.main_UI.tambah_btn.clicked.connect(self.show_daftarPasien)
        self.main_UI.masuk_btn.clicked.connect(self.show_mainWidget_content)
        self.main_UI.informasi.clicked.connect(self.tampil_informasi)
        self.main_UI.galeri_rekam.clicked.connect(self.tampil_rekam)
        self.main_UI.about_btn.clicked.connect(self.about)
        self.main_UI.exit_btn.clicked.connect(sys.exit)
        self.main_UI.exit_btn_2.clicked.connect(sys.exit)
        self.main_UI.exit_btn_3.clicked.connect(sys.exit)
        self.main_UI.back_btn.clicked.connect(self.show_welcomeWidget_content)
        self.main_UI.rekam_btn.clicked.connect(self.show_rekam_window)
        self.main_UI.notes_btn.clicked.connect(self.show_catatan_dokter)
        self.main_UI.unggahFoto_btn.clicked.connect(self.unggah_foto)
        self.main_UI.simpanData_btn.clicked.connect(self.simpan_data)
        self.main_UI.foto1.clicked.connect(self.tampil_rekam)
        self.main_UI.video1.clicked.connect(self.tampil_video)
        self.main_UI.foto2.clicked.connect(self.tampil_rekam)
        self.main_UI.video2.clicked.connect(self.tampil_video)
        self.main_UI.galeriView.itemDoubleClicked.connect(self.galeryView_dbClick)
        self.main_UI.videoView.itemDoubleClicked.connect(self.videoView_dbClick)
        self.foto = ""
        self.time_now = QTimer(self)
        self.time_now.setInterval(1000)
        self.time_now.timeout.connect(self.update_time)
        self.time_now.start()
        self.CATROUS.show()

    def init_rekamUI(self):
        self.rekam_window = QMainWindow()
        self.rekam_UI = Ui_Rekam()
        self.rekam_UI.setupUi(self.rekam_window)
        self.rekamThread = captureVideo()
        #self.rekam_window.setWindowFlag(Qt.FramelessWindowHint, True)
        self.rekam_UI.play_btn.setIcon(QIcon(QPixmap(':img/resource/play-video.png')))
        self.rekam_UI.stop_btn.setIcon(QIcon(QPixmap(':img/resource/stop-video.png')))
        self.rekam_UI.save_btn.setIcon(QIcon(QPixmap(':img/resource/save-video.png')))
        self.rekam_UI.exit_btn.setIcon(QIcon(QPixmap(':img/resource/clear-button.png')))
        self.rekamThread.changePixmap.connect(self.rekam_UI.imageLabel.setPixmap)
        self.rekam_UI.play_btn.clicked.connect(self.startVideo)
        self.rekam_UI.stop_btn.clicked.connect(self.stopVideo)
        self.rekam_UI.save_btn.clicked.connect(self.simpan_gambar)
        self.rekam_UI.exit_btn.clicked.connect(self.keluar_rekam)

    def init_catatan_dokter(self):
        self.notes_window = QMainWindow()
        self.notes_UI = Ui_notesWindow()
        self.notes_UI.setupUi(self.notes_window)
        #self.notes_window.setWindowFlag(Qt.FramelessWindowHint, True)
        self.notes_UI.save_btn.setIcon(QIcon(QPixmap(':img/resource/save-video.png')))
        self.notes_UI.cancel_btn.setIcon(QIcon(QPixmap(':img/resource/clear-button.png')))
        self.notes_UI.save_btn.clicked.connect(self.add_catatan_dokter)
        self.notes_UI.cancel_btn.clicked.connect(self.notes_window.close)

    def galeryView_dbClick(self, item):
        col = self.main_UI.galeriView.currentColumn()
        row = self.main_UI.galeriView.currentRow()
        im = Image.open(item.text())
        width, height = im.size
        path = item.text()
        self.createImageWindow(width, height, path)

    def videoView_dbClick(self, item):
        col = self.main_UI.videoView.currentColumn()
        row = self.main_UI.videoView.currentRow()
        thumbnail = item.text().replace(".jpg","")
        self.createVideoWindow(thumbnail)

    def show_catatan_dokter(self):
        self. notes_UI.catatanDokter.clear()
        self.notes_window.show()

    def show_rekam_window(self):
        self.rekamThread.start()
        self.rekam_window.show()

    def keluar_rekam(self):
        self.rekamThread.trigKeluar()
        self.rekam_window.close()

    def startVideo(self):
        self.makeFileAVI()
        self.rekamThread.trigStartRecord()
        self.rekam_UI.rekam_label.setText("Merekam...")
        self.slideAnim(self.rekam_UI.rekam_label, 760,0)
        #message = QMessageBox()
        #message.warning(self.rekam_window, "Perhatian", "Mulai merekam!")

    def stopVideo(self):
        if self.rekamThread.isRecording == True:
            self.slideAnim(self.rekam_UI.rekam_label, 980,0)
            vid_dir = self._dir + '/' + self.current_pasien + '/rekam/video'
            thumbnail_list = vid_dir + '/thumb.dat'
            #thumbnail = VideoStream(str(self.rekamThread.video_name)).get_frame_at_sec(1).image()
            #thumbnail.save(str(self.rekamThread.video_name) + '.jpg')
            thumbnail_path = str(self.rekamThread.video_name) + '.jpg'
            thumbnail = FFmpeg(inputs={str(self.rekamThread.video_name):None}, outputs={thumbnail_path: ['-ss', '00:00:2','-vframes','1']})
            thumbnail.run()
            #ffmpeg('-y', '-vf', '-vframes', '1', thumbnail_path,'-i', str(self.rekamThread.video_name))
            with open(thumbnail_list, 'a') as f:
                filedata = thumbnail_path
                filedata = str(filedata) + "\n"
                f.write(filedata)
            message = QMessageBox()
            message.warning(self.rekam_window, "Perhatian", "Video disimpan!")
        self.rekamThread.stopRecord()

    def simpan_gambar(self):
        self.makeFileIMG()
        self.rekamThread.trigSaveFrame()
        message = QMessageBox()
        message.warning(self.rekam_window, "Perhatian", "Berhasil disimpan!")

    def update_time(self):
        self.main_UI.tanggalupdate_label.setText(QDateTime.currentDateTime().toString())
        self.main_UI.nomorpasien_label.setText(self.random_number + str(self.main_UI.hari_combobox.currentText()) + str(self.main_UI.bulan_combobox.currentText()) + str(self.main_UI.tahun_combobox.currentText()))

    def tampil_informasi(self):
        self.main_UI.informasi.setStyleSheet(style_akhir)
        self.main_UI.galeri_rekam.setStyleSheet(style_awal)
        #self.main_UI.diagnosa.setStyleSheet(style_awal)
        self.main_UI.stackedWidget.setCurrentIndex(0)
        self.tampil_catatan_dokter()

    def tampil_rekam(self):
        self.main_UI.informasi.setStyleSheet(style_awal)
        self.main_UI.galeri_rekam.setStyleSheet(style_akhir)
        #self.main_UI.diagnosa.setStyleSheet(style_awal)
        self.main_UI.stackedWidget.setCurrentIndex(1)
        self.show_picture()

    def tampil_video(self):
        self.main_UI.stackedWidget.setCurrentIndex(2)
        self.show_thumbnail()

    def makedir_and_file(self):
        self._dir = os.path.join(os.getcwd(), 'profile')
        if not os.path.exists(self._dir):
            os.makedirs(self._dir)
        self.pasien_list = self._dir + '/pasien.list'
        try:
            openFile = open(self.pasien_list, 'r')
            openFile.close()
        except IOError:
            openFile = open(self.pasien_list, 'w')
            openFile.close()

    def drawShadow(self):
        effect = QGraphicsDropShadowEffect()
        effect.setColor(QColor(0,0,0,80))
        effect.setBlurRadius(5)
        effect.setXOffset(2)
        effect.setYOffset(2)
        return effect

    def simpan_data(self):
        if self.main_UI.namaTextEdit.text() == "":
            message = QMessageBox()
            message.warning(self, "Perhatian", "Nama masih kosong!")
        else:
            with open(self.pasien_list, 'a') as f:
                filedata = self.main_UI.nomorpasien_label.text()
                filedata = str(filedata) + "\n"
                f.write(filedata)
            dir_name = self._dir + '/' + self.main_UI.nomorpasien_label.text()
            img_dir = self._dir + '/' + self.main_UI.nomorpasien_label.text() + '/rekam'
            vid_dir = self._dir + '/' + self.main_UI.nomorpasien_label.text() + '/rekam/video'
            self.makeDirectory(dir_name)
            self.makeDirectory(img_dir)
            self.makeDirectory(vid_dir)
            fname = dir_name + '/data.dat'
            fnotes = dir_name + '/catatan_dokter.dat'
            img_list = img_dir + '/list.dat'
            vid_list = vid_dir + '/list.dat'
            self.thumbnail_list = vid_dir + '/thumb.dat'
            with open(img_list, 'a') as f:
                f.write("")
            with open(vid_list, 'a') as f:
                f.write("")
            with open(self.thumbnail_list, 'a') as f:
                f.write("")
            with open(fnotes, 'a') as f:
                f.write("")
            with open(fname, 'w') as f:
                filedata = self.main_UI.nomorpasien_label.text()
                filedata = str(filedata) + "\n"
                f.write(filedata)
                filedata = self.main_UI.namaTextEdit.text()
                filedata = str(filedata) + "\n"
                f.write(filedata)
                filedata = self.main_UI.jenisKelamin.currentText()
                filedata = str(filedata) + "\n"
                f.write(filedata)
                filedata = self.main_UI.ttlTextEdit.text()
                filedata = str(filedata) + "\n"
                f.write(filedata)
                filedata = str(self.main_UI.hari_combobox.currentText()) + '-' + str(self.main_UI.bulan_combobox.currentText()) + '-' + str(self.main_UI.tahun_combobox.currentText())
                filedata = filedata + "\n"
                f.write(filedata)
                umur_tahun = int(datetime.now().year) - int(self.main_UI.tahun_combobox.currentText())
                #umur_bulan = int(datetime.now().month) - int(self.main_UI.bulan_combobox.currentText())
                #umur_hari = int(datetime.now().day) - int(self.main_UI.hari_combobox.currentText())
                filedata = str(umur_tahun) + " Tahun "#+ str(umur_bulan) + " Bulan " + str(umur_hari) + " Hari"
                filedata = filedata + "\n"
                f.write(filedata)
                filedata = str(self.main_UI.golongan_darah.text())
                filedata = filedata + "\n"
                f.write(filedata)
                filedata = str(self.main_UI.pekerjaanLineEdit.text())
                filedata = filedata + "\n"
                f.write(filedata)
                filedata = str(self.main_UI.tanggalupdate_label.text())
                filedata = filedata + "\n"
                f.write(filedata)
            if self.foto == "":
                pass
            else:
                copy(self.foto, dir_name + '/')
            message = QMessageBox()
            message.warning(self, "Perhatian", "Berhasil disimpan!")

    def tampil_data(self):
        try:
            file_png = self._dir + '/' + self.current_pasien + '/*.png'
            file_jpg = self._dir + '/' + self.current_pasien + '/*.jpg'
            file_jpeg = self._dir + '/' + self.current_pasien + '/*.jpeg'
            file_foto = glob.glob(file_png)
            foto = ""
            if file_foto == []:
                file_foto = glob.glob(file_jpg)
                if file_foto == []:
                    file_foto = glob.glob(file_jpeg)
                    if file_foto == []:
                        pass
                    else:
                        for data in file_foto:
                            foto = data
                else:
                    for data in file_foto:
                        foto = data
            else:
                for data in file_foto:
                    foto = data

            file = open(foto)
            file.close()
            self.avatar_ico = foto
        except IOError:
            self.avatar_ico = avatar_ico_default
        fname = self._dir + '/' + self.current_pasien + '/data.dat'
        with open(fname, 'r') as f:
            jumlah_data = 0
            for isi_data in f:
                jumlah_data = jumlah_data +1
                isi_data = isi_data.replace("\n", "")
                if jumlah_data == 1:
                    self.main_UI.nomor_label.setText(isi_data)
                if jumlah_data == 2:
                    self.main_UI.nama_label.setText(isi_data)
                if jumlah_data == 3:
                    self.main_UI.jenis_kelamin_label.setText(isi_data)
                if jumlah_data == 4:
                    self.main_UI.tempat_label.setText(isi_data)
                if jumlah_data == 5:
                    self.main_UI.ttl_label.setText(isi_data)
                if jumlah_data == 6:
                    self.main_UI.umur_label.setText(isi_data)
                if jumlah_data == 7:
                    self.main_UI.gol_darah_label.setText(isi_data)
                if jumlah_data == 8:
                    self.main_UI.pekerjaan_label.setText(isi_data)

    def unggah_foto(self):
        self.foto, _ = QFileDialog.getOpenFileName(self, 'Unggah Foto', os.path.join(os.getcwd()), "Image files (*.jpg *.jpeg *.png)")
        self.main_UI.foto_label.setText(str(self.foto))

    def add_picture(self, row, col, path, widget):
        item = QTableWidgetItem()
        picture = QPixmap(path)
        copy = picture.scaled(320, 240, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        item.setIcon(QIcon(copy))
        item.setText(str(path))
        widget.setItem(row, col, item)

    def show_thumbnail(self):
        vid_dir = self._dir + '/' + self.current_pasien + '/rekam/video'
        vid_list = vid_dir + '/' + 'list.dat'
        thumbnail_list = vid_dir + '/thumb.dat'
        with open(vid_list, 'r') as f:
            jumlah_data = 0
            row = 0
            for data in f:
                row += 1
            if row != 0:
                self.main_UI.no_video.setVisible(False)
            if row < 2:
                self.main_UI.videoView.setColumnCount(row)
            else:
                self.main_UI.videoView.setColumnCount(2)
            if row % 2 != 0:
                row = (row/2) + 1
            else:
                row = row/2
            self.main_UI.videoView.setRowCount(row)
        with open(thumbnail_list, 'r') as f:
            jumlah_data = 0
            row = 0
            col = 0
            for data in f:
                data = data.replace("\n", "")
                jumlah_data += 1
                if col > 1:
                    row += 1
                    col = 0
                self.add_picture(row, col, data, self.main_UI.videoView)
                col += 1


    def show_picture(self):
        img_dir = self._dir + '/' + self.current_pasien + '/rekam'
        img_list = img_dir + '/' + 'list.dat'
        with open(img_list, 'r') as f:
            jumlah_data = 0
            row = 0
            for data in f:
                row += 1
            if row != 0:
                self.main_UI.label_kosong.setVisible(False)
            if row < 2:
                self.main_UI.galeriView.setColumnCount(row)
            else:
                self.main_UI.galeriView.setColumnCount(2)
            if row % 2 != 0:
                row = (row/2) + 1
            else:
                row = row/2
            self.main_UI.galeriView.setRowCount(row)
        with open(img_list, 'r') as f:
            jumlah_data = 0
            row = 0
            col = 0
            for data in f:
                data = data.replace("\n", "")
                jumlah_data += 1
                if col > 1:
                    row += 1
                    col = 0
                self.add_picture(row, col, data, self.main_UI.galeriView)
                col += 1

    def add_catatan_dokter(self):
        fnotes = self._dir + '/' + self.current_pasien + '/catatan_dokter.dat'
        with open(fnotes, 'a') as f:
            filedata = self.notes_UI.catatanDokter.toPlainText() + ' - ' + self.notes_UI.nama_dokter.text() + "\n"
            f.write(filedata)
        self.notes_window.close()

    def tampil_catatan_dokter(self):
        fnotes = self._dir + '/' + self.current_pasien + '/catatan_dokter.dat'
        with open(fnotes, 'r') as f:
            filedata=""
            for data in f:
                filedata += data
            self.main_UI.catatan_dokter_txtedit.setText(filedata)

    def show_welcomeWidget_content(self):
        self.fadeAnim(self.main_UI.daftarPasien_widget, 0)
        self.fadeAnim(self.main_UI.mainWidget, 0)
        self.slideAnim(self.main_UI.avatarWidget, -270, -10)
        self.show_logo(self.main_UI.logo)
        self.fadeAnim(self.main_UI.welcomeWidget, 1)
        self.random_number = str(random.randint(1000,9999))

    def show_avatarWidget_content(self):
        self.displayAvatar(self.avatar_ico)
        self.slideAnim(self.main_UI.avatarWidget, 0, -10)

    def show_logo(self, widget):
        brand = QPixmap(':/img/resource/teeth.png')
        widget.setScaledContents(True)
        widget.setPixmap(brand)

    def fadeAnim(self, widget, state):
        self.eff = QGraphicsOpacityEffect(self)
        widget.setGraphicsEffect(self.eff)
        self.animFade = QPropertyAnimation(self.eff, b"opacity")
        self.animFade.setDuration(500)
        if state == 1:
            self.animFade.setStartValue(0)
            self.animFade.setEndValue(1)
            self.animFade.setEasingCurve(QEasingCurve.InBack)
            self.animFade.start(QPropertyAnimation.DeleteWhenStopped)
            widget.setVisible(True)
        else:
            self.animFade.setStartValue(1)
            self.animFade.setEndValue(0)
            self.animFade.setEasingCurve(QEasingCurve.OutBack)
            self.animFade.start(QPropertyAnimation.DeleteWhenStopped)
            widget.setVisible(False)

    def addAnim(self, widget):
        anim = QPropertyAnimation(widget, b"geometry")
        return anim

    def slideAnim(self, widget, x, y):
        if widget.x() == x and widget.y() == y:
            pass
        else:
            self.animSlide = QPropertyAnimation(widget, b"geometry")
            self.animSlide.setDuration(300)
            self.animSlide.setStartValue(QRect(widget.x(),widget.y(),widget.width(),widget.height()))
            self.animSlide.setEndValue(QRect(x, y, widget.width(), widget.height()))
            self.animSlide.start(QPropertyAnimation.DeleteWhenStopped)
            widget.setVisible(True)

    def show_mainWidget_content(self):
        found = False
        self.current_pasien = self.main_UI.nomor_txtedit.text()
        self.current_pasien = self.current_pasien.replace("\n", "")
        if self.current_pasien == "":
            self.main_UI.error_label.setText("Nomor Kosong")
            self.slideAnim(self.main_UI.error_label, 730,600)
            message = QMessageBox()
            message.warning(self, "Perhatian", "Nomor kosong!")
            self.slideAnim(self.main_UI.error_label, 1030,600)
        else:
            with open(self.pasien_list, 'r') as f:
                for list_pasien in f:
                    list_pasien = list_pasien.replace("\n", "")
                    if self.current_pasien == list_pasien:
                        self.fadeAnim(self.main_UI.welcomeWidget, 0)
                        self.main_UI.mainWidget.setVisible(True)
                        self.tampil_data()
                        self.show_avatarWidget_content()
                        self.fadeAnim(self.main_UI.mainWidget, 1)
                        self.tampil_informasi()
                        found = True
            if found == False:
                self.main_UI.error_label.setText("Nomor Tidak Ditemukan")
                self.slideAnim(self.main_UI.error_label, 730,600)
                message = QMessageBox()
                message.warning(self, "Perhatian", "Nomor tidak ditemukan")
                self.slideAnim(self.main_UI.error_label, 1030,600)

    def show_daftarPasien(self):
        self.fadeAnim(self.main_UI.welcomeWidget, 0)
        self.fadeAnim(self.main_UI.daftarPasien_widget, 1)

    def makeDirectory(self, dir):
        if not os.path.exists(dir):
            os.makedirs(dir)

    def makeFileAVI(self):
        vid_dir = self._dir + '/' + self.current_pasien + '/rekam/video'
        self.makeDirectory(vid_dir)
        video = datetime.now().strftime('%Y%m%d_%H%M%S')
        vid_name = vid_dir + '/' + 'VID_' + video + '.avi'
        vid_list = vid_dir + '/' + 'list.dat'
        with open(vid_list, 'a') as f:
            filedata = vid_name + "\n"
            f.write(filedata)
        self.rekamThread.video_name = vid_name

    def makeFileIMG(self):
        img_dir = self._dir + '/' + self.current_pasien + '/rekam'
        self.makeDirectory(img_dir)
        image = datetime.now().strftime('%Y%m%d_%H%M%S')
        img_name = img_dir + '/' + 'IMG_' + image + '.jpg'
        img_list = img_dir + '/' + 'list.dat'
        with open(img_list, 'a') as f:
            filedata = img_name + "\n"
            f.write(filedata)
        self.rekamThread.filename = img_name

    def displayAvatar(self, icon):
        self.avatar_icon = QPixmap(icon)
        self.mask = QBitmap(self.avatar_icon.size())
        self.painter = QPainter(self.mask)
        self.mask.fill(Qt.white)
        self.painter.setBrush(Qt.black)
        self.painter.drawEllipse(0,0,self.mask.width(),self.mask.height())
        self.avatar_icon.setMask(self.mask)
        self.main_UI.avatar.setScaledContents(True)
        self.painter.end()
        self.main_UI.avatar.setPixmap(self.avatar_icon)

    def createImageWindow(self, width, height, path):
        self.window = QWidget()
        self.window.setGeometry(0, 0, width, height)
        #self.window.setFixedSize(width, height)
        item = QLabel(self.window)
        item.setAlignment(Qt.AlignCenter)
        #layout = QVBoxLayout()
        #layout.addWidget(item)
        picture = QPixmap(str(path))
        item.setPixmap(picture.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.window.setWindowTitle(str(path))
        #self.window.setLayout(layout)
        self.window.show()

    def createVideoWindow(self, path):
        self.videoWindow = video_window(path)

    def about(self):
        self.about_window = QWidget()
        self.about_window.setGeometry(0,0,262,363)
        self.about_window.setFixedSize(262,363)
        self.about_window.setWindowTitle("Tentang")
        self.about_window.setStyleSheet("QWidget{background-color:#0bb6e4;}")
        layout = QVBoxLayout(self.about_window)
        title = QLabel(self.about_window)
        icon_label = QLabel(self.about_window)
        nama_label = QLabel(self.about_window)
        deskripsi_label = QLabel(self.about_window)
        layout.addWidget(icon_label)
        layout.addWidget(title)
        layout.addWidget(nama_label)
        layout.addWidget(deskripsi_label)
        title.setAlignment(Qt.AlignCenter)
        icon_label.setAlignment(Qt.AlignCenter)
        nama_label.setAlignment(Qt.AlignCenter)
        deskripsi_label.setAlignment(Qt.AlignCenter)
        self.show_logo(icon_label)
        title.setText("CATROUS")
        nama_label.setText("Cermin dan Kamera Intraoral\nTerintegrasi Sistem")
        deskripsi_label.setText("Solusi Ergonomis bagi Dokter Gigi\ndalam Diagnosis dan Edukasi\nKesehatan Gigi dan Mulut Pasien\nUniversias Gadjah Mada")
        icon_label.setScaledContents(True)
        nama_label.setScaledContents(True)
        deskripsi_label.setScaledContents(True)
        f = QFont('Trebuchet MS', 11, QFont.Normal)
        f1 = QFont('Trebuchet MS', 12, QFont.Bold)
        title.setFont(f1)
        nama_label.setFont(f)
        deskripsi_label.setFont(f)
        self.about_window.show()

#main loop
if __name__ == '__main__':
    core = QApplication(sys.argv)
    Application = App()
    sys.exit(core.exec_())
