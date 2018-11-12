from PyQt5.QtCore import Qt, QAbstractListModel, QVariant, QSize
from PyQt5.QtGui import QColor, QFont, QBrush


class MyModel(QAbstractListModel):
    def __init__(self):
        super().__init__()

    def rowCount(self, parent):
        return 3

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        # Display role текст
        if role == Qt.DisplayRole:
            return 'myModelItem' + str(index.row())
        # Font role шрифт текста
        if role == Qt.FontRole:
            return QFont('MS Sans Serif', 16)
        # TextAlignment role выравнивание текста
        if role == Qt.TextAlignmentRole:
            return (Qt.AlignCenter or Qt.AlignHCenter)
        # Background role цвет фона
        if role == Qt.BackgroundRole:
            return QBrush(Qt.gray)
        # Foreground role цвет текста
        if role == Qt.ForegroundRole:
            return QBrush(Qt.blue)
        # CheckState role  если данная роль используется
        # у элемента отбражается чек бокс
        if role == Qt.CheckStateRole:
            return Qt.Unchecked
        # SizeHint role здесь модель говорит какой размер области
        # нужен для отображения ее элемента
        if role == Qt.SizeHintRole:
            return QSize(60, 40)
        # Decoration role  тут может быть картинка, иконка или даже цвет
        if role == Qt.DecorationRole:
            return QColor(Qt.red)
        # Если у нас нет данных для роли которую просят возвращаем
        # невалидный QVariant
        print("Unimplemented role number is:" + str(role))
        return QVariant()
