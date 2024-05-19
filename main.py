import sys

from PyQt5.QtWidgets import QApplication

from login_window import LoginWindow
from main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # Change from MainWindow() to LoginWindow() for login page. If you want instant access, put MainWindow()
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())

