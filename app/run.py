import sys
from PySide2.QtWidgets import QApplication
from app.main import MyStock
from database import create_db, connect_db

if __name__ == '__main__':
    app = QApplication(sys.argv)
    create_db.Base.metadata.create_all(bind=connect_db.engine)
    main_prog = MyStock()
    main_prog.showMaximized()
    sys.exit(app.exec_())
