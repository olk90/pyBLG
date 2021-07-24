import sys

from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

from view.translate import translate


class SettingsWidget(QWidget):

    def __init__(self, dialog):
        super().__init__(parent=dialog)

        ui_file_name = "ui_files/settings_widget.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, dialog)
        ui_file.close()

        self.translate_ui()

    def translate_ui(self):
        self.widget.settingsLabel.setText(translate("Form", "Settings"))
        self.widget.layoutLabel.setText(translate("Form", "Layout"))
        self.widget.outputTypeLabel.setText(translate("Form", "Output Type"))
        self.widget.formatLabel.setText(translate("Form", "Format"))
        self.widget.barcodeCheckbox.setText(translate("Form", "Print Barcode"))
        self.widget.nameCheckbox.setText(translate("Form", "Print Name"))
