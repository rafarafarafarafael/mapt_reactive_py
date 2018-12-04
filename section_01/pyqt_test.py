import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = QWidget()
    win.resize(250, 150)
    win.move(350, 200)
    win.setWindowTitle('Hello World')
    win.show()
    sys.exit(app.exec_())