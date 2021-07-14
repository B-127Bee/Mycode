from PyQt5 import QtCore, QtGui, QtWidgets
from Widget import Widget
from Slider import Slider


class Gui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(615, 404)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.wgt_video = Widget(self.centralwidget)
        self.wgt_video.setMinimumSize(QtCore.QSize(410, 200))
        self.wgt_video.setMaximumSize(QtCore.QSize(16777215, 16777215))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.wgt_video.setPalette(palette)
        self.wgt_video.setAutoFillBackground(True)
        self.wgt_video.setObjectName("wgt_video")
        self.gridLayout.addWidget(self.wgt_video, 0, 0, 1, 1)
        self.sld_video = Slider(self.centralwidget)
        self.sld_video.setMinimumSize(QtCore.QSize(410, 0))
        self.sld_video.setMaximumSize(QtCore.QSize(16777215, 20))
        self.sld_video.setMaximum(100)
        self.sld_video.setOrientation(QtCore.Qt.Horizontal)
        self.sld_video.setObjectName("sld_video")
        self.gridLayout.addWidget(self.sld_video, 1, 0, 1, 1)
        self.lab_video = QtWidgets.QLabel(self.centralwidget)
        self.lab_video.setMaximumSize(QtCore.QSize(16777215, 50))
        self.lab_video.setObjectName("lab_video")
        self.gridLayout.addWidget(self.lab_video, 1, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.btn_open = QtWidgets.QPushButton(self.splitter)
        self.btn_open.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_open.setObjectName("btn_open")
        self.btn_play = QtWidgets.QPushButton(self.splitter)
        self.btn_play.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_play.setObjectName("btn_play")
        self.btn_pause = QtWidgets.QPushButton(self.splitter)
        self.btn_pause.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_pause.setObjectName("btn_pause")
        self.btn_detect = QtWidgets.QPushButton(self.splitter)
        self.btn_detect.setMaximumSize(QtCore.QSize(100, 25))
        self.btn_detect.setObjectName("btn_detect")
        self.text1 = QtWidgets.QLabel(self.splitter)
        self.text1.setMaximumSize(QtCore.QSize(100, 25))
        self.text1.setObjectName("Threshold_L")
        self.Le1 = QtWidgets.QLineEdit(self.splitter)
        self.Le1.setMaximumSize(QtCore.QSize(100, 25))
        self.Le1.setObjectName("Threshold")
        self.gridLayout.addWidget(self.splitter, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 615, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lab_video.setText(_translate("MainWindow", "0%"))
        self.btn_open.setText(_translate("MainWindow", "VideoFile"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_detect.setText(_translate("MainWindow", "Detect"))
        self.text1.setText(_translate("Mainwindow", "Threshold"))
