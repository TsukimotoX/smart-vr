import sqlite3
from contextlib import closing
from data.database import Database

class DeviceRepository:
    def getAll(self) -> list[sqlite3.Row]:
        with closing(Database.connect()) as connection:
            return connection.execute("""SELECT id, name, type, hardware_uid, model, firmware_version FROM Device ORDER BY id""").fetchall()
