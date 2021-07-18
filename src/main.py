import sys

from PySide2.QtWidgets import *

from view.mainDialog import MainDialog

if __name__ == "__main__":
    app = QApplication()
    form = QWidget(None)
    MainDialog(form)
    form.show()
    sys.exit(app.exec_())
