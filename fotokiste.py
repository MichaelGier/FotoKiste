import sys
import os
import subprocess


from config import fotokisteText, fotokisteCfg

from datetime import datetime, date, time
from time import sleep

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTime, QTimer, QUrl
from PyQt5.QtGui import QIcon, QPixmap, QCursor
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtWebKitWidgets import QWebView
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow

if not fotokisteCfg['nopi']:
    try:
        from picamera import PiCamera
    except ImportError:
        print("PiCamera nicht gefunden - Simulation eingeschaltet")
        fotokisteCfg['nopi'] = True

    try:
        import RPi.GPIO as GPIO
    except ImportError:
        print("RPi GPIO nicht gefunden - Simulation eingeschaltet")
        fotokisteCfg['nopi'] = True

from shutil import copyfile, move
from stat import S_ISREG, ST_MTIME, ST_MODE

class Ui_Form_mod ( object ):
    def setupUi (self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("FotoKiste")
        Form.resize(fotokisteCfg['window-width'], fotokisteCfg['window-heigh'])
        Form.setMinimumSize(QtCore.QSize(fotokisteCfg['window-width'], fotokisteCfg['window-height']))
        Form.setMaximumSize(QtCore.QSize(fotokisteCfg['window-width'], fotokisteCfg['window-height']))
        Form.setHtml("Initializing...")

        def initSystem (self, Form):
            # Kamera
            if not fotokisteCfg['nopi']:
                self.camera = PiCamera()
                self.camera.hflip = fotokisteCfg['cam-c-hflip']
                if (fotokisteCfg['cam-p-hflip'] == fotokisteCfg['cam-c-hflip']):
                    fotokisteCfg['cam-p-hflip'] = False
            self.isLive = False

            
class QWebView_mod(QWebView):
    def __init__(self):
        super(QWebView, self).__init__()
        self.ui = Ui_Form_mod()
        self.ui.setupUi(self)
        self.ui.initSystem(self)
        self.ui.screenMain(self)
        self.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))

        if not fotoboxCfg['nopi']:
            GPIO.setmode(GPIO.BCM)

            GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
            GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)

            self.btnC1 = GPIO.HIGH
            self.btnC2 = GPIO.HIGH
            self.btnC3 = GPIO.HIGH
    
        #Key Poller
        self.timerKey = QTimer(self)
        self.timerKey.timeout.connect(self.buttonCheck)
        self.timerKey.start(25)
        self.btnB  = 1

        self.showFullScreen()

app = QApplication(sys.argv)
window = QWebView_mod()

sys.exit(app.exec_())