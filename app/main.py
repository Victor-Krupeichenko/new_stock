from PySide2.QtWidgets import QMainWindow, QHeaderView, QDialog, QDialogButtonBox, QApplication
from gui import win_gui, add_form, update_form, delete_dialog


class MyDialogDelete(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = delete_dialog.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.delete_dialog)

    def delete_dialog(self, button):
        """Диалоговое окно для удаления записи"""
        standard_button = self.sender().standardButton(button)  # Получаем стандартную константу кнопки (Ok или Cancel)
        print('Получение записи из БД')
        if standard_button == QDialogButtonBox.Ok:
            print('ok')
            self.accept()
        else:  # standard_button == QDialogButtonBox.Cancel:
            print("Cancel button was clicked")
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
        print("Получение записи из БД")
        if standard_button == QDialogButtonBox.Ok:
            print('ok')
            self.accept()
        else:  # standard_button == QDialogButtonBox.Cancel:
            print("Cancel button was clicked")
            self.accept()


class MyDialogAdd(QDialog):
    def __init__(self):
        super(MyDialogAdd, self).__init__()
        self.ui = add_form.Ui_DialogAdd()
        self.ui.setupUi(self)
        self.ui.buttonBox.clicked.connect(self.add_item)

    def add_item(self, button):
        """Добовляет запись в таблицу"""
        standard_button = self.sender().standardButton(button)  # Получаем стандартную константу кнопки (Ok или Cancel)
        if standard_button == QDialogButtonBox.Ok:
            title = self.ui.lineEdit_title.text()
            invent = self.ui.lineEdit_invent.text()
            count = int(self.ui.spinBox.text())
            price = self.ui.doubleSpinBox.value()
            date = self.ui.dateEdit.date().toString("dd-MM-yyyy")
            if all([title, invent, count, price, date]):
                status = True
                print('Запись в БД', status)
                # очищаем форму
                self.ui.lineEdit_title.setText('')
                self.ui.lineEdit_invent.setText('')
                self.ui.spinBox.setValue(0)
                self.ui.doubleSpinBox.setValue(0.0)
                self.close()
        else:  # standard_button == QDialogButtonBox.Cancel:
            print("Cancel button was clicked")
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
        self.ui.btn_add.clicked.connect(self.add_item)
        self.ui.btn_update.clicked.connect(self.update_item)
        self.ui.btn_remove.clicked.connect(self.delete_item)
        self.ui.btn_search.clicked.connect(self.search_item)
        self.current_dialog = None

    def open_dialog_window(self, func):
        """Открывает новое диалоговое окно и закрывает старое"""
        if self.current_dialog is not None:
            self.current_dialog.close()
        child_window = func
        self.current_dialog = child_window
        func.show()

    def search_item(self):
        """Поиск записи в БД"""
        print('Получение записи из БД')

    def delete_item(self):
        """Вызывает диалоговое окно для удаления записи"""
        self.open_dialog_window(self.dialog_delete)

    def add_item(self):
        """Вызывает диалоговое окно для создания записи"""
        self.open_dialog_window(self.dialog_add)

    def update_item(self):
        """Вызывает диалоговое окно для обновления записи"""
        self.open_dialog_window(self.dialog_update)

    def closeEvent(self, event):
        """Автоматически закрывает диалоговое окно при выходе из программы"""
        for widget in QApplication.topLevelWidgets():
            if isinstance(widget, QDialog):
                widget.close()
        event.accept()
