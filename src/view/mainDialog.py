from PySide2.QtGui import *
from PySide2.QtWidgets import *

from view.barcodeTableWidget import BarcodeTableWidget
from view.ioWidget import IOWidget
from view.settingsWidget import SettingsWidget
from view.translate import translate


class MainDialog(QMainWindow):

    def __init__(self, form):
        super().__init__(parent=form)

        form.setWindowTitle(translate("Title", "pyBLG"))

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.layout = QVBoxLayout(form)
        self.settings = SettingsWidget(form=form, font=font)
        self.io = IOWidget(form=form, font=font)
        self.table = BarcodeTableWidget(form=form)

        self.layout.addWidget(self.settings.frame)
        self.layout.addWidget(self.io.frame)
        self.layout.addWidget(self.table.frame)

        form.resize(451, 714)
