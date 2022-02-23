from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://google.com"))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)


        back_button = QAction("Back", self)
        back_button.triggered.connect(self.browser.back)
        navbar.addAction(back_button)

        for_button = QAction("Forward", self)
        for_button.triggered.connect(self.browser.forward)
        navbar.addAction(for_button)

        reload_button = QAction("Reload", self)
        reload_button.triggered.connect(self.browser.reload)
        navbar.addAction(reload_button)

        home_button = QAction("Home",self)
        home_button.triggered.connect(self.navigate_home)
        navbar.addAction(home_button)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
    
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        q = q.toString()
        self.url_bar.setText(q)




def main():
    app = QApplication(sys.argv)
    QApplication.setApplicationName("custom web browser")
    windowTest = Window()
    app.exec_()

if __name__ == "__main__":
    main()

