from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class qlabel_extended(QLabel):
	clicked = pyqtSignal()
	def __init__(self, parent=None):
		QLabel.__init__(self, parent)

	def mousePressEvent(self, event):
		self.clicked.emit()