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

        # Воспроизведение звука с повторением
        self.media_player = QMediaPlayer(self)
        url = QUrl.fromLocalFile(resource_path('assets/audios/audio.mp3'))
        content = QMediaContent(url)
        self.media_player.setMedia(content)
        self.media_player.mediaStatusChanged.connect(self.handleMediaStatusChanged)

        # Установка фона
        background_image = QImage(resource_path('assets/images/background_image.png'))
        
        # Установка размера окна
        screen_geometry = QApplication.desktop().screenGeometry()
        new_width = int(background_image.width() // 1.5)
        new_height = int(background_image.height() // 1.5)

        self.setFixedSize(new_width, new_height)
        x = (screen_geometry.width() - new_width) // 2
        y = (screen_geometry.height() - new_height) // 2
        
        self.setGeometry(x, y, new_width, new_height)
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(background_image.scaled(new_width, new_height)))
        self.setPalette(palette)

    def handleMediaStatusChanged(self, status):
        if status == QMediaPlayer.EndOfMedia:
            self.media_player.setPosition(0)
            self.media_player.play()
        self.media_player.play()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
