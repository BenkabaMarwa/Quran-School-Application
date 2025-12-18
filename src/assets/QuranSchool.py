from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5 import QtCore, QtGui, QtWidgets, uic
import easygui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import os
import pyautogui
import sqlite3
import random
import datetime
import subprocess
from barcode.writer import ImageWriter
from barcode.writer import ImageWriter
import time
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import webbrowser
from PyQt5.QtGui import QMovie
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import numpy as np
import string
from PIL import Image, ImageDraw, ImageFont
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog
from PyQt5.QtGui import QTextDocument
from PyQt5.QtCore import QSizeF
import base64 
from PyQt5.QtPrintSupport import QPrintPreviewDialog
import subprocess



database=sqlite3.connect("QuranSchool.db")
cursor=database.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Users(
                    Id TEXT PRIMARY KEY,
                    Username TEXT NOT NULL,
                    Password TEXT,
                    RePassword TEXT
                    )
    """)


class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school, self).__init__()
        uic.loadUi("QuranSchool.ui", self)  # Loads UI onto 'self'
        
        self.setWindowTitle("Quran School")
        self.showMaximized()
        self.setMinimumSize(1200, 800)
        self.LoginFrame_2.hide()

        effect = QGraphicsOpacityEffect(self.label_4)
        effect.setOpacity(0.19)
        self.label_4.setGraphicsEffect(effect)
        effect2 = QGraphicsOpacityEffect(self.label_8)
        effect2.setOpacity(0.19)
        self.label_8.setGraphicsEffect(effect2)

        self.SignupButton.clicked.connect(self.SignUpAnAccount)
        self.LoginButton.clicked.connect(self.LoginToMyAccount)

        self.ClearButton.clicked.connect(self.ClearLogin)
        self.ClearButton2.clicked.connect(self.ClearSignup)

    def SignUpAnAccount(self):
        try:
            Id=random.randrange(10000000000000000)
            Username=self.UserNameLineEdit2.text()
            Password=self.PasswordLineEdit2.text()
            RePassword=self.PasswordLineEdit3.text()
            if Password!=RePassword:
                self.label_2.setText("يرجى تأكيد كلمة السر")
            else:
                cursor.execute("INSERT INTO Users (Id,Username,Password,RePassword) VALUES (?,?,?,?)",(Id,Username,Password,RePassword))
                database.commit()
        except Exception as error:
            print("error",error)

    def LoginToMyAccount(self):
        try:
            Username=self.UserNameLineEdit.text()
            Password=self.PasswordLineEdit.text()
            cursor.execute("SELECT * FROM Users WHERE Username=? AND Password=?",(Username,Password))
            data=cursor.fetchall()
            if data:
                self.stackedWidget.setCurrentIndex(1)
            else:
                self.label_3.setText("كلمة السر خاطئة")
        except Exception as error:
            print("error",error)

    def ClearLogin(self):
        self.UserNameLineEdit.clear()
        self.PasswordLineEdit.clear()
    def ClearSignup(self):
        self.UserNameLineEdit2.clear()
        self.PasswordLineEdit2.clear()
        self.PasswordLineEdit3.clear()






if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())