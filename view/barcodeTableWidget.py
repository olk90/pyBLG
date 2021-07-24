import sys

from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *


class BarcodeTableWidget(QWidget):

    def __init__(self, form):
        super().__init__(parent=form)

        ui_file_name = "ui_files/barcode_table_widget.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, form)
        ui_file.close()

        self.setup_ui()

    def setup_ui(self):
        header = self.widget.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.load_data()

    # TODO replace with proper implementation
    def load_data(self):
        items = [{"name": "John", "barcode": "100034589012"},
                 {"name": "Mark", "barcode": "100034589034"},
                 {"name": "George", "barcode": "3240589767"}]
        row = 0
        self.widget.table.setRowCount(len(items))
        for item in items:
            self.widget.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.widget.table.setItem(row, 1, QTableWidgetItem(item["barcode"]))
            row = row + 1
