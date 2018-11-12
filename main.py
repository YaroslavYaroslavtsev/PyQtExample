import sys
from PyQt5.QtWidgets import QApplication, QListView
from myModel import MyModel

if __name__ == '__main__':

    app = QApplication(sys.argv)
    w = QListView()
    model = MyModel()
    w.setModel(model)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('Simple')
    w.show()
    sys.exit(app.exec_())
