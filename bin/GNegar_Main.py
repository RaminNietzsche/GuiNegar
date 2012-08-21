#-*- coding: utf-8 -*-

import getopt
import sys
from PyQt4 import QtGui,QtCore
from lib.GNegar import *
from lib.Virastar import PersianEditor
from lib.VirAbout import *
#from GNegar import GlobalValues

class GlobalValues(object):
        global text
        global text2
        global fix_dashes
        global fix_three_dots
        global fix_english_quotes
        global fix_hamzeh
        global hamzeh_with_yeh
        global cleanup_zwnj
        global fix_spacing_for_braces_and_quotes
        global fix_LTRM_RTLM
        global fix_arabic_numbers
        global fix_english_numbers
        global fix_misc_non_persian_chars
        global fix_perfix_spacing
        global fix_suffix_spacing
        global aggresive
        global cleanup_kashidas
        global cleanup_extra_marks
        global cleanup_spacing
        text2 = ""
        fix_dashes = False
        fix_three_dots = False
        fix_english_quotes = False
        fix_hamzeh = True
        hamzeh_with_yeh = False
        cleanup_zwnj = False
        fix_spacing_for_braces_and_quotes = False
        fix_LTRM_RTLM = False
        fix_arabic_numbers = False
        fix_english_numbers = False
        fix_misc_non_persian_chars = False
        fix_perfix_spacing = False
        fix_suffix_spacing = False
        aggresive = True
        cleanup_kashidas = False
        cleanup_extra_marks = False
        cleanup_spacing = False
       
    
class frmMain(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.center()
        self.GetText()
        self.ui.Runit.clicked[bool].connect(self.RunlolaRun)
        self.ui.fix_dashes.stateChanged.connect(self.fix_dashes)
        self.ui.fix_three_dots.stateChanged.connect(self.fix_three_dots)
        self.ui.fix_english_quotes.stateChanged.connect(self.fix_english_quotes)
        self.ui.fix_hamzeh.clicked[bool].connect(self.fix_hamzeh)
        self.ui.hamzeh_with_yeh.clicked[bool].connect(self.hamzeh_with_yeh)
        self.ui.cleanup_zwnj.stateChanged.connect(self.cleanup_zwnj)
        self.ui.fix_spacing_for_braces_and_quotes.stateChanged.connect(self.fix_spacing_for_braces_and_quotes)
        self.ui.fix_LTRM_RTLM.stateChanged.connect(self.fix_LTRM_RTLM)
        self.ui.fix_arabic_numbers.stateChanged.connect(self.fix_arabic_numbers)
        self.ui.fix_english_numbers.stateChanged.connect(self.fix_english_numbers)
        self.ui.fix_misc_non_persian_chars.stateChanged.connect(self.fix_misc_non_persian_chars)
        self.ui.fix_perfix_spacing.stateChanged.connect(self.fix_perfix_spacing)
        self.ui.fix_suffix_spacing.stateChanged.connect(self.fix_suffix_spacing)
#        self.ui.aggresive.stateChanged.connect(self.aggresive)
        self.ui.cleanup_kashidas.stateChanged.connect(self.cleanup_kashidas)
        self.ui.cleanup_extra_marks_2.stateChanged.connect(self.cleanup_extra_marks)
        self.ui.cleanup_spacing.stateChanged.connect(self.cleanup_spacing)
        self.ui.AboutPush.clicked[bool].connect(self.AboutUs)
        
    def closeEvent(self, event):       
        st=u'آیا قصد خروج از برنامه را دارید؟'
        reply = QtGui.QMessageBox.question(self, u'هشدار',
            st, QtGui.QMessageBox.Yes | 
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 
            
    def center(self):       
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())            

    def GetText(self):
        return self.ui.textEdit.toPlainText ()
        
    def RunlolaRun(self, pressed):
        for line in self.GetText().split('\n'):
            if len(line) == 0:
                continue
            st = (unicode(line.toUtf8(), "utf-8"))  
            run_PE.text = unicode(st)
            globals()["text2"]=globals()["text2"]+unicode(run_PE.cleanup())+"\n"
        self.ui.textEdit.setText(globals()["text2"])
        globals()["text2"]=""
 
    def fix_dashes(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_dashes = True
        else:
            run_PE.fix_dashes = False

    def fix_three_dots(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_three_dots = True
        else:
            run_PE.fix_three_dots = False

    def fix_english_quotes(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_english_quotes = True
        else:
            run_PE.fix_english_quotes = False

    def fix_hamzeh(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.hamzeh_with_yeh = False
        else:
            run_PE.hamzeh_with_yeh = True

    def hamzeh_with_yeh(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.hamzeh_with_yeh = True
        else:
            run_PE.hamzeh_with_yeh = False

    def cleanup_zwnj(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.cleanup_zwnj = True
        else:
            run_PE.cleanup_zwnj = False

    def fix_spacing_for_braces_and_quotes(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_spacing_for_braces_and_quotes = True
        else:
            run_PE.fix_spacing_for_braces_and_quotes = False

    def fix_LTRM_RTLM(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_LTRM_RTLM = True
        else:
            run_PE.fix_LTRM_RTLM = False

    def fix_arabic_numbers(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_arabic_numbers = True
        else:
            run_PE.fix_arabic_numbers = False

    def fix_english_numbers(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_english_numbers = True
        else:
            run_PE.fix_english_numbers = False

    def fix_misc_non_persian_chars(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_misc_non_persian_chars = True
        else:
            run_PE.fix_misc_non_persian_chars = False

    def fix_perfix_spacing(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_perfix_spacing = True
        else:
            run_PE.fix_perfix_spacing = False

    def fix_suffix_spacing(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.fix_suffix_spacing = True
        else:
            run_PE.fix_suffix_spacing = False

    def cleanup_kashidas(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.cleanup_kashidas = True
        else:
            run_PE.cleanup_kashidas = False

    def cleanup_extra_marks(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.cleanup_extra_marks = True
        else:
            run_PE.cleanup_extra_marks = False

    def cleanup_spacing(self, state):
        if state == QtCore.Qt.Checked:
            run_PE.cleanup_spacing = True
        else:
            run_PE.cleanup_spacing = False
            
    def AboutUs(self, state):
        QtGui.QWidget.__init__(self, parent=None)
        Dialog2 = QtGui.QDialog()
        ui2 = Ui_Dialog()
        ui2.setupUi(Dialog2)
        Dialog2.exec_()
        

def cleanUpAllCheck():
        run_PE.fix_dashes  = False
        run_PE.fix_three_dots  = False
        run_PE.fix_english_quotes  = False
        run_PE.fix_hamzeh  = True
        run_PE.hamzeh_with_yeh  = False
        run_PE.cleanup_zwnj  = False
        run_PE.fix_spacing_for_braces_and_quotes  = False
        run_PE.fix_LTRM_RTLM  = False
        run_PE.fix_arabic_numbers  = False
        run_PE.fix_english_numbers  = False
        run_PE.fix_misc_non_persian_chars  = False
        run_PE.fix_perfix_spacing  = False
        run_PE.fix_suffix_spacing  = False
        run_PE.aggresive  = True
        run_PE.cleanup_kashidas  = False
        run_PE.cleanup_extra_marks  = False
        run_PE.cleanup_spacing  = False

def About():
        app2 = QtGui.QApplication(sys.argv)
        Dialog2 = QtGui.QDialog()
        ui2 = Ui_Dialog()
        ui2.setupUi(Dialog2)
        Dialog2.show()
        sys.exit(app.exec_())


global run_PE
run_PE = PersianEditor("")

if __name__ == "__main__":
  cleanUpAllCheck()
  app = QtGui.QApplication(sys.argv)
  MainWindow = frmMain()
  MainWindow.show()
  sys.exit(app.exec_())

