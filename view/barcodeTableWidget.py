from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

from logic.barcodes import barcodeProperties, create_label
from view.uiHelpers import load_ui_file


class BarcodeTableWidget(QWidget):

    def __init__(self, dialog):
        super().__init__(parent=dialog)

        ui_file_name = "ui_files/barcode_table_widget.ui"
        ui_file = load_ui_file(ui_file_name)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, dialog)
        ui_file.close()

        self.setup_ui()

    def setup_ui(self):
        header = self.widget.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.widget.generateButton.clicked.connect(self.generate_labels)

        self.widget.eraseButton.clicked.connect(self.clear_table)
        self.update_button_states()

    def clear_table(self):
        table = self.get_table()
        table.setRowCount(0)
        self.update_button_states()

    def generate_labels(self):
        table = self.get_table()
        rows = table.rowCount()
        for row in range(0, rows):
            name = table.item(row, 0).text()
            barcode = table.item(row, 1).text()
            create_label(name, barcode)

    def update_button_states(self):
        table = self.get_table()
        table_not_empty = table.rowCount() > 0
        output_path_set = len(barcodeProperties.output_path) > 0
        self.widget.generateButton.setEnabled(table_not_empty and output_path_set)
        self.widget.eraseButton.setEnabled(table_not_empty)

    def get_table(self):
        return self.widget.table
