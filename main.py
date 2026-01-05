import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.coffeeTable : QTableWidget
        uic.loadUi("main.ui", self)
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.coffeeTable.setRowCount(len(result))
        for i, row in enumerate(result):
            for item_ind in range(len(row)):
                item = QTableWidgetItem(str(row[item_ind]))
                self.coffeeTable.setItem(i, item_ind, item)
        con.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())