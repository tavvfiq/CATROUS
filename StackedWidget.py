import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class FaderWidget(QWidget):

    def __init__(self, old_widget, new_widget):
    
        QWidget.__init__(self, new_widget)
        
        self.old_pixmap = QPixmap(new_widget.size())
        old_widget.render(self.old_pixmap)
        self.pixmap_opacity = 1.0
        
        self.timeline = QTimeLine()
        self.timeline.valueChanged.connect(self.animate)
        self.timeline.finished.connect(self.close)
        self.timeline.setDuration(400)
        self.timeline.start()
        
        self.resize(new_widget.size())
        #self.show()
    
    def paintEvent(self, event):
    
        painter = QPainter()
        painter.begin(self)
        painter.setOpacity(self.pixmap_opacity)
        painter.drawPixmap(0, 0, self.old_pixmap)
        painter.end()
    
    def animate(self, value):
    
        self.pixmap_opacity = 1.0 - value
        self.repaint()

class StackedWidget(QStackedWidget):

    def __init__(self, parent = None):
        QStackedWidget.__init__(self, parent)
    
    def setCurrentIndex(self, index):
        if self.currentWidget() == self.widget(index):
            pass
        else:    
            self.fader_widget = FaderWidget(self.currentWidget(), self.widget(index))
            QStackedWidget.setCurrentIndex(self, index)