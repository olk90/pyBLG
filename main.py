from PyQt5 import QtCore, QtGui, QtWidgets


class MainDialog(object):

    def __init__(self):
        # settings pane
        self.settingsFrame = QtWidgets.QFrame(Form)
        self.labelContentFrame = QtWidgets.QFrame(self.settingsFrame)
        self.formatComboBox = QtWidgets.QComboBox(self.settingsFrame)
        self.formatLabel = QtWidgets.QLabel(self.settingsFrame)
        self.outputTypeComboBox = QtWidgets.QComboBox(self.settingsFrame)
        self.outputTypeLabel = QtWidgets.QLabel(self.settingsFrame)
        self.layoutLabel = QtWidgets.QLabel(self.settingsFrame)

        self.settingsFrameLayout = QtWidgets.QVBoxLayout(self.settingsFrame)
        self.settingsFormLayout = QtWidgets.QFormLayout()

        self.settingsLabel = QtWidgets.QLabel(self.settingsFrame)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.nameCheckBox = QtWidgets.QCheckBox(self.labelContentFrame)
        self.barcodeCheckbox = QtWidgets.QCheckBox(self.labelContentFrame)
        self.settingsCheckboxLayout = QtWidgets.QHBoxLayout(self.labelContentFrame)

        # input/output pane
        self.ioFrame = QtWidgets.QFrame(Form)

        self.inputFileFrame = QtWidgets.QFrame(self.ioFrame)
        self.inputLayout = QtWidgets.QHBoxLayout(self.inputFileFrame)
        self.inputPathEdit = QtWidgets.QLineEdit(self.inputFileFrame)
        self.inputButton = QtWidgets.QToolButton(self.inputFileFrame)
        self.inputFileLabel = QtWidgets.QLabel(self.ioFrame)

        self.outputPathFrame = QtWidgets.QFrame(self.ioFrame)
        self.outputPathLabel = QtWidgets.QLabel(self.ioFrame)
        self.outputButton = QtWidgets.QToolButton(self.outputPathFrame)
        self.outputPathEdit = QtWidgets.QLineEdit(self.outputPathFrame)
        self.outputLayout = QtWidgets.QHBoxLayout(self.outputPathFrame)
        self.ioFormLayout = QtWidgets.QFormLayout()
        self.ioLabel = QtWidgets.QLabel(self.ioFrame)
        self.ioFrameLayout = QtWidgets.QVBoxLayout(self.ioFrame)

        # table pane
        self.tableFrame = QtWidgets.QFrame(Form)
        self.table_frame_layout = QtWidgets.QVBoxLayout(self.tableFrame)
        self.tableView = QtWidgets.QTableView(self.tableFrame)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tableFrame)

    def setup_ui(self, form):
        form.setObjectName("Form")
        form.resize(451, 714)

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)

        self.configure_settings(font)
        self.configure_io(font)
        self.configure_table(font)

        self.translate_ui(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    @staticmethod
    def configure_frame(frame):
        frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        frame.setFrameShadow(QtWidgets.QFrame.Raised)

    def configure_settings(self, font):
        self.configure_frame(self.settingsFrame)
        self.verticalLayout.addWidget(self.settingsFrame)

        self.configure_format_cb()
        self.configure_output_cb()

        self.settingsLabel.setFont(font)
        self.settingsFrameLayout.addWidget(self.settingsLabel)
        self.settingsFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.layoutLabel)
        self.settingsFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.labelContentFrame)
        self.settingsFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.outputTypeLabel)
        self.settingsFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.outputTypeComboBox)
        self.settingsFormLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.formatLabel)
        self.settingsFormLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.formatComboBox)
        self.settingsCheckboxLayout.addWidget(self.barcodeCheckbox)
        self.settingsCheckboxLayout.addWidget(self.nameCheckBox)
        self.settingsFrameLayout.addLayout(self.settingsFormLayout)

    def configure_io(self, font):
        self.configure_frame(self.ioFrame)
        self.verticalLayout.addWidget(self.ioFrame)

        self.ioLabel.setFont(font)
        self.ioFrameLayout.addWidget(self.ioLabel)
        self.ioFormLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.inputFileLabel)
        self.inputLayout.addWidget(self.inputPathEdit)
        self.inputButton.setText("")
        self.inputLayout.addWidget(self.inputButton)

        self.ioFormLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.inputFileFrame)
        self.ioFormLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.outputPathLabel)

        self.outputLayout.addWidget(self.outputPathEdit)
        self.outputLayout.addWidget(self.outputButton)

        self.ioFormLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.outputPathFrame)
        self.ioFrameLayout.addLayout(self.ioFormLayout)

    def configure_table(self, font):
        self.configure_frame(self.tableFrame)
        self.verticalLayout.addWidget(self.tableFrame)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        ## self.tableView.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.tableView.setAlternatingRowColors(True)
        self.table_frame_layout.addWidget(self.tableView)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Reset)
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
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("Form", "Form"))
        self.settingsLabel.setText(_translate("Form", "Settings"))
        self.layoutLabel.setText(_translate("Form", "Layout"))
        self.outputTypeLabel.setText(_translate("Form", "Output Type"))
        self.formatLabel.setText(_translate("Form", "Format"))
        self.barcodeCheckbox.setText(_translate("Form", "Print Barcode"))
        self.nameCheckBox.setText(_translate("Form", "Print Name"))
        self.ioLabel.setText(_translate("Form", "Input/Output"))
        self.inputFileLabel.setText(_translate("Form", "Input File"))
        self.outputPathLabel.setText(_translate("Form", "Output Path"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    dialog = MainDialog()
    dialog.setup_ui(Form)
    Form.show()
    sys.exit(app.exec())
