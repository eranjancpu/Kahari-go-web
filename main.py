import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://www.google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        self.addToolBar(navbar)
        self.setWindowIcon(QIcon('image.png'))

        back_btn = QAction('<=', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        forward_btn = QAction('=>', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)
        reload_btn = QAction('reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)


APP = QApplication(sys.argv)
QApplication.setApplicationName('Kahari Go Web 0.5')
window = MainWindow()
APP.exec_()
