
import sys

from PyQt5 import QtGui, QtWidgets

from designer import Ui_MplMainWindow


class DesignerMainWindow(QtWidgets.QMainWindow, Ui_MplMainWindow):
    """Customization for Qt Designer created window"""

    def __init__(self, parent=None):
        super(DesignerMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.check)
        self.pushButton_4.clicked.connect(self.check)
        self.pushButton_5.clicked.connect(self.clean_s)
        self.pushButton_6.clicked.connect(self.clean_h)
        self.pushButton_8.clicked.connect(self.start_h)
        self.pushButton_7.clicked.connect(self.start_s)
        self.score_h = 0
        self.score_s = 0

    def start_s(self):
        self.tabWidget_4.setCurrentIndex(1)

    def start_h(self):
        self.tabWidget_3.setCurrentIndex(1)
    def check(self):
        self.score_h = 0
        self.score_s = 0
        if self.tabWidget.currentIndex() == 0:

            self.textEdit.setReadOnly(True)
            self.textEdit_2.setReadOnly(True)
            self.textEdit_7.setReadOnly(True)
            self.textEdit_8.setReadOnly(True)
            self.textEdit_9.setReadOnly(True)

            if self.label_3.text().replace(' ', '').replace('\n', '') == self.textEdit.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_h += 1


            if self.label_5.text().replace(' ', '').replace('\n', '') == self.textEdit_2.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_h += 1

            if self.label_17.text().replace(' ', '').replace('\n', '') == self.textEdit_7.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_h += 1
            if self.textEdit_8.toPlainText().replace(' ', '').replace('\n', '') == '18':
                self.score_h += 1
            print()
            if self.label_21.text().replace(' ', '').replace('\n', '') == self.textEdit_9.toPlainText().replace(' ', '').replace \
                    ('\n', '').replace('1241', '1279'):
                self.score_h += 1

            self.label_res_1.setText(str(self.score_h))


        elif self.tabWidget.currentIndex() == 1:

            self.textEdit_10.setReadOnly(True)
            self.textEdit_11.setReadOnly(True)
            self.textEdit_12.setReadOnly(True)
            self.textEdit_13.setReadOnly(True)
            self.textEdit_14.setReadOnly(True)

            print('society')
            print(self.label_25.text().replace(' ', '').replace('\n', '') )
            print(self.textEdit_11.toPlainText().replace('\n', '').replace(' ', ''))
            if self.label_23.text().replace(' ', '').replace('\n', '') == self.textEdit_10.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_s += 1
            if self.label_25.text().replace(' ', '').replace('\n', '') == self.textEdit_11.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_s += 1
            if self.label_27.text().replace(' ', '').replace('\n', '') == self.textEdit_12.toPlainText().replace(' ', '').replace \
                    ('\n', ''):
                self.score_s += 1
            if self.textEdit_13.toPlainText().replace(' ', '').replace('\n', '') == '870':
                self.score_s += 1

            if self.label_31.text().replace(' ', '').replace('\n', '') == self.textEdit_14.toPlainText().replace(' ', '').replace \
                    ('\n', '').replace('Либерализм', 'Консерватизм'):
                self.score_s += 1

            self.label_res_2.setText(str(self.score_s))

    def clean_h(self):
        self.textEdit.setText('')
        self.textEdit_2.setText('')
        self.textEdit_7.setText('')
        self.textEdit_9.setText('')
        self.textEdit_8.setText('')
        self.label_res_1.setText('')

        self.textEdit.setReadOnly(False)
        self.textEdit_2.setReadOnly(False)
        self.textEdit_7.setReadOnly(False)
        self.textEdit_8.setReadOnly(False)
        self.textEdit_9.setReadOnly(False)

    def clean_s(self):
        self.textEdit_10.setText('')
        self.textEdit_11.setText('')
        self.textEdit_12.setText('')
        self.textEdit_13.setText('')
        self.textEdit_14.setText('')
        self.label_res_2.setText('')

        self.textEdit_10.setReadOnly(False)
        self.textEdit_11.setReadOnly(False)
        self.textEdit_12.setReadOnly(False)
        self.textEdit_13.setReadOnly(False)
        self.textEdit_14.setReadOnly(False)


app = QtWidgets.QApplication(sys.argv)
dmw = DesignerMainWindow()
dmw.show()
sys.exit(app.exec_())
