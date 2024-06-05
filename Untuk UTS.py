import sys
import csv
import pandas as pd
import PySimpleGUI as sg 
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QLabel, 
    QLineEdit,
    QPushButton, 
    QMessageBox
    )
from datetime import datetime

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Page Absensi')
        self.setGeometry(100, 100, 400, 200)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginPage()
    window.show()
    sys.exit(app.exec())
