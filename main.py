from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtCore import *
from GUI import Gui_MainWindow
import sys
import os


class MainWindow(Gui_MainWindow, QMainWindow):
    def __init__(self):
        super(Gui_MainWindow, self).__init__()
        self.setupUi(self)
        self.sld_video_pressed = False
        self.player = QMediaPlayer()
        self.player.setVideoOutput(self.wgt_video)
        self.btn_open.clicked.connect(self.openVideoFile)
        self.btn_play.clicked.connect(self.playVideo)
        self.btn_pause.clicked.connect(self.pauseVideo)
        self.btn_detect.clicked.connect(self.detect)
        self.player.positionChanged.connect(self.changeSlide)
        self.sld_video.setTracking(False)
        self.sld_video.sliderReleased.connect(self.releaseSlider)
        self.sld_video.sliderPressed.connect(self.pressSlider)
        self.sld_video.sliderMoved.connect(self.moveSlider)
        self.sld_video.ClickedValue.connect(self.clickedSlider)

    def detect(self):
        text = self.Le1.text()
        if text is "" or not text[2:].isdecimal() or not text[0] is '0' or not text[1] is '.':
            msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有输入正确的置信度(0~1)')
            msg_box.exec_()
        else:
            a = QFileDialog.getOpenFileName(self)[0]
            if a is "":
                msg_box = QMessageBox(QMessageBox.Warning, '警告', '没有选择MP4视频文件')
                msg_box.exec_()
            else:
                self.t = Thread_1(text, a)
                self.t.finishSignal.connect(lambda:self.playFinal())
                self.t.start()

    def playFinal(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile("output/output.mp4")))
        self.player.play()


    def clickedSlider(self, position):
        if self.player.duration() > 0:
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)
        else:
            self.sld_video.setValue(0)

    def moveSlider(self, position):
        self.sld_video_pressed = True
        if self.player.duration() > 0:
            video_position = int((position / 100) * self.player.duration())
            self.player.setPosition(video_position)
            self.lab_video.setText("%.2f%%" % position)

    def pressSlider(self):
        self.sld_video_pressed = True
        print("pressed")

    def releaseSlider(self):
        self.sld_video_pressed = False

    def changeSlide(self, position):
        if not self.sld_video_pressed:
            self.videoLength = self.player.duration() + 0.1
            self.sld_video.setValue(round((position / self.videoLength) * 100))
            self.lab_video.setText("%.2f%%" % ((position / self.videoLength) * 100))

    def openVideoFile(self):
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(QFileDialog.getOpenFileName(self)[0])))
        self.player.play()

    def playVideo(self):
        self.player.play()

    def pauseVideo(self):
        self.player.pause()



def runDetect(threshold, route):
    r1 = os.getcwd()
    string1 = "pip install -r" + r1 + "\\PaddleDetection\\requirements.txt"
    string2 = "python PaddleDetection\\deploy\\python\\infer.py --model_dir=PaddleDetection\\model --use_gpu=True " \
              "--video_file=" + route + " --threshold=" + threshold
    os.system(string1)
    os.system(string2)


class Thread_1(QThread):
    finishSignal = pyqtSignal(str)

    def __init__(self, threshold, route):
        super().__init__()
        self.threshold = threshold
        self.route = route

    def run(self):
        runDetect(self.threshold, self.route)
        self.finishSignal.emit('Finished.')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    Gui_start = MainWindow()
    Gui_start.show()
    sys.exit(app.exec_())
