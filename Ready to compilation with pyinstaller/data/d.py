import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread

from pytube import YouTube
from pytube import exceptions
from pytube.helpers import safe_filename


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Simple YouTube Downloader by Leus")
        MainWindow.resize(760, 300)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(760, 300))
        MainWindow.setMaximumSize(QtCore.QSize(760, 300))
        MainWindow.setStyleSheet("background-color: #3F3F3F;\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("QPushButton {\n"
                                         "    background-color: #EB2C1E;\n"
                                         "    color: white;\n"
                                         "    border-radius: 10px;\n"
                                         "    font-family: \"Segoe UI Semibold\";\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "#DloadBtn:hover {\n"
                                         "    background-color: #981C14;\n"
                                         "    border-color: #57100B;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "QLineEdit{\n"
                                         "    background-color: white;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 5px;\n"
                                         "    border-color: #C6C6C6;\n"
                                         "    font-family: \"Segoe UI Semibold\";\n"
                                         "    color: #1B1B1B;\n"
                                         "\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar {\n"
                                         "    border: 5px solid #2C954F;\n"
                                         "    border-radius: 10px;\n"
                                         "    background-color: white;\n"
                                         "}\n"
                                         "\n"
                                         "QProgressBar::chunk {\n"
                                         "    background-color: #50C878;\n"
                                         "    border-radius: 4px;\n"
                                         "}\n"
                                         "\n"
                                         "#Path {\n"
                                         "    background-color: #F4CA16;\n"
                                         "    font-family: \"Segoe UI Semibold\";\n"
                                         "    font-size: 18px;\n"
                                         "    border-radius: 10px;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 5px;\n"
                                         "    border-color: #D4AD00;\n"
                                         "}\n"
                                         "\n"
                                         "#Path:hover{\n"
                                         "    background-color: #F07555;\n"
                                         "    border-color: #BB3716;\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "#pathLabel {\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 1px;\n"
                                         "    border-color: silver;\n"
                                         "    color: white;\n"
                                         "    font-family: \"Segoe UI Semibold\";\n"
                                         "}\n"
                                         "\n"
                                         "#labelTitle {\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 1px;\n"
                                         "    border-color: silver;\n"
                                         "    color: white;\n"
                                         "    font-family: \"Segoe UI Semibold\";\n"
                                         "}\n"
                                         "\n"
                                         "#labelQuality {\n"
                                         "    color: white;\n"
                                         "    font-family: \"Segoe UI Semibold\"\n"
                                         "}\n"
                                         "\n"
                                         "\n"
                                         "#ChoiseQ {\n"
                                         "    color: black;\n"
                                         "    background-color: white;\n"
                                         "    border-radius: 5px;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 3px;\n"
                                         "    border-color: silver;\n"
                                         "}\n"
                                         "\n"
                                         "#OnlyAudio {\n"
                                         "    color: white;\n"
                                         "    font-family: \"Segoe UI Semibold\"\n"
                                         "}\n"
                                         "\n"
                                         "#OnlyAudioChoice {\n"
                                         "    color: black;\n"
                                         "    background-color: white;\n"
                                         "    border-radius: 5px;\n"
                                         "    border-style: solid;\n"
                                         "    border-width: 3px;\n"
                                         "    border-color: silver;\n"
                                         "}\n""")
        self.centralwidget.setObjectName("centralwidget")
        self.LinkLine = QtWidgets.QLineEdit(self.centralwidget)
        self.LinkLine.setGeometry(QtCore.QRect(10, 10, 741, 51))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.LinkLine.setFont(font)
        self.LinkLine.setStyleSheet("")
        self.LinkLine.setText("")
        self.LinkLine.setObjectName("LinkLine")
        self.Progress = QtWidgets.QProgressBar(self.centralwidget)
        self.Progress.setGeometry(QtCore.QRect(10, 190, 741, 31))
        self.Progress.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.Progress.setStyleSheet("")
        self.Progress.setProperty("value", 100)
        self.Progress.setTextVisible(False)
        self.Progress.setOrientation(QtCore.Qt.Horizontal)
        self.Progress.setInvertedAppearance(False)
        self.Progress.setTextDirection(QtWidgets.QProgressBar.TopToBottom)
        self.Progress.setFormat("%p%")
        self.Progress.setObjectName("Progress")
        self.DloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.DloadBtn.setGeometry(QtCore.QRect(10, 230, 741, 61))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.DloadBtn.setFont(font)
        self.DloadBtn.setObjectName("DloadBtn")
        self.Path = QtWidgets.QPushButton(self.centralwidget)
        self.Path.setGeometry(QtCore.QRect(250, 150, 501, 31))
        self.Path.setObjectName("Path")
        self.pathLabel = QtWidgets.QLabel(self.centralwidget)
        self.pathLabel.setGeometry(QtCore.QRect(250, 110, 501, 31))
        self.pathLabel.setText("")
        self.pathLabel.setObjectName("pathLabel")
        self.ChoiseQ = QtWidgets.QComboBox(self.centralwidget)
        self.ChoiseQ.setGeometry(QtCore.QRect(120, 150, 121, 31))
        self.ChoiseQ.setObjectName("ChoiseQ")
        self.ChoiseQ.addItem("")
        self.ChoiseQ.addItem("")
        self.labelTitle = QtWidgets.QLabel(self.centralwidget)
        self.labelTitle.setGeometry(QtCore.QRect(10, 70, 741, 31))
        self.labelTitle.setText("")
        self.labelTitle.setObjectName("labelTitle")
        self.labelQuality = QtWidgets.QLabel(self.centralwidget)
        self.labelQuality.setGeometry(QtCore.QRect(10, 150, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.labelQuality.setFont(font)
        self.labelQuality.setObjectName("labelQuality")
        self.OnlyAudio = QtWidgets.QLabel(self.centralwidget)
        self.OnlyAudio.setGeometry(QtCore.QRect(10, 110, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Semibold")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.OnlyAudio.setFont(font)
        self.OnlyAudio.setObjectName("OnlyAudio")
        self.OnlyAudioChoice = QtWidgets.QComboBox(self.centralwidget)
        self.OnlyAudioChoice.setGeometry(QtCore.QRect(120, 110, 121, 31))
        self.OnlyAudioChoice.setObjectName("OnlyAudioChoice")
        self.OnlyAudioChoice.addItem("")
        self.OnlyAudioChoice.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Simple YouTube Downloader by Leus", "Simple YouTube Downloader by Leus"))
        self.DloadBtn.setText(_translate("MainWindow", "Download"))
        self.Path.setText(_translate("MainWindow", "Path"))
        self.ChoiseQ.setItemText(0, _translate("MainWindow", "High"))
        self.ChoiseQ.setItemText(1, _translate("MainWindow", "Low"))
        self.labelQuality.setText(_translate("MainWindow", "Quality:"))
        self.OnlyAudio.setText(_translate("MainWindow", "Only audio:"))
        self.OnlyAudioChoice.setItemText(0, _translate("MainWindow", "Audio and video"))
        self.OnlyAudioChoice.setItemText(1, _translate("MainWindow", "Only audio"))


class Download(QThread):
    dataChanged = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal(str)

    def __init__(self, video, path=None):
        super().__init__()
        self.working = True
        self.video = video
        self.path = path

    def run(self):
        self.dataChanged.emit("Start downloading")
        while True:
            self.video.download(self.path)
            break
        print("Загрузка завершена")
        self.finished.emit('Downloading complete')

    def stopped(self):
        return self.working


class StatusBar(QThread):
    dataChanged = QtCore.pyqtSignal(str)
    finished = QtCore.pyqtSignal(str)

    def __init__(self, path, file_name, s_bar, video, activate_btns_func):
        QThread.__init__(self)
        # Флаг инициализации
        self.working = True
        self.path = path
        self.fileName = file_name
        self.status_bar = s_bar
        self.video = video

        self.activate_btns = activate_btns_func

    def run(self):
        total_size = self.video.filesize
        print(total_size)

        print(self.path)
        print(self.fileName)
        path_to_file = self.path + '/' + self.fileName + '.mp4'

        while True:
            # Расчет текущего количества данных
            try:
                current_size = os.path.getsize(path_to_file)
            except BaseException:
                continue

            percent = (float(current_size) / float(total_size)) * float(100)
            self.status_bar.setValue(int(percent))
            if percent >= 100:
                print('Востанавливаем')
                self.activate_btns(activate=True)
                break

    def stopped(self):
        return self.working


class YouTubeDownloader(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.pathLabel.setText(os.getcwd())

        self.Path.clicked.connect(self.set_dir)
        self.DloadBtn.clicked.connect(self.start_downloading_btn)

        self.downloader = None
        self.status_bar = None

    def set_dir(self):
        """Указываем путь для сохранения файла"""
        path = QtWidgets.QFileDialog.getExistingDirectory(self, directory='.')
        self.pathLabel.setText(path)

    def start_downloading_btn(self):
        link = self.LinkLine.text()
        quality = [1 if self.ChoiseQ.currentText() == 'High' else -1][0]
        path = [self.pathLabel.text() if self.pathLabel.text() else os.path.curdir][0]

        try:
            video = YouTube(url=link)
        except exceptions.PytubeError:
            return

        filename = safe_filename(video.title)

        video.streams.get_audio_only(subtype='mp4')
        if self.OnlyAudioChoice.currentText() == "Audio and video":
            if quality > 0:
                video = video.streams.get_highest_resolution()
            else:
                video = video.streams.get_lowest_resolution()
        else:
            video = video.streams.get_audio_only(subtype='mp4')

        self.labelTitle.setText(video.title)

        self.downloader = Download(video=video, path=path)
        self.downloader.working = True
        self.downloader.start()

        self.activate_btns(activate=False)
        self.status_bar = StatusBar(path=path,
                                    file_name=filename,
                                    s_bar=self.Progress,
                                    video=video,
                                    activate_btns_func=self.activate_btns)
        self.status_bar.working = True
        self.status_bar.start()

    def activate_btns(self, activate=True):
        link_line = self.LinkLine
        quality = self.ChoiseQ
        path = self.Path
        download_btn = self.DloadBtn
        only_audio_btn = self.OnlyAudioChoice

        if not activate:
            link_line.setEnabled(False)
            quality.setEnabled(False)
            path.setEnabled(False)
            only_audio_btn.setEnabled(False)
            download_btn.setStyleSheet(
                """
                background-color: #57100B;
                """
            )
            download_btn.setText('In process...')
            return
        link_line.setEnabled(True)
        quality.setEnabled(True)
        path.setEnabled(True)
        only_audio_btn.setEnabled(True)
        download_btn.setStyleSheet(
            """
            background-color: #EB2C1E
            """
        )
        download_btn.setText('Download')


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = YouTubeDownloader()
    window.show()  # Show the window
    app.exec_()  # Start application


if __name__ == '__main__':
    main()
