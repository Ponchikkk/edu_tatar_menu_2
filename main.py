import sys
import sqlite3
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog

from eduauth import edu_auth
from edu_tatar_functions import upload_files, post_page, get_files

from untitled import Ui_QMainWindow
from dialogs import error_post_dialog_show, succefully_post_dialog_show, dialog_proxy_settings, \
    dialog_authorization_settings, dialog_links_food_settings


class MainWindow(QMainWindow, Ui_QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_file = ""
        self.show()
        self.data()

        self.pushButton_close_application.clicked.connect(self.exit)
        self.pushButton_send.clicked.connect(self.send_file)
        self.pushBatton_attach_file.clicked.connect(self.attach_file)
        self.pushButton_unpin_file.clicked.connect(self.unpin_file)

        self.QAction_proxy_settings.triggered.connect(self.proxy_settings)
        self.Qaction_authorization_settings.triggered.connect(self.authorization_settings)
        self.QAction_linkfood_settings.triggered.connect(self.linkfood_settings)

    def exit(self):
        sys.exit()

    def data(self):
        db = sqlite3.connect("edu_tatar_ru_menu.db")
        cur = db.cursor()
        cur.execute(
            f'''SELECT login, password, link_folder_food, page_folder_food, proxy FROM users_data''')
        cur = cur.fetchall()
        print(cur)
        db.close()
        return [str(i) for i in cur[0]]

    def attach_file(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\')
        self.path_file = fname[0]
        self.label_file_path.setText(self.path_file.split("/")[-1])
        self.statusbar.showMessage("Файл прикреплен")

    def unpin_file(self):
        self.label_file_path.setText("")
        self.path_file = ""
        self.statusbar.showMessage("Файл откреплен")

    def proxy_settings(self):
        dialog_proxy_settings()

    def authorization_settings(self):
        dialog_authorization_settings()

    def linkfood_settings(self):
        dialog_links_food_settings()

    def send_file(self):
        login, password, link_folder_food, page_folder_food, proxy = self.data()

        proxy = {"http": proxy}
        self.statusbar.showMessage("Операция выполняется...")
        # edu_session = edu_auth(login, password, proxy)

        # fp = open(self.path_file, "rb")
        # fn = self.path_file.split("/")[-1]
        # print(fn)
        # files = {'file': (fn, fp, 'application/vnd.ms-excel')}
        # upload_files(edu_session, files, proxy)
        # post_page(edu_session, page_id=800107, data=get_files(edu_session), proxy=proxy)
        try:
            link_folder_food = "/".join(link_folder_food.split("/")[:7])
            fp = open(self.path_file, "rb")
            fn = self.path_file.split("/")[-1]
            print(fn)
            files = {'file': (fn, fp, 'application/vnd.ms-excel')}
            edu_session = edu_auth(login, password, proxy)
            upload_files(edu_session, files, proxy)
            post_page(edu_session, page_folder_food, get_files(edu_session, link_folder_food), proxy,
                      link_folder_food)
            succefully_post_dialog_show()
            self.statusbar.showMessage("Успешно!")
        except:
            self.statusbar.showMessage("Ошибка!")
            error_post_dialog_show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = MainWindow()

    sys.exit(app.exec_())
