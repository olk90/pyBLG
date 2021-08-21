from PySide2.QtWidgets import *

from view.barcodeTableWidget import BarcodeTableWidget
from view.ioWidget import IOWidget
from view.settingsWidget import SettingsWidget
from view.uiHelpers import translate


class MainDialog(QMainWindow):

    def __init__(self, form):
        super().__init__(parent=form)

        form.setWindowTitle(translate("Title", "pyBLG"))

        self.layout = QVBoxLayout(form)
        self.settingsWidget = SettingsWidget(dialog=self).widget
        self.ioWidget = IOWidget(dialog=self).widget
        self.barcodeTableWidget = BarcodeTableWidget(dialog=self)
        self.tableWidget = self.barcodeTableWidget.widget

        self.layout.addWidget(self.settingsWidget)
        self.layout.addWidget(self.ioWidget)
        self.layout.addWidget(self.tableWidget)

        form.resize(451, 714)
