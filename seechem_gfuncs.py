from PyQt5.QtWidgets import QWidget, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor    

# box shadow
def box_shadow(the_box):
    box_shadoweffect = QGraphicsDropShadowEffect()
    box_shadoweffect.setBlurRadius(15)
    box_shadoweffect.setColor(QColor(0, 0, 0, 160))
    box_shadoweffect.setOffset(4, 4)

    the_box.setGraphicsEffect(box_shadoweffect)
    return box_shadoweffect

