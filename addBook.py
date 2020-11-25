import sys
from uuid import uuid4

import qrcode
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AddBook(QDialog):
    def __init__(self, parent, cursor) -> None:
        super().__init__(parent)
        self.cursor = cursor
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle("Add Book")
        self.resize(720, 360)
        self.setModal(True)

        self.gridLayout = QGridLayout(self)

        self.titleLabel = QLabel(self)
        self.titleLabel.setText("Title")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.titleLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.titleLineEdit, 0, 1, 1, 1)

        self.isbn13Label = QLabel(self)
        self.isbn13Label.setText("ISBN 13")

        self.gridLayout.addWidget(self.isbn13Label, 1, 0, 1, 1)

        self.isbn13LineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.isbn13LineEdit, 1, 1, 1, 1)

        self.numberOfCopiesLabel = QLabel(self)
        self.numberOfCopiesLabel.setText("Number of Copies")

        self.gridLayout.addWidget(self.numberOfCopiesLabel, 2, 0, 1, 1)

        self.numberOfCopiesSpinBox = QSpinBox(self)

        self.gridLayout.addWidget(self.numberOfCopiesSpinBox, 2, 1, 1, 1)

        self.authorLabel = QLabel(self)
        self.authorLabel.setText("Author")

        self.gridLayout.addWidget(self.authorLabel, 3, 0, 1, 1)

        self.authorComboBox = QComboBox(self)

        self.gridLayout.addWidget(self.authorComboBox, 3, 1, 1, 1)

        self.publisherLabel = QLabel(self)
        self.publisherLabel.setText("Publisher")

        self.gridLayout.addWidget(self.publisherLabel, 4, 0, 1, 1)

        self.publisherComboBox = QComboBox(self)

        self.gridLayout.addWidget(self.publisherComboBox, 4, 1, 1, 1)

        self.datePublishedLabel = QLabel(self)
        self.datePublishedLabel.setText("Date Published")

        self.gridLayout.addWidget(self.datePublishedLabel, 5, 0, 1, 1)

        self.datePublishedDateEdit = QDateEdit(self)
        self.datePublishedDateEdit.setCalendarPopup(True)
        self.datePublishedDateEdit.setDate(QDate.currentDate())
        self.datePublishedDateEdit.setMaximumDate(QDate.currentDate())

        self.gridLayout.addWidget(self.datePublishedDateEdit, 5, 1, 1, 1)

        self.priceLabel = QLabel(self)
        self.priceLabel.setText("Price")

        self.gridLayout.addWidget(self.priceLabel, 6, 0, 1, 1)

        self.priceLineEdit = QLineEdit(self)
        self.priceLineEdit.setValidator(QIntValidator())

        self.gridLayout.addWidget(self.priceLineEdit, 6, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)

        self.gridLayout.addWidget(self.buttonBox, 7, 0, 1, 2)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.addBookFunc)
        self.buttonBox.rejected.connect(self.reject)

    def addBookFunc(self):
        # Validate inputs. If failed show QMessageBox.warning(self, "Title", "Error Message"), return
        folderName = QFileDialog.getExistingDirectory(
            self, "Save QR codes to")
        if folderName:
            # Add Book to db Primary key ISBN-13
            for i in range(1, self.numberOfCopiesSpinBox.value() + 1):
                uuid = str(uuid4())
                # Add copy to db Primary Key UUID4
                qrcode.make(uuid).save(
                    f"{folderName}/{self.titleLineEdit.text()} Copy {i}.png")
            self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AddBook(None, None)
    win.show()
    sys.exit(app.exec_())
