from PySide2.QtCore import QCoreApplication


def translate(context, text):
    return QCoreApplication.translate(context, text, None)
