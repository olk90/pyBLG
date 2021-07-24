import sys

from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

from logic.csvConverter import load_csv
from view.translate import translate


class IOWidget(QWidget):

    def __init__(self, dialog):
        super().__init__(parent=dialog)

        ui_file_name = "ui_files/io_widget.ui"
        ui_file = QFile(ui_file_name)
        if not ui_file.open(QFile.ReadOnly):
            print("Cannot open {}: {}".format(ui_file_name, ui_file.errorString()))
            sys.exit(-1)

        loader = QUiLoader()
        self.widget = loader.load(ui_file, dialog)
        ui_file.close()

        self.dialog = dialog

        self.setup_ui()
        self.translate_ui()

    def setup_ui(self):
        self.widget.inputPathButton.clicked.connect(self.select_input_file)
        self.widget.outputPathButton.clicked.connect(self.select_output_path)

    def translate_ui(self):
        self.widget.ioLabel.setText(translate("Form", "Input/Output"))
        self.widget.inputPathEdit.setPlaceholderText(translate("Form", "Input File"))
        self.widget.outputPathEdit.setPlaceholderText(translate("Form", "Output Path"))

    def select_input_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self,
                                                   translate("Form", "Open CSV"),
                                                   "",
                                                   translate("Form", "Data files (*.csv)"))
        self.widget.inputPathEdit.setText(file_name)

        table = self.dialog.tableWidget.table
        load_csv(file_name, table)

    def select_output_path(self):
        directory = QFileDialog.getExistingDirectory(self,
                                                     translate("Form", "Select output path"))
        self.widget.outputPathEdit.setText(directory)
