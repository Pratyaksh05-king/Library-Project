import sys
from uuid import uuid4

import qrcode
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from addBook import AddBook
from dialogs import ScanISBN13, ScanQR
from utils import addDataToTable


class ManageBooks(QWidget):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor
        self.title = "Manage Books"
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

        self.searchGroupBox = QGroupBox(self)
        self.searchGroupBox.setTitle("Search")

        self.formLayout = QFormLayout(self.searchGroupBox)
        self.nameLabel = QLabel(self.searchGroupBox)
        self.nameLabel.setText("Name")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.nameLabel)

        self.nameLineEdit = QLineEdit(self.searchGroupBox)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.nameLineEdit)

        self.categoryLabel = QLabel(self.searchGroupBox)
        self.categoryLabel.setText("Category")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.categoryLabel)

        self.categoryComboBox = QComboBox(self.searchGroupBox)

        self.formLayout.setWidget(
            1, QFormLayout.FieldRole, self.categoryComboBox)

        self.authorLabel = QLabel(self.searchGroupBox)
        self.authorLabel.setText("Author")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.authorLabel)

        self.authorLineEdit = QLineEdit(self.searchGroupBox)

        self.formLayout.setWidget(
            2, QFormLayout.FieldRole, self.authorLineEdit)

        self.publisherLabel = QLabel(self.searchGroupBox)
        self.publisherLabel.setText("Publisher")

        self.formLayout.setWidget(
            3, QFormLayout.LabelRole, self.publisherLabel)

        self.publisherLineEdit = QLineEdit(self.searchGroupBox)

        self.formLayout.setWidget(
            3, QFormLayout.FieldRole, self.publisherLineEdit)

        self.search = QPushButton(self.searchGroupBox)
        self.search.setText("Search")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.search)

        self.verticalLayout.addWidget(self.searchGroupBox)

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

        self.optionsHorizontalLayout = QHBoxLayout()
        self.scanISBN13 = QPushButton(self)
        self.scanISBN13.setText("Scan ISBN-13")

        self.optionsHorizontalLayout.addWidget(self.scanISBN13)

        self.addNewBook = QPushButton(self)
        self.addNewBook.setText("Add New Book")

        self.optionsHorizontalLayout.addWidget(self.addNewBook)

        self.addCopy = QPushButton(self)
        self.addCopy.setText("Add Copy")

        self.optionsHorizontalLayout.addWidget(self.addCopy)

        self.removeCopy = QPushButton(self)
        self.removeCopy.setText("Remove Copy")

        self.optionsHorizontalLayout.addWidget(self.removeCopy)

        self.verticalLayout.addLayout(self.optionsHorizontalLayout)

    def connectUi(self):
        self.search.clicked.connect(self.searchFunc)
        self.scanISBN13.clicked.connect(self.scanISBN13Func)
        self.addNewBook.clicked.connect(AddBook(self, self.cursor).exec_)
        self.addCopy.clicked.connect(self.addCopyFunc)
        self.removeCopy.clicked.connect(self.removeCopyFunc)

    def searchFunc(self):
        # Generate SQL from inputs
        # Add data from db using addDataToTable
        pass

    def scanISBN13Func(self):
        # get all ISBN-13s from db (reference)
        reference = ["1" * 13]
        isbn = ScanISBN13(self, reference).exec_()
        # Get data from db and add data from db using isbn and addDatatoTable

    def addCopyFunc(self):
        # get all ISBN-13s from db (reference)
        reference = ["1" * 13]
        isbn = ScanISBN13(self, reference).exec_()
        # Get book name and number of copies using ISBN from db and remove below line
        name, copy = "Book", 3
        uuid = str(uuid4())
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save QR code as", f"{name} {copy}.png", "PNG Image")
        if filePath:
            qrcode.make(uuid).save(filePath)
            # Save copy to db and QR to file.

    def removeCopyFunc(self):
        # get all book UUIDs from db (reference)
        reference = ["1" * 36]
        qr = ScanQR(self, reference).exec_()
        # Remove Copy from db if it is not in issues


if __name__ == "__main__":
    app = QApplication([])
    win = ManageBooks(None)
    win.show()
    sys.exit(app.exec_())
