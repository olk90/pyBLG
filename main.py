import qdarkstyle
import sys
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainDialog(QWidget):

    def __init__(self):
        super().__init__()

        # settings pane
        self.settingsFrame = QFrame(Form)
        self.labelContentFrame = QFrame(self.settingsFrame)
        self.formatComboBox = QComboBox(self.settingsFrame)
        self.formatLabel = QLabel(self.settingsFrame)
        self.outputTypeComboBox = QComboBox(self.settingsFrame)
        self.outputTypeLabel = QLabel(self.settingsFrame)
        self.layoutLabel = QLabel(self.settingsFrame)

        self.settingsFrameLayout = QVBoxLayout(self.settingsFrame)
        self.settingsFormLayout = QFormLayout()

        self.settingsLabel = QLabel(self.settingsFrame)
        self.verticalLayout = QVBoxLayout(Form)
        self.nameCheckBox = QCheckBox(self.labelContentFrame)
        self.barcodeCheckbox = QCheckBox(self.labelContentFrame)
        self.settingsCheckboxLayout = QHBoxLayout(self.labelContentFrame)

        # input/output pane
        self.ioFrame = QFrame(Form)

        self.inputFileFrame = QFrame(self.ioFrame)
        self.inputLayout = QHBoxLayout(self.inputFileFrame)
        self.inputPathEdit = QLineEdit(self.inputFileFrame)
        self.inputButton = QToolButton(self.inputFileFrame)
        self.inputFileLabel = QLabel(self.ioFrame)

        self.outputPathFrame = QFrame(self.ioFrame)
        self.outputPathLabel = QLabel(self.ioFrame)
        self.outputButton = QToolButton(self.outputPathFrame)
        self.outputPathEdit = QLineEdit(self.outputPathFrame)
        self.outputLayout = QHBoxLayout(self.outputPathFrame)
        self.ioFormLayout = QFormLayout()
        self.ioLabel = QLabel(self.ioFrame)
        self.ioFrameLayout = QVBoxLayout(self.ioFrame)

        # table pane
        self.tableFrame = QFrame(Form)
        self.table_frame_layout = QVBoxLayout(self.tableFrame)
        self.table = QTableView(self.tableFrame)
        self.buttonBox = QDialogButtonBox(self.tableFrame)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(451, 714)

        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.configure_settings(font)
        self.configure_io(font)
        self.configure_table()

        self.translate_ui(form)
        QMetaObject.connectSlotsByName(form)

    @staticmethod
    def configure_frame(frame):
        frame.setFrameShape(QFrame.StyledPanel)
        frame.setFrameShadow(QFrame.Raised)

    def configure_settings(self, font):
        self.configure_frame(self.settingsFrame)
        self.verticalLayout.addWidget(self.settingsFrame)

        self.configure_format_cb()
        self.configure_output_cb()

        self.settingsLabel.setFont(font)
        self.settingsFrameLayout.addWidget(self.settingsLabel)
        self.settingsFormLayout.setWidget(0, QFormLayout.LabelRole, self.layoutLabel)
        self.settingsFormLayout.setWidget(0, QFormLayout.FieldRole, self.labelContentFrame)
        self.settingsFormLayout.setWidget(1, QFormLayout.LabelRole, self.outputTypeLabel)
        self.settingsFormLayout.setWidget(1, QFormLayout.FieldRole, self.outputTypeComboBox)
        self.settingsFormLayout.setWidget(2, QFormLayout.LabelRole, self.formatLabel)
        self.settingsFormLayout.setWidget(2, QFormLayout.FieldRole, self.formatComboBox)
        self.settingsCheckboxLayout.addWidget(self.barcodeCheckbox)
        self.settingsCheckboxLayout.addWidget(self.nameCheckBox)
        self.settingsFrameLayout.addLayout(self.settingsFormLayout)

    def configure_io(self, font):
        self.configure_frame(self.ioFrame)
        self.verticalLayout.addWidget(self.ioFrame)

        self.ioLabel.setFont(font)
        self.ioFrameLayout.addWidget(self.ioLabel)
        self.ioFormLayout.setWidget(0, QFormLayout.LabelRole, self.inputFileLabel)
        self.inputLayout.addWidget(self.inputPathEdit)
        self.inputButton.setText("")
        self.inputLayout.addWidget(self.inputButton)

        self.ioFormLayout.setWidget(0, QFormLayout.FieldRole, self.inputFileFrame)
        self.ioFormLayout.setWidget(1, QFormLayout.LabelRole, self.outputPathLabel)

        self.outputLayout.addWidget(self.outputPathEdit)
        self.outputLayout.addWidget(self.outputButton)

        self.ioFormLayout.setWidget(1, QFormLayout.FieldRole, self.outputPathFrame)
        self.ioFrameLayout.addLayout(self.ioFormLayout)

    def configure_table(self):
        self.configure_frame(self.tableFrame)
        self.verticalLayout.addWidget(self.tableFrame)

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

    def configure_format_cb(self):
        self.formatComboBox.addItem("Code 128")
        self.formatComboBox.addItem("EAN 128")

    def configure_output_cb(self):
        self.outputTypeComboBox.addItem("*.png")
        self.outputTypeComboBox.addItem("*.odt")
        self.outputTypeComboBox.addItem("*.docx")

    def translate_ui(self, form):
        form.setWindowTitle(translate("Form", "Form"))
        self.settingsLabel.setText(translate("Form", "Settings"))
        self.layoutLabel.setText(translate("Form", "Layout"))
        self.outputTypeLabel.setText(translate("Form", "Output Type"))
        self.formatLabel.setText(translate("Form", "Format"))
        self.barcodeCheckbox.setText(translate("Form", "Print Barcode"))
        self.nameCheckBox.setText(translate("Form", "Print Name"))
        self.ioLabel.setText(translate("Form", "Input/Output"))
        self.inputFileLabel.setText(translate("Form", "Input File"))
        self.outputPathLabel.setText(translate("Form", "Output Path"))


def translate(context, text):
    return QCoreApplication.translate(context, text, None)


def style_sheet(__app):
    dark_stylesheet = qdarkstyle.load_stylesheet_pyqt5()
    __app.setStyleSheet(dark_stylesheet)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    style_sheet(app)
    Form = QWidget()
    dialog = MainDialog()
    dialog.setup_ui(Form)
    Form.show()
    sys.exit(app.exec_())
