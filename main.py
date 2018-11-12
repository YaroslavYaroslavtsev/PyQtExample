import sys
from PyQt5.QtWidgets import QApplication, QListView
from myModel import MyModel
from itemDelegate import MyItemDelegate

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QListView()
    w.setItemDelegate(MyItemDelegate())
    model = MyModel()
    w.setModel(model)
    w.resize(500, 300)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
