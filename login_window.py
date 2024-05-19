from PyQt5.QtWidgets import QWidget, QMessageBox
from PyQt5.QtCore import Qt, QPoint, pyqtSlot
from PyQt5.QtGui import QMouseEvent

from ui.login import Ui_Form
from main_window import MainWindow
class LoginWindow(QWidget):
    def __init__(self):
        super(LoginWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self._startPos = None
        self._endPos = None
        self._tracking = False

        ## hide the frame and background of the app
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
    @pyqtSlot()
    def on_loginButton_clicked(self):
        if self.ui.userInput.text() == "admin" and self.ui.passInput.text() == "1234":
            self.close()
            main_window = MainWindow()
            main_window.show()
        else:
            errorBox = QMessageBox(self)
            errorBox.setWindowTitle("Login Error")
            errorBox.setIcon(QMessageBox.Warning)
            errorBox.setText("Warning, username or password is incorrect.")
            errorBox.setStandardButtons(QMessageBox.Ok)
            errorBox.exec_()

    @pyqtSlot()
    def on_exitButton_clicked(self):
        # Function for exit button
        exit_msgBox = QMessageBox(self)
        exit_msgBox.setIcon(QMessageBox.Warning)
        exit_msgBox.setWindowTitle("Exit application")
        exit_msgBox.setText("Are you sure you want to exit?")
        exit_msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply = exit_msgBox.exec_()
        if reply == QMessageBox.Yes:
            self.close()
        else:
            return

    def mouseMoveEvent(self, a0: QMouseEvent) -> None:
        if self._tracking:
            self._endPos = a0.pos() - self._startPos
            self.move(self.pos() + self._endPos)

    def mousePressEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._startPos = QPoint(a0.x(), a0.y())
            self._tracking = True

    def mouseReleaseEvent(self, a0: QMouseEvent) -> None:
        if a0.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None

