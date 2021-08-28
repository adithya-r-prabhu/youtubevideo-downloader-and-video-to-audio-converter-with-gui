from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5 import QtWebEngineCore
from PyQt5.QtWebEngineWidgets import QWebEngineSettings
from PyQt5.QtWidgets import QFileDialog
from pytube import YouTube
import os, time
from playsound import playsound
import platform
import subprocess

# error in pytube so do this before proceding https://github.com/pytube/pytube/issues/1105#issuecomment-907033591
# i have fixed this in this program by cloning the module from github and correcting inside it


class youtubewebviewclass(object):
    def youtubewebviewwindow(self, Dialog):
        QWebEngineSettings.globalSettings().setAttribute(
            QWebEngineSettings.PluginsEnabled, True
        )
        Dialog.setObjectName("Dialog")
        Dialog.resize(593, 456)
        self.webView = QtWebEngineWidgets.QWebEngineView(Dialog)
        self.webView.setGeometry(QtCore.QRect(0, 0, 591, 451))
        self.webView.setUrl(QtCore.QUrl("https://www.youtube.com/feed/explore"))
        self.webView.setObjectName("webView")
        self.Downloadthisvideobutton = QtWidgets.QPushButton(Dialog)
        self.Downloadthisvideobutton.setGeometry(QtCore.QRect(438, 420, 151, 25))
        self.Downloadthisvideobutton.setObjectName("Downloadthisvideobutton")
        self.Downloadthisvideobutton.clicked.connect(
            self.on_click_downloadthisvideobutton
        )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.Downloadthisvideobutton.setText(
            _translate("Dialog", "Download this video")
        )

    def on_click_downloadthisvideobutton(self, Dialog):

        youtube_video_url = self.webView.url().toString()
        print(youtube_video_url)
        try:

            yt_obj = YouTube(youtube_video_url)

            filters = yt_obj.streams.filter(progressive=True, file_extension="mp4")
            time.sleep(3)
            folderpath_to_save_youtube_video = (
                QtWidgets.QFileDialog.getExistingDirectory(None, "Select Folder")
            )
            time.sleep(3)
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


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = youtubewebviewclass()
    ui.youtubewebviewwindow(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
