from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtCore import QThread, pyqtSignal

from pytube import YouTube
from pytube.helpers import safe_filename
from pytube import exceptions
import sys
import os

ui_form = uic.loadUiType('design.ui')[0]


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


class YouTubeDownloader(QtWidgets.QMainWindow, ui_form):
    def __init__(self, parent=None):
        QtWidgets.QMainWindow.__init__(self, parent)
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

        # https://www.youtube.com/watch?v=Of_ncEWRd2E&ab_channel=The%D0%9B%D1%8E%D0%B4%D0%B8

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
