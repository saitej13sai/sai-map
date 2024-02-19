import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView

class HazardMapApp(QMainWindow):
    def __init__(self, html_path):
        super().__init__()

        self.setWindowTitle("Hazard Map")
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.webview = QWebEngineView()
        with open(html_path, 'r') as file:
            html_content = file.read()
            self.webview.setHtml(html_content)
        layout.addWidget(self.webview)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = HazardMapApp("C:\\Users\\saite\\Downloads\\text-to-html-converter.txt")
    window.show()
    sys.exit(app.exec_())
