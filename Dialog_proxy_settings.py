# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Dialog_proxy_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog_proxy_settings(object):
    def setupUi(self, Dialog_proxy_settings):
        Dialog_proxy_settings.setObjectName("Dialog_proxy_settings")
        Dialog_proxy_settings.resize(400, 296)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog_proxy_settings)
        self.buttonBox.setGeometry(QtCore.QRect(30, 240, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.widget = QtWidgets.QWidget(Dialog_proxy_settings)
        self.widget.setGeometry(QtCore.QRect(30, 100, 187, 23))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Dialog_proxy_settings)
        self.buttonBox.accepted.connect(Dialog_proxy_settings.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog_proxy_settings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog_proxy_settings)

    def retranslateUi(self, Dialog_proxy_settings):
        _translate = QtCore.QCoreApplication.translate
        Dialog_proxy_settings.setWindowTitle(_translate("Dialog_proxy_settings", "?????????????????? ????????????"))
        self.label.setText(_translate("Dialog_proxy_settings", "<html><head/><body><p align=\"right\">????????????:</p></body></html>"))
