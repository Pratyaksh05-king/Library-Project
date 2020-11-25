# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'self.ui'
##
# Created by: Qt User Interface Compiler version 5.15.1
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from dialogs import ScanQR
from utils import addDataToTable


class ManageIssues(QWidget):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor
        self.title = "Manage Issues"
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.verticalLayout = QVBoxLayout(self)
        self.backHorizontalLayout = QHBoxLayout()
        self.back = QPushButton(self)
        self.back.setText("Back")

        self.backHorizontalLayout.addWidget(self.back)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.backHorizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.backHorizontalLayout)

        self.groupBox = QGroupBox(self)
        self.groupBox.setTitle("Search")

        self.gridLayout = QGridLayout(self.groupBox)

        self.bookTitleLabel = QLabel(self.groupBox)
        self.bookTitleLabel.setText("Book Title")

        self.gridLayout.addWidget(self.bookTitleLabel, 0, 0, 1, 1)

        self.bookTitleLineEdit = QLineEdit(self.groupBox)

        self.gridLayout.addWidget(self.bookTitleLineEdit, 0, 1, 1, 3)

        self.issuedAfterLabel = QLabel(self.groupBox)
        self.issuedAfterLabel.setText("Issued After")

        self.gridLayout.addWidget(self.issuedAfterLabel, 1, 0, 1, 1)

        self.issuedAfterDateEdit = QDateEdit(self.groupBox)
        self.issuedAfterDateEdit.setCalendarPopup(True)
        self.issuedAfterDateEdit.setMaximumDate(QDate.currentDate())

        self.gridLayout.addWidget(self.issuedAfterDateEdit, 1, 1, 1, 1)

        self.issuedBeforeLabel = QLabel(self.groupBox)
        self.issuedBeforeLabel.setText("Before")

        self.gridLayout.addWidget(self.issuedBeforeLabel, 1, 2, 1, 1)

        self.issuedBeforeDateEdit = QDateEdit(self.groupBox)
        self.issuedBeforeDateEdit.setCalendarPopup(True)
        self.issuedBeforeDateEdit.setMaximumDate(QDate.currentDate())
        self.issuedBeforeDateEdit.setDate(QDate.currentDate())

        self.gridLayout.addWidget(self.issuedBeforeDateEdit, 1, 3, 1, 1)

        self.fineAmountMinLabel = QLabel(self.groupBox)
        self.fineAmountMinLabel.setText("Fine Amount From")

        self.gridLayout.addWidget(self.fineAmountMinLabel, 2, 0, 1, 1)

        self.fineAmountMinLineEdit = QLineEdit(self.groupBox)
        self.fineAmountMinLineEdit.setValidator(QIntValidator())

        self.gridLayout.addWidget(self.fineAmountMinLineEdit, 2, 1, 1, 1)

        self.fineAmountMaxLabel = QLabel(self.groupBox)
        self.fineAmountMaxLabel.setText("To")

        self.gridLayout.addWidget(self.fineAmountMaxLabel, 2, 2, 1, 1)

        self.fineAmountMaxLineEdit = QLineEdit(self.groupBox)
        self.fineAmountMaxLineEdit.setValidator(QIntValidator())

        self.gridLayout.addWidget(self.fineAmountMaxLineEdit, 2, 3, 1, 1)

        self.search = QPushButton(self.groupBox)
        self.search.setText("Search")

        self.gridLayout.addWidget(self.search, 6, 1, 1, 3)

        self.verticalLayout.addWidget(self.groupBox)

        self.tableWidget = QTableWidget(self)
        self.tableWidget.setFocusPolicy(Qt.NoFocus)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setShowGrid(False)
        self.tableWidget.setSortingEnabled(True)
        self.tableWidget.setStyleSheet(
            "background-color: white; selection-background-color: #a8cce9;")
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.tableWidget)

        self.backHorizontalLayout = QHBoxLayout()
        self.issueCopy = QPushButton(self)
        self.issueCopy.setText("Issue Copy")

        self.backHorizontalLayout.addWidget(self.issueCopy)

        self.recallCopy = QPushButton(self)
        self.recallCopy.setText("Recall Copy")

        self.backHorizontalLayout.addWidget(self.recallCopy)

        self.compensateCopy = QPushButton(self)
        self.compensateCopy.setText("Compensate Copy")

        self.backHorizontalLayout.addWidget(self.compensateCopy)

        self.verticalLayout.addLayout(self.backHorizontalLayout)

    def connectUi(self):
        self.search.clicked.connect(self.searchFunc)
        self.issueCopy.clicked.connect(self.issueCopyFunc)
        self.recallCopy.clicked.connect(self.recallCopyFunc)
        self.compensateCopy.clicked.connect(self.compensateCopyFunc)
        self.issuedAfterDateEdit.dateChanged.connect(
            lambda date: self.issuedBeforeDateEdit.setMinimumDate(date))
        self.issuedBeforeDateEdit.dateChanged.connect(
            lambda date: self.issuedAfterDateEdit.setMaximumDate(date))
        self.fineAmountMinLineEdit.textChanged.connect(
            self.fineAmountMinLineEditFunc)
        self.fineAmountMaxLineEdit.textChanged.connect(
            self.fineAmountMaxLineEditFunc)

    def searchFunc(self):
        # Validate inputs. If failed show QMessageBox.warning(self, "Title", "Error Message")
        # Generate SQL from inputs
        # Add data from db using addDataToTable
        pass

    def issueCopyFunc(self):
        # get all copy UUIDs from db (reference)
        reference = ["1" * 36]
        copyQR = ScanQR(self, reference, title="Scan QR code of Copy").exec_()
        if not copyQR:
            return
        # get all member UUIDs from db (reference)
        reference = ["1" * 36]
        memberQR = ScanQR(
            self, reference, title="Scan QR code of Member").exec_()
        if not memberQR:
            return
        # Check if copy is available and member hasn't reached limit, else show error message
        # Add copy to issued

    def recallCopyFunc(self):
        # get all copy UUIDs from db (reference)
        reference = ["1" * 36]
        copyQR = ScanQR(self, reference).exec_()
        # remove copy from issues in db if issued, else show error message

    def compensateCopyFunc(self):
        if self.tableWidget.currentRow() == -1:
            QMessageBox.warning(
                self, "No Copy Selected", "Please select a copy in table to compensate")
            return
        # get primary key of copy selected and remove it from copies table in db

    def fineAmountMinLineEditFunc(self, string):
        try:
            if int(string) > int(self.fineAmountMaxLineEdit.text()):
                self.fineAmountMaxLineEdit.setText(string)
        except:
            pass

    def fineAmountMaxLineEditFunc(self, string):
        try:
            if int(string) < int(self.fineAmountMinLineEdit.text()):
                self.fineAmountMinLineEdit.setText(string)
        except:
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ManageIssues(None)
    win.show()
    sys.exit(app.exec_())
