import sys
from PySide2.QtWidgets import QApplication
from app.main import MyStock
from database import create_db
from database.connect_db import engine

if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_db.Base.metadata.create_all(bind=engine)
    main_prog = MyStock()
    main_prog.showMaximized()
    sys.exit(app.exec_())
