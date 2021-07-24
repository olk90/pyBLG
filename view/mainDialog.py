from PySide2.QtWidgets import *

from view.barcodeTableWidget import BarcodeTableWidget
from view.ioWidget import IOWidget
from view.settingsWidget import SettingsWidget
from view.translate import translate


class MainDialog(QMainWindow):

    def __init__(self, form):
        super().__init__(parent=form)

        form.setWindowTitle(translate("Title", "pyBLG"))

        self.layout = QVBoxLayout(form)
        self.settingsWidget = SettingsWidget(dialog=self).widget
        self.ioWidget = IOWidget(dialog=self).widget
        self.tableWidget = BarcodeTableWidget(dialog=self).widget

        self.layout.addWidget(self.settingsWidget.frame)
        self.layout.addWidget(self.ioWidget.frame)
        self.layout.addWidget(self.tableWidget.frame)

        form.resize(451, 714)
