import sqlite3
from PyQt5.QtWidgets import QDialog

from Dialog_error_post import Ui_Error_post_dialog
from Dialog_successfully_post import Ui_Successfully_post_dialog
from Dialog_proxy_settings import Ui_Dialog_proxy_settings
from Dialog_authorization import Ui_Dialog_authorization_settings
from Dialog_links_food import Ui_Dialog_links_food


class Error_post_dialog(QDialog, Ui_Error_post_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close())


def error_post_dialog_show():
    dialog = Error_post_dialog()
    dialog.show()
    dialog.exec_()


class Succefully_post_dialog(QDialog, Ui_Successfully_post_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.close_button.clicked.connect(lambda: self.close())


class Dialog_proxy_settings(QDialog, Ui_Dialog_proxy_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.download_data()

    def accept(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''UPDATE users_data  SET proxy = "{self.lineEdit.text()}"''')
        db.commit()
        db.close()
        self.close()

    def download_data(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''SELECT proxy FROM users_data''')
        cur = cur.fetchall()
        self.lineEdit.setText(str(cur[0][0]))
        db.close()


def dialog_proxy_settings():
    dialog = Dialog_proxy_settings()
    dialog.show()
    dialog.exec_()


class Dialog_authorization_settings(QDialog, Ui_Dialog_authorization_settings):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.download_data()

    def accept(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''UPDATE users_data  SET login = "{self.lineEdit_login.text()}", password = "{self.lineEdit_password.text()}"''')
        db.commit()
        db.close()
        self.close()

    def download_data(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''SELECT login, password FROM users_data''')
        cur = cur.fetchall()
        self.lineEdit_login.setText(str(cur[0][0]))
        self.lineEdit_password.setText(str(cur[0][1]))
        db.close()


def dialog_authorization_settings():
    dialog = Dialog_authorization_settings()
    dialog.show()
    dialog.exec_()


class Dialog_links_food(QDialog, Ui_Dialog_links_food):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.download_data()

    def accept(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''UPDATE users_data  SET link_folder_food = "{self.lineEdit.text()}", page_folder_food = "{self.lineEdit_2.text()}"''')
        db.commit()
        db.close()
        self.close()

    def download_data(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''SELECT link_folder_food, page_folder_food FROM users_data''')
        cur = cur.fetchall()
        self.lineEdit.setText(str(cur[0][0]))
        self.lineEdit_2.setText(str(cur[0][1]))
        db.close()


def dialog_links_food_settings():
    dialog = Dialog_links_food()
    dialog.show()
    dialog.exec_()


def succefully_post_dialog_show():
    dialog = Succefully_post_dialog()
    dialog.show()
    dialog.exec_()
