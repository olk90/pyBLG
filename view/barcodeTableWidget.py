from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

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

        self.widget.eraseButton.clicked.connect(self.clear_table)
        self.update_button_states()

    def clear_table(self):
        table = self.get_table()
        table.setRowCount(0)
        self.update_button_states()

    def update_button_states(self):
        table = self.get_table()
        enable = table.rowCount() > 0
        self.widget.generateButton.setEnabled(enable)
        self.widget.eraseButton.setEnabled(enable)

    def get_table(self):
        return self.widget.table
