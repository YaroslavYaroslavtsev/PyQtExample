from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtGui import QFont, QBrush, QPixmap, QPainter
from PyQt5.QtWidgets import QItemDelegate, QStyleOptionViewItem


class MyItemDelegate(QItemDelegate):
    def __init__(self):
        super().__init__()

    # TrackDelegate(int durationColumn, QObject *parent = 0);
    def paint(self, painter, option, index):
        super().paint(painter, option, index)
        super().drawDisplay(painter, option, option.rect, 'MyRedrawText\nsdsddsd')

    def createEditor(self, parent, option, index):
        super().createEditor(parent, option, index)

    def setEditorData(self, editor, index):
        super().setEditorData(editor, index)

    def setModelData(self, editor, model, index):
        super().setModelData(editor, model, index)

    def drawBackground(self, painter, option, index):
        myoption = QStyleOptionViewItem(option)
        myoption.backgroundBrush = QBrush(Qt.red)
        super().drawBackground(painter, myoption, index)

    @pyqtSlot()
    def commitAndCloseEditor():
        super().commitAndCloseEditor()
