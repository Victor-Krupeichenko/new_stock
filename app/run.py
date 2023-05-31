import sys
from PySide2.QtWidgets import QApplication
from app.main import MyStock

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_prog = MyStock()
    main_prog.showMaximized()
    sys.exit(app.exec_())
