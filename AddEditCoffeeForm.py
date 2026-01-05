import sqlite3
from PyQt6.QtWidgets import QMainWindow
from PyQt6 import uic


class AddEditCoffeeForm(QMainWindow):
    def __init__(self, coffee_id=None):
        super().__init__()
        uic.loadUi("addEditCoffeeForm.ui", self)
        self.coffee_id = coffee_id

        if coffee_id is not None:
            self.load_data()

        self.saveButton.clicked.connect(self.save_data)

    def load_data(self):
        con = sqlite3.connect("coffee.db")
        cur = con.cursor()
        data = cur.execute(
            "SELECT name, roast_level, form, taste_desc, price, package_size "
            "FROM coffee WHERE id = ?", (self.coffee_id,)
        ).fetchone()
        con.close()

        self.nameEdit.setText(data[0])
        self.roastEdit.setText(data[1])
        self.formEdit.setText(data[2])
        self.tasteEdit.setText(data[3])
        self.priceEdit.setText(str(data[4]))
        self.packageEdit.setText(data[5])

    def save_data(self):
        data = (
            self.nameEdit.text(),
            self.roastEdit.text(),
            self.formEdit.text(),
            self.tasteEdit.text(),
            float(self.priceEdit.text()),
            self.packageEdit.text()
        )

        con = sqlite3.connect("coffee.db")
        cur = con.cursor()

        if self.coffee_id is None:
            cur.execute(
                "INSERT INTO coffee (name, roast_level, form, taste_desc, price, package_size) "
                "VALUES (?, ?, ?, ?, ?, ?)",
                data
            )
        else:
            cur.execute(
                "UPDATE coffee SET name=?, roast_level=?, form=?, taste_desc=?, price=?, package_size=? "
                "WHERE id=?",
                data + (self.coffee_id,)
            )

        con.commit()
        con.close()
        self.close()
