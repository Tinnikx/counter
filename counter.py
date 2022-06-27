from PyQt5.QtWidgets import QApplication, QMainWindow

from generated.counter import Ui_MainWindow


class MyCounter(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        super().__init__()
        self.setupUi(self)
        self.show()

        self.reset_btn.clicked.connect(lambda: self.count_num.setText('0'))
        self.count_btn.clicked.connect(lambda: self.count_num.setText(str(int(self.count_num.text()) + 1)))
        self.count_btn.setShortcut('Space')


if __name__ == '__main__':
    app = QApplication([])
    my_counter = MyCounter()
    app.exec()
