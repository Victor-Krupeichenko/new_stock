from PySide2.QtWidgets import QMainWindow, QHeaderView, QDialog, QDialogButtonBox, QApplication, QTableWidgetItem
from database.database_operations import create_item, item_all, search_item, delete_item, update_item
from gui import win_gui, add_form, update_form, delete_dialog

_ROW_ITEMS = list()


class MyDialogDelete(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = delete_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.delete_dialog)

    def delete_dialog(self, button):
        """Диалоговое окно для удаления записи"""
        standard_button = self.sender().standardButton(button)  # Получаем стандартную константу кнопки (Ok или Cancel)
        global _ROW_ITEMS
        if standard_button == QDialogButtonBox.Ok:
            if len(_ROW_ITEMS) > 0:
                delete_item(int(_ROW_ITEMS[-1]))
                _ROW_ITEMS = list()
                self.ui.label_2.setText('')
                self.accept()
        else:  # standard_button == QDialogButtonBox.Cancel:
            self.accept()


class MyDialogUpdate(QDialog):
    def __init__(self):
        super(MyDialogUpdate, self).__init__()
        self.ui = update_form.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.update_item)

    def update_item(self, button):
        """Обновляет запись в таблице"""
        standard_button = self.sender().standardButton(button)  # Получаем стандартную константу кнопки (Ok или Cancel)
        global _ROW_ITEMS
        if standard_button == QDialogButtonBox.Ok:
            title = self.ui.lineEdit_title.text()
            invent = self.ui.lineEdit_invent.text()
            count = self.ui.spinBox.text()
            price = self.ui.doubleSpinBox.value()
            if len(_ROW_ITEMS) > 0:
                update_item(int(_ROW_ITEMS[-1]), title=title, invent=invent, count=count, price=price)
                _ROW_ITEMS = list()
                self.ui.lineEdit_title.setText('')
                self.ui.lineEdit_invent.setText('')
                self.ui.spinBox.setValue(0)
                self.ui.doubleSpinBox.setValue(0.0)
                self.accept()
        else:  # standard_button == QDialogButtonBox.Cancel:
            self.accept()


class MyDialogAdd(QDialog):
    def __init__(self):
        super(MyDialogAdd, self).__init__()
        self.ui = add_form.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.add_item)

    def add_item(self, button):
        """Добавляет запись в таблицу"""
        standard_button = self.sender().standardButton(button)  # Получаем стандартную константу кнопки (Ok или Cancel)
        if standard_button == QDialogButtonBox.Ok:
            title = self.ui.lineEdit_title.text()
            invent = self.ui.lineEdit_invent.text()
            count = int(self.ui.spinBox.text())
            price = self.ui.doubleSpinBox.value()
            if any([title]):
                create_item(title=title, invent=invent, count=count, price=price)
                self.ui.lineEdit_title.setText('')
                self.ui.lineEdit_invent.setText('')
                self.ui.spinBox.setValue(0)
                self.ui.doubleSpinBox.setValue(0.0)
                self.close()
        else:  # standard_button == QDialogButtonBox.Cancel:
            self.accept()


class MyStock(QMainWindow):
    def __init__(self):
        super(MyStock, self).__init__()
        self.ui = win_gui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.dialog_add = MyDialogAdd()
        self.dialog_update = MyDialogUpdate()
        self.dialog_delete = MyDialogDelete()
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.hideColumn(6)
        self.filling_table()
        self.current_dialog = None
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_remove.clicked.connect(self.delete_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_search.clicked.connect(self.search_item)
        self.ui.btn_all.clicked.connect(self.view_all_records)
        self.ui.tableWidget.cellClicked.connect(self.handle_cell_clicked)

    # def button_active_not_active(self, boolean):
    #     """Делает кнопки активными ли не активными"""
    #     self.ui.btn_all.setEnabled(boolean)
    #     self.ui.btn_add.setEnabled(boolean)
    #     self.ui.btn_remove.setEnabled(boolean)
    #     self.ui.btn_update.setEnabled(boolean)

    def handle_cell_clicked(self, row):
        """Получение id выделенной строки в таблице"""
        items = [self.ui.tableWidget.item(row, c).text() for c in range(self.ui.tableWidget.columnCount())]
        global _ROW_ITEMS
        _ROW_ITEMS = items

    def view_all_records(self):
        """Вывод всех записей"""
        self.filling_table()

    def record_output(self, values):
        """Вывод записей"""
        self.ui.tableWidget.setRowCount(len(values))
        for idx, value in enumerate(values):
            self.ui.tableWidget.setItem(idx, 0, QTableWidgetItem(str(value.title)))
            self.ui.tableWidget.setItem(idx, 1, QTableWidgetItem(str(value.date)))
            self.ui.tableWidget.setItem(idx, 2, QTableWidgetItem(str(value.inventary_num)))
            self.ui.tableWidget.setItem(idx, 3, QTableWidgetItem(str(value.count)))
            self.ui.tableWidget.setItem(idx, 4, QTableWidgetItem(str(value.price)))
            self.ui.tableWidget.setItem(idx, 5, QTableWidgetItem(str('на складе')))
            self.ui.tableWidget.setItem(idx, 6, QTableWidgetItem(str(value.id)))

    # def open_dialog_window(self, func):
    #     """Открывает новое диалоговое окно и закрывает старое"""
    #     if self.current_dialog is not None:
    #         self.current_dialog.close()
    #     child_window = func
    #     self.current_dialog = child_window
    #     func.show()

    def filling_table(self):
        """Заполняет таблицу"""
        records = item_all()
        self.record_output(records)

    def search_item(self):
        """Поиск записи в БД"""
        search = self.ui.line_search.text()
        records = search_item(search)
        self.record_output(records)
        self.ui.line_search.setText('')

    def delete_item(self):
        """Вызывает диалоговое окно для удаления записи"""
        if len(_ROW_ITEMS) > 0:
            self.dialog_delete.ui.label_2.setText(_ROW_ITEMS[0])
        self.dialog_delete.exec_()
        self.filling_table()

    def add_item(self):
        """Вызывает диалоговое окно для создания записи"""
        self.dialog_add.exec_()
        self.filling_table()

    def update_item(self):
        """Вызывает диалоговое окно для обновления записи"""
        if len(_ROW_ITEMS) > 0:
            self.dialog_update.ui.lineEdit_title.setText(_ROW_ITEMS[0])
            self.dialog_update.ui.lineEdit_invent.setText(_ROW_ITEMS[2])
            self.dialog_update.ui.spinBox.setValue(int(_ROW_ITEMS[3]))
            self.dialog_update.ui.doubleSpinBox.setValue(float(_ROW_ITEMS[4]))
        self.dialog_update.exec_()
        self.filling_table()

    def closeEvent(self, event):
        """Автоматически закрывает диалоговое окно при выходе из программы"""
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QDialog):
                widget.close()
        event.accept()
