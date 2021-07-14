from PyQt5.QtCore import *
from PyQt5.QtWidgets import QSlider


class Slider(QSlider):
    ClickedValue = pyqtSignal(int)

    def __init__(self, father):
        super().__init__(Qt.Horizontal, father)

    def mousePressEvent(self, QMouseEvent):
        super().mousePressEvent(QMouseEvent)
        value = QMouseEvent.localPos().x()
        value = round(value / self.width() * self.maximum())
        self.ClickedValue.emit(value)
