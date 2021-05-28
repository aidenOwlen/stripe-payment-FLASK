# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\achill123\Desktop\RegalTuning.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QThread
import random 
from PIL import Image,ImageFont,ImageDraw
from PIL.ImageColor import getcolor,getrgb
from PIL.ImageOps import grayscale
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import time
import stripe
from flask import Flask, request, make_response, abort, url_for, redirect,render_template
import webbrowser

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.fromaddr = "*************" #regalfiles@gmail.com
        self.password = "************"
        self.toaddr = "*************"
        self.Validate = 0
        self.Color_liste = ["red","blue","black","green","orange"]
        self.Ma_Liste = list(map(chr, range(65, 91))) + list(map(chr, range(97,123)))
        self.Validate = 0

        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(947, 774)
        MainWindow.setMinimumSize(QtCore.QSize(947, 774))
        MainWindow.setMaximumSize(QtCore.QSize(947, 774))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(530, 553, 161, 16))
        self.label_21.setStyleSheet(_fromUtf8("font-weight: bold;\n"
""))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 590, 101, 41))
        self.pushButton_2.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.Tab2 = QtGui.QTabWidget(self.centralwidget)
        self.Tab2.setGeometry(QtCore.QRect(0, 0, 981, 791))
        self.Tab2.setAutoFillBackground(False)
        self.Tab2.setStyleSheet(_fromUtf8("background-color: rgb(240, 240, 240);\n"
"QTabWidget { border:none }"))
        self.Tab2.setMovable(False)
        self.Tab2.setObjectName(_fromUtf8("Tab2"))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_6.setGeometry(QtCore.QRect(473, 340, 456, 157))
        self.groupBox_6.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.Comments = QtGui.QTextEdit(self.groupBox_6)
        self.Comments.setGeometry(QtCore.QRect(20, 25, 411, 121))
        self.Comments.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Comments.setObjectName(_fromUtf8("Comments"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 176, 456, 157))
        self.groupBox_2.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_6.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(20, 60, 53, 16))
        self.label_7.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(20, 90, 53, 16))
        self.label_8.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.Manu = QtGui.QLineEdit(self.groupBox_2)
        self.Manu.setGeometry(QtCore.QRect(111, 31, 191, 22))
        self.Manu.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Manu.setObjectName(_fromUtf8("Manu"))
        self.Model = QtGui.QLineEdit(self.groupBox_2)
        self.Model.setGeometry(QtCore.QRect(111, 60, 191, 22))
        self.Model.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Model.setObjectName(_fromUtf8("Model"))
        self.Engine = QtGui.QLineEdit(self.groupBox_2)
        self.Engine.setGeometry(QtCore.QRect(111, 89, 191, 22))
        self.Engine.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Engine.setObjectName(_fromUtf8("Engine"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(310, 30, 21, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(310, 60, 16, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(310, 90, 16, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox = QtGui.QGroupBox(self.tab_3)
        self.groupBox.setGeometry(QtCore.QRect(10, 12, 456, 157))
        self.groupBox.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(0, 30, 111, 16))
        self.label.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 53, 16))
        self.label_2.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 90, 53, 16))
        self.label_3.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.Name = QtGui.QLineEdit(self.groupBox)
        self.Name.setGeometry(QtCore.QRect(111, 60, 191, 22))
        self.Name.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Name.setObjectName(_fromUtf8("Name"))
        self.Email = QtGui.QLineEdit(self.groupBox)
        self.Email.setGeometry(QtCore.QRect(111, 89, 191, 22))
        self.Email.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Email.setObjectName(_fromUtf8("Email"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(310, 60, 53, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(310, 90, 53, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.CusNumber = QtGui.QLineEdit(self.groupBox)
        #self.CusNumber.setValidator(QtGui.QIntValidator())
        #self.CusNumber.setMaxLength(20)
        self.CusNumber.setGeometry(QtCore.QRect(111, 31, 191, 22))
        self.CusNumber.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.CusNumber.setObjectName(_fromUtf8("CusNumber"))
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.Name.raise_()
        self.Email.raise_()
        self.CusNumber.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.groupBox_4 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_4.setGeometry(QtCore.QRect(473, 12, 456, 157))
        self.groupBox_4.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 60, 71, 16))
        self.label_14.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.TuningFile = QtGui.QLineEdit(self.groupBox_4)
        self.TuningFile.setReadOnly(True)
        self.TuningFile.setGeometry(QtCore.QRect(90, 60, 261, 22))
        self.TuningFile.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.TuningFile.setObjectName(_fromUtf8("TuningFile"))
        self.Open = QtGui.QPushButton(self.groupBox_4)
        self.Open.clicked.connect(self.OPEN)
        self.Open.setGeometry(QtCore.QRect(260, 90, 93, 31))
        self.Open.setObjectName(_fromUtf8("Open"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_5.setGeometry(QtCore.QRect(473, 176, 456, 157))
        self.groupBox_5.setStyleSheet(_fromUtf8("QGroupBox { font-weight:bold }"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_15 = QtGui.QLabel(self.groupBox_5)
        self.label_15.setGeometry(QtCore.QRect(25, 30, 51, 16))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(30, 60, 53, 16))
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.Year = QtGui.QLineEdit(self.groupBox_5)
        self.Year.setValidator(QtGui.QIntValidator())
        self.Year.setMaxLength(4)
        self.Year.setGeometry(QtCore.QRect(91, 31, 191, 22))
        self.Year.setStyleSheet(_fromUtf8("background-color:white"))
        self.Year.setObjectName(_fromUtf8("Year"))
        self.HP = QtGui.QLineEdit(self.groupBox_5)
        self.HP.setGeometry(QtCore.QRect(91, 60, 191, 22))
        self.HP.setStyleSheet(_fromUtf8("background-color:white"))
        self.HP.setObjectName(_fromUtf8("HP"))
        self.Gearbox = QtGui.QComboBox(self.groupBox_5)
        self.Gearbox.addItem("Automatic")
        self.Gearbox.addItem("Manual")
        self.Gearbox.setGeometry(QtCore.QRect(91, 89, 191, 22))
        self.Gearbox.setStyleSheet(_fromUtf8("background-color:white"))
        self.Gearbox.setObjectName(_fromUtf8("Gearbox"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(290, 30, 16, 16))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.groupBox_5)
        self.label_19.setGeometry(QtCore.QRect(290, 60, 16, 16))
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.groupBox_5)
        self.label_20.setGeometry(QtCore.QRect(290, 90, 16, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 340, 456, 157))
        self.groupBox_3.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.Stage1 = QtGui.QCheckBox(self.groupBox_3)
        self.Stage1.setGeometry(QtCore.QRect(21, 22, 72, 20))
        self.Stage1.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.Stage1.setObjectName(_fromUtf8("Stage1"))
        self.Stage2 = QtGui.QCheckBox(self.groupBox_3)
        self.Stage2.setGeometry(QtCore.QRect(21, 50, 72, 20))
        self.Stage2.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.Stage2.setObjectName(_fromUtf8("Stage2"))
        self.Stage3 = QtGui.QCheckBox(self.groupBox_3)
        self.Stage3.setGeometry(QtCore.QRect(21, 78, 72, 20))
        self.Stage3.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.Stage3.setObjectName(_fromUtf8("Stage3"))
        self.DPF = QtGui.QCheckBox(self.groupBox_3)
        self.DPF.setGeometry(QtCore.QRect(136, 22, 49, 20))
        self.DPF.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.DPF.setObjectName(_fromUtf8("DPF"))
        self.EGR = QtGui.QCheckBox(self.groupBox_3)
        self.EGR.setGeometry(QtCore.QRect(136, 50, 50, 20))
        self.EGR.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.EGR.setObjectName(_fromUtf8("EGR"))
        self.TQMo = QtGui.QCheckBox(self.groupBox_3)
        self.TQMo.setGeometry(QtCore.QRect(252, 50, 61, 20))
        self.TQMo.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.TQMo.setObjectName(_fromUtf8("TQMo"))
        self.DTC = QtGui.QCheckBox(self.groupBox_3)
        self.DTC.setGeometry(QtCore.QRect(136, 78, 51, 20))
        self.DTC.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.DTC.setObjectName(_fromUtf8("DTC"))
        self.VMAX = QtGui.QCheckBox(self.groupBox_3)
        self.VMAX.setGeometry(QtCore.QRect(252, 78, 61, 20))
        self.VMAX.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.VMAX.setObjectName(_fromUtf8("VMAX"))
        self.FLAPS = QtGui.QCheckBox(self.groupBox_3)
        self.FLAPS.setGeometry(QtCore.QRect(252, 22, 63, 20))
        self.FLAPS.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.FLAPS.setObjectName(_fromUtf8("FLAPS"))
        self.Others = QtGui.QLineEdit(self.groupBox_3)
        self.Others.setGeometry(QtCore.QRect(70, 110, 261, 22))
        self.Others.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Others.setObjectName(_fromUtf8("Others"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 110, 51, 16))
        self.label_12.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(60, 520, 331, 157))
        self.label_13.setStyleSheet(_fromUtf8("background-image :url(nex.png);\n"
""))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.Send = QtGui.QPushButton(self.tab_3)
        self.Send.clicked.connect(self.send)
        self.Send.setGeometry(QtCore.QRect(630, 580, 101, 41))
        self.Send.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.Send.setObjectName(_fromUtf8("Send"))
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(610, 540, 161, 16))
        self.label_22.setStyleSheet(_fromUtf8("font-weight: bold;\n"
""))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.Tab2.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_74 = QtGui.QLabel(self.tab_4)
        self.label_74.setGeometry(QtCore.QRect(50, 550, 341, 131))
        self.label_74.setStyleSheet(_fromUtf8("background-image :url(nex.png);"))
        self.label_74.setText(_fromUtf8(""))
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.Send2 = QtGui.QPushButton(self.tab_4)
        self.Send2.setGeometry(QtCore.QRect(620, 630, 101, 41))
        self.Send2.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.Send2.setObjectName(_fromUtf8("Send2"))
        self.label_73 = QtGui.QLabel(self.tab_4)
        self.label_73.setGeometry(QtCore.QRect(600, 580, 161, 16))
        self.label_73.setStyleSheet(_fromUtf8("font-weight: bold;\n"
""))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.groupBox_10 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_10.setGeometry(QtCore.QRect(470, 280, 451, 231))
        self.groupBox_10.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_10.setObjectName(_fromUtf8("groupBox_10"))
        self.SupportComments = QtGui.QTextEdit(self.groupBox_10)
        self.SupportComments.setGeometry(QtCore.QRect(20, 25, 421, 191))
        self.SupportComments.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.SupportComments.setObjectName(_fromUtf8("SupportComments"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_8.setGeometry(QtCore.QRect(470, 130, 451, 141))
        self.groupBox_8.setStyleSheet(_fromUtf8("QGroupBox { font-weight : bold }"))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_67 = QtGui.QLabel(self.groupBox_8)
        self.label_67.setGeometry(QtCore.QRect(25, 30, 51, 16))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.label_68 = QtGui.QLabel(self.groupBox_8)
        self.label_68.setGeometry(QtCore.QRect(30, 60, 53, 16))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.label_69 = QtGui.QLabel(self.groupBox_8)
        self.label_69.setGeometry(QtCore.QRect(20, 90, 61, 16))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.Year2 = QtGui.QLineEdit(self.groupBox_8)
        self.Year2.setValidator(QtGui.QIntValidator())
        self.Year2.setMaxLength(4)
        self.Year2.setGeometry(QtCore.QRect(91, 31, 191, 22))
        self.Year2.setStyleSheet(_fromUtf8("background-color:white"))
        self.Year2.setObjectName(_fromUtf8("Year2"))
        self.HP2 = QtGui.QLineEdit(self.groupBox_8)
        self.HP2.setGeometry(QtCore.QRect(91, 60, 191, 22))
        self.HP2.setStyleSheet(_fromUtf8("background-color:white"))
        self.HP2.setObjectName(_fromUtf8("HP2"))
        self.Gearbox2 = QtGui.QComboBox(self.groupBox_8)
        self.Gearbox2.addItem("Automatic")
        self.Gearbox2.addItem("Manual")

        self.Gearbox2.setGeometry(QtCore.QRect(91, 89, 191, 22))
        self.Gearbox2.setStyleSheet(_fromUtf8("background-color:white"))
        self.Gearbox2.setObjectName(_fromUtf8("Gearbox2"))
        self.label_70 = QtGui.QLabel(self.groupBox_8)
        self.label_70.setGeometry(QtCore.QRect(290, 30, 16, 16))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.label_71 = QtGui.QLabel(self.groupBox_8)
        self.label_71.setGeometry(QtCore.QRect(290, 60, 16, 16))
        self.label_71.setObjectName(_fromUtf8("label_71"))
        self.label_72 = QtGui.QLabel(self.groupBox_8)
        self.label_72.setGeometry(QtCore.QRect(290, 90, 16, 16))
        self.label_72.setObjectName(_fromUtf8("label_72"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 130, 451, 141))
        self.groupBox_7.setStyleSheet(_fromUtf8("font-weight:bold;"))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_53 = QtGui.QLabel(self.groupBox_7)
        self.label_53.setGeometry(QtCore.QRect(10, 30, 91, 16))
        self.label_53.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.label_55 = QtGui.QLabel(self.groupBox_7)
        self.label_55.setGeometry(QtCore.QRect(20, 60, 53, 16))
        self.label_55.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_63 = QtGui.QLabel(self.groupBox_7)
        self.label_63.setGeometry(QtCore.QRect(20, 90, 53, 16))
        self.label_63.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_63.setObjectName(_fromUtf8("label_63"))
        self.Manu2 = QtGui.QLineEdit(self.groupBox_7)
        self.Manu2.setGeometry(QtCore.QRect(111, 31, 191, 22))
        self.Manu2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Manu2.setObjectName(_fromUtf8("Manu2"))
        self.Model2 = QtGui.QLineEdit(self.groupBox_7)
        self.Model2.setGeometry(QtCore.QRect(111, 60, 191, 22))
        self.Model2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Model2.setObjectName(_fromUtf8("Model2"))
        self.Engine2 = QtGui.QLineEdit(self.groupBox_7)
        self.Engine2.setGeometry(QtCore.QRect(111, 89, 191, 22))
        self.Engine2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Engine2.setObjectName(_fromUtf8("Engine2"))
        self.label_64 = QtGui.QLabel(self.groupBox_7)
        self.label_64.setGeometry(QtCore.QRect(310, 30, 21, 16))
        self.label_64.setObjectName(_fromUtf8("label_64"))
        self.label_65 = QtGui.QLabel(self.groupBox_7)
        self.label_65.setGeometry(QtCore.QRect(310, 60, 16, 16))
        self.label_65.setObjectName(_fromUtf8("label_65"))
        self.label_66 = QtGui.QLabel(self.groupBox_7)
        self.label_66.setGeometry(QtCore.QRect(310, 90, 16, 16))
        self.label_66.setObjectName(_fromUtf8("label_66"))
        self.groupBox_11 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_11.setGeometry(QtCore.QRect(11, 11, 451, 111))
        self.groupBox_11.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_11.setObjectName(_fromUtf8("groupBox_11"))
        self.label_75 = QtGui.QLabel(self.groupBox_11)
        self.label_75.setGeometry(QtCore.QRect(10, 30, 53, 16))
        self.label_75.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_75.setObjectName(_fromUtf8("label_75"))
        self.label_76 = QtGui.QLabel(self.groupBox_11)
        self.label_76.setGeometry(QtCore.QRect(10, 60, 53, 16))
        self.label_76.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_76.setObjectName(_fromUtf8("label_76"))
        self.Name2 = QtGui.QLineEdit(self.groupBox_11)
        self.Name2.setGeometry(QtCore.QRect(101, 30, 191, 22))
        self.Name2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Name2.setObjectName(_fromUtf8("Name2"))
        self.Email2 = QtGui.QLineEdit(self.groupBox_11)
        self.Email2.setGeometry(QtCore.QRect(101, 59, 191, 22))
        self.Email2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.Email2.setObjectName(_fromUtf8("Email2"))
        self.label_77 = QtGui.QLabel(self.groupBox_11)
        self.label_77.setGeometry(QtCore.QRect(300, 30, 53, 16))
        self.label_77.setObjectName(_fromUtf8("label_77"))
        self.label_78 = QtGui.QLabel(self.groupBox_11)
        self.label_78.setGeometry(QtCore.QRect(300, 60, 53, 16))
        self.label_78.setObjectName(_fromUtf8("label_78"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_9.setGeometry(QtCore.QRect(10, 280, 451, 231))
        self.groupBox_9.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.label_23 = QtGui.QLabel(self.groupBox_9)
        self.label_23.setGeometry(QtCore.QRect(-150, 20, 581, 141))
        self.label_23.setStyleSheet(_fromUtf8("background-image:url(captcha.png)"))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.Captcha = QtGui.QLineEdit(self.groupBox_9)
        self.Captcha.setGeometry(QtCore.QRect(4, 178, 441, 22))
        self.Captcha.setStyleSheet(_fromUtf8("background-color:white;\n"
""))
        self.Captcha.setObjectName(_fromUtf8("Captcha"))
        self.Validate = QtGui.QPushButton(self.groupBox_9)
        self.Validate.clicked.connect(self.captcha)
        self.Validate.setGeometry(QtCore.QRect(4, 200, 441, 28))
        self.Validate.setStyleSheet(_fromUtf8("font-weight:normal"))
        self.Validate.setObjectName(_fromUtf8("Validate"))
        self.groupBox_12 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_12.setGeometry(QtCore.QRect(469, 11, 451, 111))
        self.groupBox_12.setStyleSheet(_fromUtf8("font-weight: bold;"))
        self.groupBox_12.setObjectName(_fromUtf8("groupBox_12"))
        self.label_79 = QtGui.QLabel(self.groupBox_12)
        self.label_79.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_79.setStyleSheet(_fromUtf8("font-weight: normal;"))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.TuningFile2 = QtGui.QLineEdit(self.groupBox_12)
        self.TuningFile2.setReadOnly(True)
        self.TuningFile2.setGeometry(QtCore.QRect(90, 30, 261, 22))
        self.TuningFile2.setStyleSheet(_fromUtf8("background-color:white;\n"
"font-weight:normal"))
        self.TuningFile2.setObjectName(_fromUtf8("TuningFile2"))
        self.pushButton_6 = QtGui.QPushButton(self.groupBox_12)
        self.pushButton_6.clicked.connect(self.ATTACH)
        self.pushButton_6.setGeometry(QtCore.QRect(260, 60, 93, 31))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_80 = QtGui.QLabel(self.tab_4)
        self.label_80.setGeometry(QtCore.QRect(1, 538, 16, 16))
        self.label_80.setStyleSheet(_fromUtf8("background-image :url(nex.png);\n"
""))
        self.label_80.setText(_fromUtf8(""))
        self.label_80.setObjectName(_fromUtf8("label_80"))
        self.Tab2.addTab(self.tab_4, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.Tab2.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.Tab2.setCurrentIndex(0)
        self.Ba3()

    def send(self):
        self.FileTuning = self.TuningFile
        My_Options = ""
        My_Check = [self.Stage1,self.Stage2,self.Stage3,self.DPF,self.EGR,self.DTC,self.FLAPS,self.TQMo,self.VMAX]
        for chi in My_Check:
            if chi.isChecked():
                My_Options += chi.text() + "\n"


        Missing = False

                
        MyInputList1 = [self.Name,self.Email,self.Manu,self.Model,self.Engine,self.Year,self.HP]
        for K in MyInputList1:
            if K.text() == "":
                
                K.setStyleSheet("border : 1px solid red;background-color:white;font-weight:normal")
                Missing = True
            else:
                K.setStyleSheet("background-color:white;font-weight:normal")
        if Missing == True:
            Msg = QtGui.QMessageBox()
            Msg.setText("Please fill in all required fields")
            Msg.setWindowTitle("Missing fields")
            Msg.setIcon(QtGui.QMessageBox.Warning)
            Msg.show()
            Msg.exec_()
        else:
            f = open("he.txt", "w")
            f.write("""
Tuning File :

-Customer details :
    Customer Number : {}
    Name : {}
    E-mail : {}

-Car details :
    Manufacturer : {}
    Model : {}
    Engine : {}
    
-Desired functions :
{}Others : {}

-Year-HP-PS-GEARBOX :
    Year : {}
    HP : {}
    Gearbox : {}

-Comments : 
{}
""".format(self.CusNumber.text(),self.Name2.text(),self.Email.text(), self.Manu.text(),self.Model.text(), self.Engine.text(), My_Options,self.Others.text(),self.Year.text(),self.HP.text(), self.Gearbox.currentText(),self.Comments.toPlainText()))
            f.close()
            R.start()
            C.start()
            #self.Mail()

    def send2(self):
        self.FileTuning = self.TuningFile2
        Missing = False
        if self.Validate == 0:
            self.captcha()

                
        MyInputList = [self.Name2,self.Email2,self.Manu2,self.Model2,self.Engine2,self.Year2,self.HP2]
        for K in MyInputList:
            if K.text() == "":
                
                K.setStyleSheet("border : 1px solid red;background-color:white;font-weight:normal")
                Missing = True
            else:
                K.setStyleSheet("background-color:white;font-weight:normal")
        if Missing == True or self.Validate == 0:
            Msg = QtGui.QMessageBox()
            Msg.setText("Please fill in all required fields & validate captcha before you submit")
            Msg.setWindowTitle("Missing fields")
            Msg.setIcon(QtGui.QMessageBox.Warning)
            Msg.show()
            Msg.exec_()
        else:
            f = open("he.txt", "w")
            f.write("""
Support :

-Customer details :
    Name : {}
    E-mail : {}

-Car details :
    Manufacturer : {}
    Model : {}
    Engine : {}

-Year-HP-PS-GEARBOX :
    Year : {}
    HP : {}
    Gearbox : {}

-Comments : 
{}
""".format(self.Name2.text(),self.Email2.text(), self.Manu2.text(),self.Model2.text(), self.Engine2.text(), self.Year2.text(),self.HP2.text(), self.Gearbox2.currentText(),self.SupportComments.toPlainText()))
            f.close()
            print("passed")
            
            self.Mail()
    def captcha(self):
        if str(self.Captcha.text()) == str(self.My_Word):
            self.label_23.setGeometry(QtCore.QRect(-55, 20, 581, 141))
            self.label_23.setStyleSheet(_fromUtf8("background-image:url(yes.png);background-repeat:no-repeat;background-position:center;"))
            self.Validate = 1
            self.Captcha.setText("")

            self.Captcha.setStyleSheet(_fromUtf8("color:black;"))
            self.Captcha.setReadOnly(True)


        else:
            self.Captcha.setText("Wrong captcha, please try again")
            self.Captcha.setStyleSheet("color:red;background-color:white")
            self.Validate = 0
            self.Captcha.setReadOnly(False)
            self.Ba3()



    def Ba3(self):
        self.My_Color = random.choice(self.Color_liste)
        self.i = 0
        self.My_Word = ""
        while self.i <= 5:
            letter = random.choice(self.Ma_Liste)
            self.My_Word += letter
            self.i +=1
        font2 = ImageFont.truetype("arial.ttf", 70, encoding ="unic")
        Combined = ("d.png")
        te = self.My_Word
        txt = Image.new("RGBA", (750,200), (255,255,255,0))
        d = ImageDraw.Draw(txt)
        d.text((235,55), te, self.My_Color,font2)
        txt.save("captcha.png")
        self.label_23.setGeometry(QtCore.QRect(-150, 20, 581, 141))
        self.label_23.setStyleSheet(_fromUtf8("background-image:url(captcha.png);"))

    def Mail(self):
        self.msg = MIMEMultipart()
        self.msg["from"] = self.fromaddr
        self.msg["To"] = self.toaddr
        self.msg["subject"] = "File Exchange"
        fpr = open("he.txt", "r")
        fprr = fpr.read()
        fpr.close()
        self.body = fprr
        

        self.msg.attach(MIMEText(self.body,"plain"))
        self.fileatt = self.FileTuning.text()
        self.attachment = open(self.fileatt,"rb")
        self.part = MIMEBase("application", "octet-stream")
        self.part.set_payload((self.attachment).read())
        encoders.encode_base64(self.part)
        self.part.add_header("Content-Disposition", "attachment; filename = %s" % self.ProdName)
        self.msg.attach(self.part)

        self.server = smtplib.SMTP("smtp.gmail.com", 587)
        self.server.starttls()
        self.server.login(self.fromaddr, self.password)
        self.text = self.msg.as_string()
        self.server.sendmail(self.fromaddr,self.toaddr,self.text)
        self.server.quit()
        self.attachment.close()
        MSG = QtGui.QMessageBox()
        MSG.setWindowTitle("Mail")
        MSG.setText("Message sent : ")
        MSG.setIcon(QtGui.QMessageBox.Information)
        MSG.show()
        MSG.exec_()

    def sent(self):

        MSG = QtGui.QMessageBox()
        MSG.setWindowTitle("Mail")
        MSG.setText("Message sent : ")
        MSG.setIcon(QtGui.QMessageBox.Information)
        MSG.show()
        MSG.exec_()





    def OPEN(self):
        FDGG = QtGui.QFileDialog()        
                
        #FDG.exec_()
        gg = FDGG.getOpenFileName()
        self.TuningFile.setText(gg)
        nameit = self.TuningFile.text().split("/")
        self.ProdName = nameit[-1]



    def ATTACH(self):
        #print(self.TuningFile2.text())
        FDG = QtGui.QFileDialog()        
                
        #FDG.exec_()
        g = FDG.getOpenFileName()
        self.TuningFile2.setText(g)
        nameit = self.TuningFile2.text().split("/")
        self.ProdName = nameit[-1]


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Regal Tuning", None))
        self.label_21.setText(_translate("MainWindow", "* = Required fields !", None))
        self.pushButton_2.setText(_translate("MainWindow", "Send", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Comments : ", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Car details :", None))
        self.label_6.setText(_translate("MainWindow", "Manufacturer :", None))
        self.label_7.setText(_translate("MainWindow", "Model :", None))
        self.label_8.setText(_translate("MainWindow", "Engine :", None))
        self.label_9.setText(_translate("MainWindow", "*", None))
        self.label_10.setText(_translate("MainWindow", "*", None))
        self.label_11.setText(_translate("MainWindow", "*", None))
        self.groupBox.setTitle(_translate("MainWindow", "Customer :", None))
        self.label.setText(_translate("MainWindow", "Customer number", None))
        self.label_2.setText(_translate("MainWindow", "Name :", None))
        self.label_3.setText(_translate("MainWindow", "E-mail :", None))
        self.label_4.setText(_translate("MainWindow", "*", None))
        self.label_5.setText(_translate("MainWindow", "*", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "File :", None))
        self.label_14.setText(_translate("MainWindow", "Tuning File :", None))
        self.Open.setText(_translate("MainWindow", "Open", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Year - HP - Gearbox", None))
        self.label_15.setText(_translate("MainWindow", "Year :", None))
        self.label_16.setText(_translate("MainWindow", "HP :", None))
        self.label_17.setText(_translate("MainWindow", "Gearbox :", None))
        self.label_18.setText(_translate("MainWindow", "*", None))
        self.label_19.setText(_translate("MainWindow", "*", None))
        self.label_20.setText(_translate("MainWindow", "*", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Desired functions :", None))
        self.Stage1.setText(_translate("MainWindow", "STAGE1", None))
        self.Stage2.setText(_translate("MainWindow", "STAGE2", None))
        self.Stage3.setText(_translate("MainWindow", "STAGE3", None))
        self.DPF.setText(_translate("MainWindow", "DPF", None))
        self.EGR.setText(_translate("MainWindow", "EGR", None))
        self.TQMo.setText(_translate("MainWindow", "TQMo", None))
        self.DTC.setText(_translate("MainWindow", "DTC", None))
        self.VMAX.setText(_translate("MainWindow", "VMAX", None))
        self.FLAPS.setText(_translate("MainWindow", "FLAPS", None))
        self.label_12.setText(_translate("MainWindow", "Others :", None))
        self.Send.setText(_translate("MainWindow", "Send", None))
        self.label_22.setText(_translate("MainWindow", "* = Required fields !", None))
        self.Tab2.setTabText(self.Tab2.indexOf(self.tab_3), _translate("MainWindow", "Tuning File", None))
        self.Send2.setText(_translate("MainWindow", "Send", None))
        self.Send2.clicked.connect(self.send2)
        self.label_73.setText(_translate("MainWindow", "* = Required fields !", None))
        self.groupBox_10.setTitle(_translate("MainWindow", "Support Comments : ", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Year - HP - Gearbox", None))
        self.label_67.setText(_translate("MainWindow", "Year :", None))
        self.label_68.setText(_translate("MainWindow", "HP :", None))
        self.label_69.setText(_translate("MainWindow", "Gearbox :", None))
        self.label_70.setText(_translate("MainWindow", "*", None))
        self.label_71.setText(_translate("MainWindow", "*", None))
        self.label_72.setText(_translate("MainWindow", "*", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Car details :", None))
        self.label_53.setText(_translate("MainWindow", "Manufacturer :", None))
        self.label_55.setText(_translate("MainWindow", "Model :", None))
        self.label_63.setText(_translate("MainWindow", "Engine :", None))
        self.label_64.setText(_translate("MainWindow", "*", None))
        self.label_65.setText(_translate("MainWindow", "*", None))
        self.label_66.setText(_translate("MainWindow", "*", None))
        self.groupBox_11.setTitle(_translate("MainWindow", "Customer :", None))
        self.label_75.setText(_translate("MainWindow", "Name :", None))
        self.label_76.setText(_translate("MainWindow", "E-mail :", None))
        self.label_77.setText(_translate("MainWindow", "*", None))
        self.label_78.setText(_translate("MainWindow", "*", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Captcha :", None))
        self.Captcha.setText(_translate("MainWindow", "                                   Please insert captcha here ", None))
        self.Validate.setText(_translate("MainWindow", "Validate", None))
        self.groupBox_12.setTitle(_translate("MainWindow", "File :", None))
        self.label_79.setText(_translate("MainWindow", "Tuning File :", None))
        self.pushButton_6.setText(_translate("MainWindow", "Open", None))
        self.Tab2.setTabText(self.Tab2.indexOf(self.tab_4), _translate("MainWindow", "Support", None))



appp = Flask(__name__)
pub_key = "***********************"         #pk_live_3CP10SIlmiBFqZo4TLpY72cP"
secret_key = "**********************"      #'sk_live_e4aVgpugDdOvndOFzbPsL4lU'
stripe.api_key = secret_key
@appp.route("/")
def index():
    return render_template("index.html", pub_key = pub_key)

@appp.route("/thanks")
def thanks():
    return render_template("thanks.html", charge = str(charge))

@appp.route("/pay", methods = ["POST"])
def pay():
    global charge
    customer = stripe.Customer.create(email=request.form['stripeEmail'], source=request.form['stripeToken'])

    charge = stripe.Charge.create(
            customer=customer.id,
            amount=100,
            currency='gbp',
            description='Tuning File'
         )
    return redirect(url_for("thanks"))

class RunTheApp(QThread):
    def __init__(self):
        QThread.__init__(self)
        #Ui_MainWindow.__init__(self)
    def __del__(self):
        self.wait()
    def run(self):
        appp.run(threaded = True)

class CheckCharge(QThread):
    def __init__(self):
        QThread.__init__(self)
    def __del__(self):
        self.wait()
    def run(self):
        webbrowser.open("http://localhost:5000")
        while 1:
            try:
                print(str(charge))
                ui.Mail()
                ll = open(str(charge.id) + ".txt", "w")
                ll.write(str(charge))
                ll.close()
                break
            except:
                time.sleep(1)

R = RunTheApp()
C = CheckCharge()


import pics_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

