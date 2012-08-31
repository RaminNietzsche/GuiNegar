# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created: Tue Aug 21 04:09:25 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import GNrc

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(545, 329)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("image/10649.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.textEdit = QtGui.QTextEdit(Dialog)
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QtCore.QRect(20, 20, 501, 291))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Nazli"))
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(_fromUtf8("     border-style: outset;\n"
"     border-width:2px;\n"
"     border-radius: 10px;\n"
"     border-color: black;\n"
"     font: bold 14px;\n"
"     margin-left:0;\n"
"     margin-right:0;\n"
"     position:absolute;\n"
"     opacity: 0.4; \n"
"     \n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 0), stop:1 rgba(0, 0, 0, 0));\n"
""))
        self.textEdit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse)
        self.textEdit.setObjectName(_fromUtf8("textEdit"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "درباره‌ی نگار و من", None, QtGui.QApplication.UnicodeUTF8))
        self.textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Nazli\'; font-size:14px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\":/image/image/Raaaaaaaaam2.jpg\" width=\"100\" style=\"float: left;\" /></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">چیزهای زیادی در موردِ من و </span><span style=\" font-size:11pt; font-weight:400; color:#ff007f;\">نگار</span><span style=\" font-size:11pt; font-weight:400;\"> وجود دارد اول اینکه اصلا خوشم نمی‌آید ازش. دوم اینکه نمی‌دانم چرا نامِ این پروژه </span><span style=\" font-size:11pt; font-weight:400; color:#ff007f;\">نگار</span><span style=\" font-size:11pt; font-weight:400;\"> شده و ترجیح می‌دادم هرچیزی می‌بود به غیر از این. سوم اینکه این پروژه متن باز است و از رابی به پایتون ترجمه شده رابی‌اش را آقایِ </span><span style=\" font-size:11pt; font-weight:400; color:#ff0000;\">عزیز</span><span style=\" font-size:11pt; font-weight:400;\"> نوشته و پایتون‌اش را</span><span style=\" font-size:11pt; font-weight:400; color:#ff5500;\"> شاهینِ آزاد</span><span style=\" font-size:11pt; font-weight:400;\"> و البته من هم گاهی کمی با کد پایتون‌اش ور می‌رفتم صرفا جهتِ تنوع.</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">پروژه را بردارید تغییر بدهید، بفروشید یا بدزدید یا هر چیزِ دیگری خلاصه در موردِ این پروژه آزادید هر کاری خواستید بکنید. حتی می‌توانید در توسعه‌ی آن مشارکت کنید:</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">اگر دوست داشتید اشکالات و نظراتِ‌تان را در موردِ </span><span style=\" font-size:11pt; font-weight:400; color:#ff007f;\">نگار</span><span style=\" font-size:11pt; font-weight:400;\"> (شخصِ خودش و یا پروژه‌اش با من در میان بگذارید)</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" fo font-size:13pt; font-weight:400;\">آدرس ایمیل من : Ramin.Najarbashi@Gmail.com</p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; font-weight:400;\">همین!</span></p>\n"
"<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:13pt; font-weight:400;\">آدرس پروژه در گیت هاب : https://github.com/RaminNietzsche/Negar</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

