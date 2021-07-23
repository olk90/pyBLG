from PySide2.QtCore import *
from PySide2.QtWidgets import *


class BarcodeTableWidget(QWidget):

    def __init__(self, form):
        super().__init__(parent=form)

        self.frame = QFrame(form)
        self.table_frame_layout = QVBoxLayout(self.frame)
        self.table = QTableWidget(self.frame)
        self.buttonBox = QDialogButtonBox(self.frame)

        self.setup_ui()

    def setup_ui(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)

        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderItem(0, QTableWidgetItem("Name"))
        self.table.setHorizontalHeaderItem(1, QTableWidgetItem("Barcode"))

        header = self.table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.Stretch)

        self.load_data()

        self.table.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table.setAlternatingRowColors(True)

        self.table_frame_layout.addWidget(self.table)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.table_frame_layout.addWidget(self.buttonBox)

    def load_data(self):
        items = [{"name": "John", "barcode": "100034589012"},
                 {"name": "Mark", "barcode": "100034589034"},
                 {"name": "George", "barcode": "3240589767"}]
        row = 0
        self.table.setRowCount(len(items))
        for item in items:
            self.table.setItem(row, 0, QTableWidgetItem(item["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(item["barcode"]))
            row = row + 1
