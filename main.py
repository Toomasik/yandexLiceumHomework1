import sqlite3
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from AddEditCoffeeForm import AddEditCoffeeForm
from main_ui import Ui_MainWindow
from resource import DB_PATH


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.load_data()

        self.addButton.clicked.connect(self.add_coffee)
        self.editButton.clicked.connect(self.edit_coffee)

    def load_data(self):
        con = sqlite3.connect(DB_PATH)
        cur = con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        con.close()

        self.coffeeTable.setRowCount(len(result))
        for i, row in enumerate(result):
            for j, item in enumerate(row):
                self.coffeeTable.setItem(i, j, QTableWidgetItem(str(item)))

    def add_coffee(self):
        self.form = AddEditCoffeeForm()
        self.form.closeEvent = lambda event: self.load_data()
        self.form.show()


    def edit_coffee(self):
        row = self.coffeeTable.currentRow()
        if row == -1:
            return

        coffee_id = int(self.coffeeTable.item(row, 0).text())
        self.form = AddEditCoffeeForm(coffee_id)
        self.form.show()
        self.form.destroyed.connect(self.load_data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
