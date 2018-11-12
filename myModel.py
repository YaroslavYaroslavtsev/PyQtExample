from PyQt5.QtCore import Qt, QAbstractListModel, QVariant, QSize
from PyQt5.QtGui import QFont, QBrush, QPixmap
import resources


class MyModel(QAbstractListModel):
    def __init__(self):
        super().__init__()
        self.itemList.append('myItem1')
        self.itemList.append('myItem2')
        self.itemList.append('myItem3')

    itemList = []

    def flags(self, index):
        return Qt.ItemIsEnabled | Qt.ItemIsEditable | Qt.ItemIsSelectable

    def rowCount(self, parent):
        return len(self.itemList)

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        # Display role текст
        if role == Qt.DisplayRole or role == Qt.EditRole:
            return self.itemList[index.row()]
        # Font role шрифт текста
        if role == Qt.FontRole:
            return QFont('MS Sans Serif', 16)
        # TextAlignment role выравнивание текста
        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter | Qt.AlignHCenter
        # Background role цвет фона
        if role == Qt.BackgroundRole:
            return QBrush(Qt.gray)
        # Foreground role цвет текста
        if role == Qt.ForegroundRole:
            return QBrush(Qt.blue)
        # CheckState role  если данная роль используется
        # у элемента отбражается чек бокс
        if role == Qt.CheckStateRole:
            return QVariant()
        # SizeHint role здесь модель говорит какой размер области
        # нужен для отображения ее элемента
        if role == Qt.SizeHintRole:
            return QSize(256, 128)
        # Decoration role  тут может быть картинка, иконка или даже цвет
        if role == Qt.DecorationRole:
            return QPixmap(":/images/icon" + str(index.row() + 1))
        # Если у нас нет данных для роли которую просят возвращаем
        # невалидный QVariant
        print("Unimplemented role number is:" + str(role))
        return QVariant()

    def setData(self, index, value, role):
        if index.isValid() and index.row() >= 0 and index.row() < len(self.itemList):
            self.itemList[index.row()] = value
            return True
        else:
            return False
