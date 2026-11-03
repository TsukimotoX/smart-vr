import sqlite3
import os

class Database:
    dbPath = "src/app/data/SmartVR.db"

    @staticmethod
    def connect() -> sqlite3.Connection:
        if not os.path.isfile(Database.dbPath):
            raise FileNotFoundError(f"Database not found: {Database.dbPath}")

        connection = sqlite3.connect(Database.dbPath)
        connection.row_factory = sqlite3.Row # позволяет читать по названиям столбцов а не по индексам
        connection.execute("PRAGMA foreign_keys = ON")

        return connection