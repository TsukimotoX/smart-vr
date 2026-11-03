from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QStackedWidget

class Sessions(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Sessions")

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self.objectName()))
        layout.addStretch()