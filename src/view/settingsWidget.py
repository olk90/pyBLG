from PySide2.QtCore import *
from PySide2.QtWidgets import *

from view.translate import translate


class SettingsWidget(QWidget):

    def __init__(self, form, font):
        super().__init__(parent=form)

        self.font = font

        self.frame = QFrame(form)
        self.labelContentFrame = QFrame(self.frame)
        self.formatComboBox = QComboBox(self.frame)
        self.formatLabel = QLabel(self.frame)
        self.outputTypeComboBox = QComboBox(self.frame)
        self.outputTypeLabel = QLabel(self.frame)
        self.layoutLabel = QLabel(self.frame)

        self.settingsFrameLayout = QVBoxLayout(self.frame)
        self.settingsFormLayout = QFormLayout(parent=None)

        self.settingsLabel = QLabel(self.frame)
        self.nameCheckbox = QCheckBox(self.labelContentFrame)
        self.barcodeCheckbox = QCheckBox(self.labelContentFrame)
        self.settingsCheckboxLayout = QHBoxLayout(self.labelContentFrame)

        self.setup_ui()

        self.translate_ui()

        QMetaObject.connectSlotsByName(form)

    def setup_ui(self):

        self.configure_format_cb()
        self.configure_output_cb()

        self.settingsLabel.setFont(self.font)
        self.settingsFrameLayout.addWidget(self.settingsLabel)
        self.settingsFormLayout.setWidget(0, QFormLayout.LabelRole, self.layoutLabel)
        self.settingsFormLayout.setWidget(0, QFormLayout.FieldRole, self.labelContentFrame)
        self.settingsFormLayout.setWidget(1, QFormLayout.LabelRole, self.outputTypeLabel)
        self.settingsFormLayout.setWidget(1, QFormLayout.FieldRole, self.outputTypeComboBox)
        self.settingsFormLayout.setWidget(2, QFormLayout.LabelRole, self.formatLabel)
        self.settingsFormLayout.setWidget(2, QFormLayout.FieldRole, self.formatComboBox)
        self.settingsCheckboxLayout.addWidget(self.barcodeCheckbox)
        self.settingsCheckboxLayout.addWidget(self.nameCheckbox)
        self.settingsFrameLayout.addLayout(self.settingsFormLayout)

    def configure_format_cb(self):
        self.formatComboBox.addItem("Code 128")
        self.formatComboBox.addItem("EAN 128")

    def configure_output_cb(self):
        self.outputTypeComboBox.addItem("*.png")
        self.outputTypeComboBox.addItem("*.odt")
        self.outputTypeComboBox.addItem("*.docx")

    def translate_ui(self):
        self.settingsLabel.setText(translate("Form", "Settings"))
        self.layoutLabel.setText(translate("Form", "Layout"))
        self.outputTypeLabel.setText(translate("Form", "Output Type"))
        self.formatLabel.setText(translate("Form", "Format"))
        self.barcodeCheckbox.setText(translate("Form", "Print Barcode"))
        self.nameCheckbox.setText(translate("Form", "Print Name"))
