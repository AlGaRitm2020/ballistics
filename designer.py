

import sys

import PyQt5.QtCore as QtCore

from PyQt5 import QtGui, QtWidgets

from designer import Ui_MplMainWindow


class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    """Customization for Qt Designer created window"""

    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        

        self.score = 0
        self.obj = [(self.lineEdit.value(), self.label.value()),
                    (self.lineEdit1.value(), self.label1.value()),
                    (self.lineEdit2.value(), self.label2.value()),
                    (self.lineEdit3.value(), self.label3.value()),
                    (self.lineEdit4.value(), self.label4.value()),
                    (self.lineEdit5.value(), self.label5.value()),
                    (self.lineEdit6.value(), self.label6.value()),
                    (self.lineEdit7.value(), self.label7.value()),
                    (self.lineEdit8.value(), self.label8.value()),
                    (self.lineEdit9.value(), self.label9.value())]
    def check(self):
        
        for i, turple in enumerate(self.obj):
            edit = turple[0]
            label = turple[1]
            if i == 4:
               if label     
                
            if edit == label:
                self.score += 1
            
        self.label_res.setText(str(self.score))    




# create the GUI application
app = QtWidgets.QApplication(sys.argv)
# instantiate the main window
dmw = DesignerMainWindow()
# show it
dmw.show()
# start the Qt main loop execution, exiting from this script
# with the same return code of Qt application
sys.exit(app.exec_())
