from PySide6.QtWidgets import QMainWindow, QStackedWidget, QHBoxLayout, QVBoxLayout, QPushButton, QWidget
from ui.pages.Dashboard import Dashboard
from ui.pages.Devices import Devices
from ui.pages.Setups import Setups
from ui.pages.Calibration import Calibration
from ui.pages.Sessions import Sessions
from ui.pages.Settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("SmartVR")
        self.setFixedSize(1280, 720)

        container = QWidget()
        self.setCentralWidget(container)
        root = QHBoxLayout(container)
        
        sidebar = QVBoxLayout()
        root.addLayout(sidebar)

        self.pages = QStackedWidget()
        root.addWidget(self.pages, 1)

        sections: list[QWidget] = [Dashboard(), Devices(), Setups(), Calibration(), Sessions(), Settings()]

        for index, page in enumerate(sections):
            button = QPushButton(page.objectName())
            size = int(self.size().height()/len(sections))-5
            button.setFixedSize(size, size)
            sidebar.addWidget(button)

            self.pages.addWidget(page)
            button.clicked.connect(lambda _=False, i=index: self.pages.setCurrentIndex(i))

        sidebar.addStretch()