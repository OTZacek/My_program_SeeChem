from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt

class LineDrawingWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

    def paintEvent(self, event):
        painter = QPainter(self)
        # Set the pen for drawing (color, width, style)
        pen = QPen(Qt.blue, 2, Qt.SolidLine)
        painter.setPen(pen)

        # Draw a line from (x1, y1) to (x2, y2)
        painter.drawLine(10, 10, 100, 100)
        painter.drawLine(10, 100, 100, 10) # Another line