from PyQt5.QtCore import Qt, QAbstractListModel, QVariant, QSize
from PyQt5.QtGui import QColor


class MyModel(QAbstractListModel):
    def __init__(self):
        super().__init__()

    def rowCount(self, parent):
        return 1

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole:
            return 'myModelItem'
        # SizeHint role здесь модель говорит какой размер области
        # нужен для отображения ее элемента
        if role == Qt.SizeHintRole:
            return QSize(60, 30)
        # Decoration role  тут может быть картинка, иконка или даже цвет
        if role == Qt.DecorationRole:
            return QColor(Qt.red)
        # Если у нас нет данных для роли которую просят возвращаем
        # невалидный QVariant
        print("Unimplemented role number is:" + str(role))
        return QVariant()
