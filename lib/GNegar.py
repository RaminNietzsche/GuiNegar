# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GNegar.ui'
#
# Created: Tue Aug 21 18:41:24 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

#--------------------------Form Maker----------------------------
from PyQt4 import QtCore, QtGui                                 #
import GNrc                                                     #
#------------------------Suggest Menu----------------------------
from PyQt4.Qt import QTextCursor                                #
import enchant                                                  #
from PyQt4.Qt import QMenu                                      #
from PyQt4.Qt import QCursor                                    #
from PyQt4.Qt import QPoint                                     #
from PyQt4.Qt import QAction                                    #
from PyQt4.QtCore import pyqtSignal                             #
from PyQt4.Qt import QSyntaxHighlighter                         #
from PyQt4.Qt import QTextCharFormat                            #
import re                                                       #
import sys                                                      #
from PyQt4.Qt import QApplication                               #
from PyQt4.Qt import QEvent                                     #
from PyQt4.Qt import QMouseEvent                                #
#from PyQt4.Qt import QPlainTextEdit                            #
from PyQt4.Qt import Qt                                         #
#----------------------------------------------------------------

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s
#--------------------------------------------------------
#         ___  _     _____ ___  ____  __  __            #
#        / _ \| |_  |  ___/ _ \|  _ \|  \/  |           #
#       | | | | __| | |_ | | | | |_) | |\/| |           #
#       | |_| | |_  |  _|| |_| |  _ <| |  | |           #
#        \__\_\\__| |_|   \___/|_| \_\_|  |_|           #
#                                                       #
#         open GNegar.ui by designer-qt4 ;)             #
#--------------------------------------------------------
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 605)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/image/image/ico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(_fromUtf8("QToolTip {\n"
"     border: 2px solid darkkhaki;\n"
"     padding: 5px;\n"
"     border-radius: 10px;\n"
"     opacity: 200; \n"
"}"))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        MainWindow.setDocumentMode(True)
        self.dict = enchant.DictWithPWL("fa_IR","fa.dic")#enchant.Dict() -----------------------> Dictionary For Suggestion!!!
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.MainFrame = QtGui.QFrame(self.centralwidget)
        self.MainFrame.setGeometry(QtCore.QRect(10, 10, 781, 561))
        self.MainFrame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.MainFrame.setStyleSheet(_fromUtf8(" #MainFrame {\n"
"     background-color: white;\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
" }"))
        self.MainFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.MainFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.MainFrame.setObjectName(_fromUtf8("MainFrame"))
        self.TextFrame = QtGui.QFrame(self.MainFrame)
        self.TextFrame.setGeometry(QtCore.QRect(10, 280, 761, 271))
        self.TextFrame.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.TextFrame.setStyleSheet(_fromUtf8("#TextFrame {\n"
"     background-color: rgb(232, 232, 232);\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
"}"))
        self.TextFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.TextFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.TextFrame.setObjectName(_fromUtf8("TextFrame"))
        self.textEdit = QtGui.QTextEdit(self.TextFrame)
        self.textEdit.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.textEdit.customContextMenuRequested.connect(self.contextMenuEvent)
        self.textEdit.highlighter = Highlighter(self.textEdit)
        self.textEdit.highlighter.setDict(self.dict)
        #self.textEdit.mousePressEvent.connect(self.mousePressEvent)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 741, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("#textEdit {\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
"}\n"
"\n"
"QToolTip {\n"
"     border: 2px solid darkkhaki;\n"
"     padding: 5px;\n"
"     border-radius: 10px;\n"
"     opacity: 200; \n"
"}"))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.SetFrame = QtGui.QFrame(self.MainFrame)
        self.SetFrame.setGeometry(QtCore.QRect(10, 40, 591, 231))
        self.SetFrame.setStyleSheet(_fromUtf8("#SetFrame {\n"
"     background-color: rgb(232, 232, 232);\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"     border-color: beige;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
"}\n"
"\n"
"QToolTip {\n"
"     border: 2px solid darkkhaki;\n"
"     padding: 5px;\n"
"     border-radius: 10px;\n"
"     opacity: 200; \n"
"     width: 2000px;\n"
"}"))
        self.SetFrame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.SetFrame.setFrameShadow(QtGui.QFrame.Raised)
        self.SetFrame.setObjectName(_fromUtf8("SetFrame"))
        self.fix_dashes = QtGui.QCheckBox(self.SetFrame)
        self.fix_dashes.setGeometry(QtCore.QRect(280, 10, 301, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        font.setPointSize(11)
        self.fix_dashes.setFont(font)
        self.fix_dashes.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_dashes.setObjectName(_fromUtf8("fix_dashes"))
        self.cleanup_zwnj = QtGui.QCheckBox(self.SetFrame)
        self.cleanup_zwnj.setGeometry(QtCore.QRect(330, 30, 251, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.cleanup_zwnj.setFont(font)
        self.cleanup_zwnj.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.cleanup_zwnj.setObjectName(_fromUtf8("cleanup_zwnj"))
        self.fix_three_dots = QtGui.QCheckBox(self.SetFrame)
        self.fix_three_dots.setGeometry(QtCore.QRect(380, 50, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_three_dots.setFont(font)
        self.fix_three_dots.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_three_dots.setObjectName(_fromUtf8("fix_three_dots"))
        self.fix_english_quotes = QtGui.QCheckBox(self.SetFrame)
        self.fix_english_quotes.setGeometry(QtCore.QRect(380, 70, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_english_quotes.setFont(font)
        self.fix_english_quotes.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_english_quotes.setObjectName(_fromUtf8("fix_english_quotes"))
        self.fix_spacing_for_braces_and_quotes = QtGui.QCheckBox(self.SetFrame)
        self.fix_spacing_for_braces_and_quotes.setGeometry(QtCore.QRect(380, 90, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_spacing_for_braces_and_quotes.setFont(font)
        self.fix_spacing_for_braces_and_quotes.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_spacing_for_braces_and_quotes.setObjectName(_fromUtf8("fix_spacing_for_braces_and_quotes"))
        self.fix_LTRM_RTLM = QtGui.QCheckBox(self.SetFrame)
        self.fix_LTRM_RTLM.setGeometry(QtCore.QRect(380, 110, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_LTRM_RTLM.setFont(font)
        self.fix_LTRM_RTLM.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_LTRM_RTLM.setObjectName(_fromUtf8("fix_LTRM_RTLM"))
        self.fix_arabic_numbers = QtGui.QCheckBox(self.SetFrame)
        self.fix_arabic_numbers.setGeometry(QtCore.QRect(380, 130, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_arabic_numbers.setFont(font)
        self.fix_arabic_numbers.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_arabic_numbers.setObjectName(_fromUtf8("fix_arabic_numbers"))
        self.fix_english_numbers = QtGui.QCheckBox(self.SetFrame)
        self.fix_english_numbers.setGeometry(QtCore.QRect(380, 150, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_english_numbers.setFont(font)
        self.fix_english_numbers.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_english_numbers.setObjectName(_fromUtf8("fix_english_numbers"))
        self.fix_misc_non_persian_chars = QtGui.QCheckBox(self.SetFrame)
        self.fix_misc_non_persian_chars.setGeometry(QtCore.QRect(380, 170, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_misc_non_persian_chars.setFont(font)
        self.fix_misc_non_persian_chars.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_misc_non_persian_chars.setObjectName(_fromUtf8("fix_misc_non_persian_chars"))
        self.fix_perfix_spacing = QtGui.QCheckBox(self.SetFrame)
        self.fix_perfix_spacing.setGeometry(QtCore.QRect(380, 190, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_perfix_spacing.setFont(font)
        self.fix_perfix_spacing.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_perfix_spacing.setObjectName(_fromUtf8("fix_perfix_spacing"))
        self.fix_suffix_spacing = QtGui.QCheckBox(self.SetFrame)
        self.fix_suffix_spacing.setGeometry(QtCore.QRect(73, 10, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_suffix_spacing.setFont(font)
        self.fix_suffix_spacing.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_suffix_spacing.setObjectName(_fromUtf8("fix_suffix_spacing"))
        self.cleanup_extra_marks_2 = QtGui.QCheckBox(self.SetFrame)
        self.cleanup_extra_marks_2.setGeometry(QtCore.QRect(73, 30, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.cleanup_extra_marks_2.setFont(font)
        self.cleanup_extra_marks_2.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.cleanup_extra_marks_2.setObjectName(_fromUtf8("cleanup_extra_marks_2"))
        self.cleanup_kashidas = QtGui.QCheckBox(self.SetFrame)
        self.cleanup_kashidas.setGeometry(QtCore.QRect(73, 50, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.cleanup_kashidas.setFont(font)
        self.cleanup_kashidas.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.cleanup_kashidas.setObjectName(_fromUtf8("cleanup_kashidas"))
        self.cleanup_spacing = QtGui.QCheckBox(self.SetFrame)
        self.cleanup_spacing.setGeometry(QtCore.QRect(73, 70, 201, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.cleanup_spacing.setFont(font)
        self.cleanup_spacing.setStyleSheet(_fromUtf8(" QCheckBox {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
" QCheckBox::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
" QCheckBox::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QCheckBox::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.cleanup_spacing.setObjectName(_fromUtf8("cleanup_spacing"))
        self.fix_hamzeh = QtGui.QRadioButton(self.SetFrame)
        self.fix_hamzeh.setGeometry(QtCore.QRect(123, 90, 151, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.fix_hamzeh.setFont(font)
        self.fix_hamzeh.setStyleSheet(_fromUtf8("  QRadioButton {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
"  QRadioButton::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
"  QRadioButton::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QRadioButton::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.fix_hamzeh.setObjectName(_fromUtf8("fix_hamzeh"))
        self.hamzeh_with_yeh = QtGui.QRadioButton(self.SetFrame)
        self.hamzeh_with_yeh.setGeometry(QtCore.QRect(160, 110, 114, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.hamzeh_with_yeh.setFont(font)
        self.hamzeh_with_yeh.setStyleSheet(_fromUtf8("  QRadioButton {\n"
"     spacing: 5px;\n"
" }\n"
"\n"
"  QRadioButton::indicator {\n"
"     width: 13px;\n"
"     height: 13px;\n"
" }\n"
"\n"
"  QRadioButton::indicator:unchecked {\n"
"    image: url(:/image/image/checkbox-unchecked.png);\n"
" }\n"
"\n"
" QRadioButton::indicator:checked {\n"
"    image: url(:/image/image/checkbox-checked.png);\n"
" }\n"
""))
        self.hamzeh_with_yeh.setObjectName(_fromUtf8("hamzeh_with_yeh"))
        self.Runit = QtGui.QPushButton(self.SetFrame)
        self.Runit.setGeometry(QtCore.QRect(110, 150, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        self.Runit.setFont(font)
        self.Runit.setStyleSheet(_fromUtf8("QPushButton:disabled{ background-color: yellow; }\n"
"QPushButton:pressed{ background-color: orange; }\n"
"QPushButton:focus:pressed{ background-color: rgb(255, 255, 255); }\n"
"QPushButton:focus{ background-color: rgb(164, 255, 44); }\n"
"QPushButton:hover{ background-color: rgb(255, 255, 127); }\n"
"QPushButton:checked{ background-color: pink; }\n"
"QPushButton {\n"
"padding: 50px 50 50 0;\n"
"background-image: url(:/image/image/ok.png);\n"
"background-repeat:no-repeat;\n"
"background-attachment:fixed;\n"
"background-position:center; \n"
"     background-color:  rgb(184, 225, 255);\n"
"     border-style: outset;\n"
"     border-width: 2px;\n"
"     border-radius: 10px;\n"
"}\n"
""))
        self.Runit.setObjectName(_fromUtf8("Runit"))
        self.Logo = QtGui.QLabel(self.MainFrame)
        self.Logo.setGeometry(QtCore.QRect(630, 67, 131, 171))
        self.Logo.setObjectName(_fromUtf8("Logo"))
        self.AboutPush = QtGui.QPushButton(self.MainFrame)
        self.AboutPush.setGeometry(QtCore.QRect(620, 40, 141, 211))
        self.AboutPush.setStyleSheet(_fromUtf8("QPushButton {\n"
"padding: 50px 50 50 0;\n"
"background-image: url(:/image/image/ok.png);\n"
"background-repeat:no-repeat;\n"
"background-attachment:fixed;\n"
"background-position:center; \n"
"     border-style: outset;\n"
"     border-width: 0px;\n"
"     border-radius: 10px;\n"
"}"))
        self.AboutPush.setText(_fromUtf8(""))
        self.AboutPush.setObjectName(_fromUtf8("AboutPush"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setStatusTip(_fromUtf8(""))
        self.statusbar.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "نگار - ویراستار فارسی", None, QtGui.QApplication.UnicodeUTF8))
        MainWindow.setStatusTip(QtGui.QApplication.translate("MainWindow", "برنامه‌ی ویرایش متون فارسی. ", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setToolTip(QtGui.QApplication.translate("MainWindow", "متن خود را وارد کنید...", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setStatusTip(QtGui.QApplication.translate("MainWindow", "محل درج متن", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nazli\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
"<p dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:11pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SetFrame.setToolTip(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p>تنظیمات مربوط به ویرایش متن</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.SetFrame.setStatusTip(QtGui.QApplication.translate("MainWindow", "انتخاب مواردی که می خوایید بر روی متن اعمال شود", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_dashes.setText(QtGui.QApplication.translate("MainWindow", "تبدیل علامت منهای پی در پی به خط کشیده", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanup_zwnj.setText(QtGui.QApplication.translate("MainWindow", "حذف نیم‌فاصله‌های غیر ضروری", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_three_dots.setText(QtGui.QApplication.translate("MainWindow", "تبدیل سه نقطه به نویسه‌ی صحیح", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_english_quotes.setText(QtGui.QApplication.translate("MainWindow", "استفاده از گیومه‌ی فارسی", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_spacing_for_braces_and_quotes.setText(QtGui.QApplication.translate("MainWindow", "تنظیم فاصله گذاری متون", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_LTRM_RTLM.setText(QtGui.QApplication.translate("MainWindow", "تصحیح چینش متن", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_arabic_numbers.setText(QtGui.QApplication.translate("MainWindow", "تبدیل اعداد عربی به فارسی", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_english_numbers.setText(QtGui.QApplication.translate("MainWindow", "تبدیل اعداد انگلیسی به فارسی", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_misc_non_persian_chars.setText(QtGui.QApplication.translate("MainWindow", "تبدیل علائم غیر فارسی با فارسی", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_perfix_spacing.setText(QtGui.QApplication.translate("MainWindow", "افزودن نیم‌فاصله به پیشوندها", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_suffix_spacing.setText(QtGui.QApplication.translate("MainWindow", "افزودن نیم‌فاصله به پسوندها", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanup_extra_marks_2.setText(QtGui.QApplication.translate("MainWindow", "حذف علامت تعحب و سوال اضافی", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanup_kashidas.setText(QtGui.QApplication.translate("MainWindow", "حذف نویسه‌ی وصل مجازی", None, QtGui.QApplication.UnicodeUTF8))
        self.cleanup_spacing.setText(QtGui.QApplication.translate("MainWindow", "حذف فاصله‌های اضافه", None, QtGui.QApplication.UnicodeUTF8))
        self.fix_hamzeh.setText(QtGui.QApplication.translate("MainWindow", "تبدیل ‌‌هٔ به ه‌ی", None, QtGui.QApplication.UnicodeUTF8))
        self.hamzeh_with_yeh.setText(QtGui.QApplication.translate("MainWindow", "تبدیل ‌‌ه‌ی به هٔ ", None, QtGui.QApplication.UnicodeUTF8))
        self.Runit.setText(QtGui.QApplication.translate("MainWindow", "اعمال", None, QtGui.QApplication.UnicodeUTF8))
        self.Logo.setText(QtGui.QApplication.translate("MainWindow", "<html><head/><body><p><img src=\":/image/image/10649.png\"/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.AboutPush.setToolTip(QtGui.QApplication.translate("MainWindow", "درباره‌ی من و نگار!", None, QtGui.QApplication.UnicodeUTF8))
        self.AboutPush.setStatusTip(QtGui.QApplication.translate("MainWindow", "درباره‌ی من و نگار!", None, QtGui.QApplication.UnicodeUTF8))


#----------------------------------------------------------------
#        ____                __  __ _____ _   _ _   _           #
#       / ___| _   _  __ _  |  \/  | ____| \ | | | | |          #
#       \___ \| | | |/ _` | | |\/| |  _| |  \| | | | |          #
#        ___) | |_| | (_| | | |  | | |___| |\  | |_| |          #
#       |____/ \__,_|\__, | |_|  |_|_____|_| \_|\___/           #
#                    |___/                                      #
#                                                               #
#          Make Suggestion menu for wrong words ;)              #
#----------------------------------------------------------------

    def contextMenuEvent(self, event):#pos):
        popup_menu = self.textEdit.createStandardContextMenu()#pos)
 
        # Select the word under the cursor.
        cursor = self.textEdit.textCursor()
        cursor.select(QTextCursor.WordUnderCursor)
        self.textEdit.setTextCursor(cursor)
 
        # Check if the selected word is misspelled and offer spelling
        # suggestions if it is.
        if self.textEdit.textCursor().hasSelection():
            text = unicode(self.textEdit.textCursor().selectedText())
            if not self.dict.check(text):
                #print "o0mad to0 dict :D"
                spell_menu = QMenu(u'شاید منظورتان این بوده:')
                #print spell_menu
                for word in self.dict.suggest(text):
                    action = SpellAction(word, spell_menu)
                    action.correct.connect(self.correctWord)
                    spell_menu.addAction(action)
                    #print word
                # Only add the spelling suggests to the menu if there are
                # suggestions.
                print len(spell_menu.actions())
                #print spell_menu.actions()
                if len(spell_menu.actions()) != 0:
                    popup_menu.insertSeparator(popup_menu.actions()[0])
                    popup_menu.insertMenu(popup_menu.actions()[0], spell_menu)
 
        popup_menu.exec_(QCursor.pos())#self.textEdit.mapToGlobal(QPoint(0, 0)))#.globalPos())
        #popup_menu.popup(pos)
 
        
        
    def proposalSelected(self, selectedWord):
        fixed = do(selectedWord)
        self.textEdit.textCursor().insertText(fixed)
        
    def mousePressEvent(self, event):
        if event.button() == Qt.RightButton:
            # Rewrite the mouse event to a left button event so the cursor is
            # moved to the location of the pointer.
            event = QMouseEvent(QEvent.MouseButtonPress, event.pos(),
                Qt.LeftButton, Qt.LeftButton, Qt.NoModifier)
        QTextEdit.mousePressEvent(self, event)        
        
    def correctWord(self, word):
        '''
        Replaces the selected text with word.
        '''
        cursor = self.textEdit.textCursor()
        cursor.beginEditBlock()
 
        cursor.removeSelectedText()
        cursor.insertText(word)
 
        cursor.endEditBlock()
 
 
class Highlighter(QSyntaxHighlighter):
 
    WORDS = u'(?iu)[\w\']+'
 
    def __init__(self, *args):
        QSyntaxHighlighter.__init__(self, *args)
 
        self.dict = None
 
    def setDict(self, dict):
        self.dict = dict
 
    def highlightBlock(self, text):
        if not self.dict:
            return
 
        text = unicode(text)
 
        format = QTextCharFormat()
        format.setUnderlineColor(Qt.red)
        format.setUnderlineStyle(QTextCharFormat.SpellCheckUnderline)
 
        for word_object in re.finditer(self.WORDS, text):
            if not self.dict.check(word_object.group()):
                self.setFormat(word_object.start(),
                    word_object.end() - word_object.start(), format)
         
        
class SpellAction(QAction):
 
    '''
    A special QAction that returns the text in a signal.
    '''
 
    correct = pyqtSignal(unicode)
 
    def __init__(self, *args):
        QAction.__init__(self, *args)
 
        self.triggered.connect(lambda x: self.correct.emit(
            unicode(self.text())))
 
