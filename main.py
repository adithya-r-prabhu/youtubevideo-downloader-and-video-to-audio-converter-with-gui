from PyQt5 import QtCore, QtGui, QtWidgets
from youtubedownloader import youtubewindowclass
from converertorgui import convertorwindowclass


# error in pytube so do this before proceding https://github.com/pytube/pytube/issues/1105#issuecomment-907033591
# i have fixed this in this program by cloning the module from github and correcting inside it


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(472, 334)
        self.Heading = QtWidgets.QLabel(Dialog)
        self.Heading.setGeometry(QtCore.QRect(125, 0, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.Heading.setFont(font)
        self.Heading.setAutoFillBackground(False)
        self.Heading.setObjectName("Heading")
        self.youtubevidedownloadbutton = QtWidgets.QPushButton(Dialog)
        self.youtubevidedownloadbutton.setGeometry(QtCore.QRect(30, 60, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.youtubevidedownloadbutton.setFont(font)
        self.youtubevidedownloadbutton.setObjectName("youtubevidedownloadbutton")
        self.youtubevidedownloadbutton.clicked.connect(
            self.on_click_youtubebutton
        )  # connecting
        self.converterbutton = QtWidgets.QPushButton(Dialog)
        self.converterbutton.setGeometry(QtCore.QRect(250, 60, 151, 41))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.converterbutton.setFont(font)
        self.converterbutton.setObjectName("converterbutton")
        self.converterbutton.clicked.connect(
            self.on_click_converterbutton
        )  # connecting

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Productivity Tools"))
        self.Heading.setText(_translate("Dialog", "Productivity Tools"))
        self.youtubevidedownloadbutton.setText(_translate("Dialog", "▶️Youtube video "))
        self.converterbutton.setText(_translate("Dialog", "🔄Video 2 Audio"))

    def on_click_youtubebutton(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = youtubewindowclass()
        self.ui.youtubewindow(self.window)
        self.window.show()

    def on_click_converterbutton(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = convertorwindowclass()
        self.ui.covertorwindow(self.window1)
        self.window1.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
