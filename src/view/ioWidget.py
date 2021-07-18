from PySide2.QtCore import *
from PySide2.QtWidgets import *

from view.translate import translate


class IOWidget(QWidget):

    def __init__(self, form, font):
        super().__init__(parent=form)

        self.font = font

        self.frame = QFrame(form)

        self.inputFileFrame = QFrame(self.frame)
        self.inputLayout = QHBoxLayout(self.inputFileFrame)
        self.inputPathEdit = QLineEdit(self.inputFileFrame)
        self.inputButton = QToolButton(self.inputFileFrame)
        self.inputFileLabel = QLabel(self.frame)

        self.outputPathFrame = QFrame(self.frame)
        self.outputPathLabel = QLabel(self.frame)
        self.outputButton = QToolButton(self.outputPathFrame)
        self.outputPathEdit = QLineEdit(self.outputPathFrame)
        self.outputLayout = QHBoxLayout(self.outputPathFrame)
        self.ioFormLayout = QFormLayout()
        self.ioLabel = QLabel(self.frame)
        self.ioFrameLayout = QVBoxLayout(self.frame)

        self.setup_ui()

        self.translate_ui()
        QMetaObject.connectSlotsByName(form)

    def setup_ui(self):
        self.ioLabel.setFont(self.font)
        self.ioFrameLayout.addWidget(self.ioLabel)
        self.ioFormLayout.setWidget(0, QFormLayout.LabelRole, self.inputFileLabel)
        self.inputLayout.addWidget(self.inputPathEdit)
        self.inputButton.setText("")
        # self.inputButton.clicked.connect(select_input_file)
        self.inputLayout.addWidget(self.inputButton)

        self.ioFormLayout.setWidget(0, QFormLayout.FieldRole, self.inputFileFrame)
        self.ioFormLayout.setWidget(1, QFormLayout.LabelRole, self.outputPathLabel)

        self.outputLayout.addWidget(self.outputPathEdit)
        self.outputLayout.addWidget(self.outputButton)

        self.ioFormLayout.setWidget(1, QFormLayout.FieldRole, self.outputPathFrame)
        self.ioFrameLayout.addLayout(self.ioFormLayout)

    def translate_ui(self):
        self.ioLabel.setText(translate("Form", "Input/Output"))
        self.inputFileLabel.setText(translate("Form", "Input File"))
        self.outputPathLabel.setText(translate("Form", "Output Path"))
