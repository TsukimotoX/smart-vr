from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QTableWidget, QPushButton, QTableWidgetItem
from data.repos.DevicesRepo import DeviceRepository

class Devices(QWidget):
    def __init__(self):
        super().__init__()

        self.setObjectName("Devices")
        self.repository = DeviceRepository()

        layout = QVBoxLayout(self)
        layout.addWidget(QLabel(self.objectName()))

        self.table = QTableWidget(0, 3)
        self.table.setHorizontalHeaderLabels(["Название", "Тип", "UID"])
        layout.addWidget(self.table)

        button = QPushButton("Обновить")
        button.clicked.connect(self.loadDevices)
        layout.addWidget(button)

        self.loadDevices()

    def loadDevices(self):
        devices = self.repository.getAll()
        self.table.setRowCount(len(devices))

        for row, device in enumerate(devices):
            for column, field in enumerate(["id", "name", "type", "hardware_uid", "model", "firmware_version"]):
                value = device[field]
                self.table.setItem(row, column, QTableWidgetItem(str(value) if value is not None else "—"))