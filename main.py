import sys

import qdarkstyle
from PySide2.QtWidgets import *
from qdarkstyle import LightPalette

from view.mainDialog import MainDialog


def style_sheet(__app):
    dark_stylesheet = qdarkstyle.load_stylesheet(palette=LightPalette())
    __app.setStyleSheet(dark_stylesheet)


if __name__ == "__main__":
    app = QApplication()
    style_sheet(app)
    form = QWidget(None)
    dialog = MainDialog(form)
    dialog.setup_ui(form)
    form.show()
    sys.exit(app.exec_())
