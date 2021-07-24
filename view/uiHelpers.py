import sys

from PySide2.QtCore import QCoreApplication, QFile


def load_ui_file(filename):
    ui_file = QFile(filename)
    if not ui_file.open(QFile.ReadOnly):
        print("Cannot open {}: {}".format(filename, ui_file.errorString()))
        sys.exit(-1)
    return ui_file


def translate(context, text):
    return QCoreApplication.translate(context, text, None)
