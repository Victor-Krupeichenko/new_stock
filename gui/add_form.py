# -*- coding: utf-8 -*-
from PySide2 import QtCore
################################################################################
## Form generated from reading UI file 'add_form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from datetime import datetime

now = datetime.now()
year = now.year
month = now.month
day = now.day


class Ui_DialogAdd(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(529, 453)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, -1, 5, -1)
        self.label_title = QLabel(self.frame)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setEnabled(True)
        font = QFont()
        font.setPointSize(10)
        self.label_title.setFont(font)
        self.label_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_title)

        self.lineEdit_title = QLineEdit(self.frame)
        self.lineEdit_title.setObjectName(u"lineEdit_title")
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_title.setFont(font1)
        self.lineEdit_title.setFocusPolicy(Qt.StrongFocus)

        self.verticalLayout_2.addWidget(self.lineEdit_title)

        self.label_invent = QLabel(self.frame)
        self.label_invent.setObjectName(u"label_invent")
        self.label_invent.setFont(font)
        self.label_invent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_invent)

        self.lineEdit_invent = QLineEdit(self.frame)
        self.lineEdit_invent.setObjectName(u"lineEdit_invent")
        self.lineEdit_invent.setFont(font1)
        self.lineEdit_invent.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.lineEdit_invent)

        self.label_count = QLabel(self.frame)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setFont(font)
        self.label_count.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_count)

        self.spinBox = QSpinBox(self.frame)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setFont(font1)
        self.spinBox.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.spinBox)

        self.label_price = QLabel(self.frame)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setFont(font)
        self.label_price.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_price)

        self.doubleSpinBox = QDoubleSpinBox(self.frame)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setFont(font1)
        self.doubleSpinBox.setFocusPolicy(Qt.ClickFocus)

        self.verticalLayout_2.addWidget(self.doubleSpinBox)

        self.label_date = QLabel(self.frame)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font)
        self.label_date.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_date)

        self.dateEdit = QDateEdit(self.frame)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)
        self.dateEdit.setFocusPolicy(Qt.ClickFocus)
        self.dateEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(year, month, day)))

        self.verticalLayout_2.addWidget(self.dateEdit)

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(5, -1, 5, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(self.frame)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font1)
        self.buttonBox.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)

    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add Item", None))
        self.label_title.setText(QCoreApplication.translate("Dialog", u"Title:", None))
        self.label_invent.setText(QCoreApplication.translate("Dialog", u"Inventary number:", None))
        self.label_count.setText(QCoreApplication.translate("Dialog", u"Count:", None))
        self.label_price.setText(QCoreApplication.translate("Dialog", u"Price:", None))
        self.label_date.setText(QCoreApplication.translate("Dialog", u"Date:", None))
    # retranslateUi
