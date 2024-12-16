import sys
import os

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPalette, QBrush, QImage, QIcon

from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    else:
        return os.path.join(os.path.abspath('.'), relative_path)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('John Pork is calling...')
        self.setWindowIcon(QIcon(resource_path('assets/images/icon.png')))

        # Воспроизведение звука
        self.media_player = QMediaPlayer(self)
        url = QUrl.fromLocalFile(resource_path('assets/audios/audio.mp3'))
        content = QMediaContent(url)
        self.media_player.setMedia(content)
        self.media_player.play()

        # Установка фона
        background_image = QImage(resource_path('assets/images/background_image.png'))
        self.setGeometry(100, 100, background_image.width(), background_image.height())
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background_image))
        self.setPalette(palette)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

