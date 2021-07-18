from PySide2.QtCore import *
from PySide2.QtWidgets import *


class BarcodeTableWidget(QWidget):

    def __init__(self, form):
        super().__init__(parent=form)

        self.frame = QFrame(form)
        self.table_frame_layout = QVBoxLayout(self.frame)
        self.table = QTableView(self.frame)
        self.buttonBox = QDialogButtonBox(self.frame)

        self.setup_ui()

    def setup_ui(self):
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.table.sizePolicy().hasHeightForWidth())
        self.table.setSizePolicy(sizePolicy)
        self.table.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.table.setAlternatingRowColors(True)

        self.table_frame_layout.addWidget(self.table)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Reset)
        self.buttonBox.setCenterButtons(False)
        self.table_frame_layout.addWidget(self.buttonBox)