from PyQt5 import QtCore, QtGui, QtWidgets
import moviepy.editor
import time
import os
import platform
import subprocess
from playsound import playsound


class convertorwindowclass(object):
    def covertorwindow(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(386, 296)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 10, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Rockwell")
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 60, 351, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.on_click_convertButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", " Video To Audio Converter"))
        self.label.setText(_translate("Dialog", "CONVERTER"))
        self.pushButton.setText(_translate("Dialog", "Open File"))

    def on_click_convertButton(self):
        videopath = QtWidgets.QFileDialog.getOpenFileName(
            None, "Select Video to convert"
        )
        videopath = videopath[0]
        video = moviepy.editor.VideoFileClip(videopath)
        audio = video.audio
        time.sleep(3)
        folderpath_to_save_converted_audio = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Select Folder to save audio"
        )
        print(folderpath_to_save_converted_audio)

        audio.write_audiofile(
            folderpath_to_save_converted_audio + "/convertedaudio.mp3"
        )

        path = folderpath_to_save_converted_audio
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
    ui = convertorwindowclass()
    ui.covertorwindow(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
