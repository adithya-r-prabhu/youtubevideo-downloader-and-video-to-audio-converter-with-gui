from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pytube import YouTube
import os
from playsound import playsound
import platform
import subprocess
from youtubewebview import youtubewebviewclass

# error in pytube so do this before proceding https://github.com/pytube/pytube/issues/1105#issuecomment-907033591
# i have fixed this in this program by cloning the module from github and correcting inside it


class youtubewindowclass(object):
    def youtubewindow(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(400, 300)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(50, 0, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.urlbox = QtWidgets.QLineEdit(dialog)
        self.urlbox.setGeometry(QtCore.QRect(150, 60, 201, 25))
        self.urlbox.setObjectName("urlbox")
        self.Enter_urllabel = QtWidgets.QLabel(dialog)
        self.Enter_urllabel.setGeometry(QtCore.QRect(20, 50, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.Enter_urllabel.setFont(font)
        self.Enter_urllabel.setObjectName("Enter_urllabel")
        self.Downloadbutton = QtWidgets.QPushButton(dialog)
        self.Downloadbutton.setGeometry(QtCore.QRect(170, 100, 151, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.Downloadbutton.setFont(font)
        self.Downloadbutton.setObjectName("Downloadbutton")
        self.Downloadbutton.clicked.connect(self.on_click_downloadbutton)
        self.orlabel = QtWidgets.QLabel(dialog)
        self.orlabel.setGeometry(QtCore.QRect(140, 160, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.orlabel.setFont(font)
        self.orlabel.setObjectName("orlabel")
        self.searchinyoutublabel = QtWidgets.QLabel(dialog)
        self.searchinyoutublabel.setGeometry(QtCore.QRect(10, 200, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.searchinyoutublabel.setFont(font)
        self.searchinyoutublabel.setObjectName("searchinyoutublabel")
        self.openyoutubebutton = QtWidgets.QPushButton(dialog)
        self.openyoutubebutton.setGeometry(QtCore.QRect(240, 200, 151, 41))
        self.openyoutubebutton.clicked.connect(self.on_click_openyoutubebutton)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.openyoutubebutton.setFont(font)
        self.openyoutubebutton.setObjectName("openyoutubebutton")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Dialog"))
        self.label.setText(_translate("dialog", "Youtube video Downloader"))
        self.Enter_urllabel.setText(_translate("dialog", "Enter url:"))
        self.Downloadbutton.setText(_translate("dialog", "Download "))
        self.orlabel.setText(_translate("dialog", "or"))
        self.searchinyoutublabel.setText(_translate("dialog", "Search in youtube:"))
        self.openyoutubebutton.setText(_translate("dialog", "open youtube"))

    def on_click_downloadbutton(self):
        youtube_video_url = a = self.urlbox.text()
        try:
            yt_obj = YouTube(youtube_video_url)

            filters = yt_obj.streams.filter(progressive=True, file_extension="mp4")

            folderpath_to_save_youtube_video = (
                QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
            )

            filters.get_highest_resolution().download(
                output_path=folderpath_to_save_youtube_video, filename="yt_video.mp4"
            )

        except Exception as e:
            print(e)

        path = folderpath_to_save_youtube_video
        playsound("sounds/sound_effect_when_task_done.mp3")

        if platform.system() == "Windows":
            os.startfile(path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", path])
        else:
            subprocess.Popen(["xdg-open", path])

    def on_click_openyoutubebutton(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = youtubewebviewclass()
        self.ui.youtubewebviewwindow(self.window2)
        self.window2.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = youtubewindowclass()
    ui.youtubewindow(dialog)
    dialog.show()
    sys.exit(app.exec_())
