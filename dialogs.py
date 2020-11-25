import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AddAuthor(QDialog):
    def __init__(self, parent, cursor) -> None:
        super().__init__(parent)
        self.cursor = cursor
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle("Add Author")
        self.resize(400, 200)

        self.gridLayout = QGridLayout(self)

        self.nameLabel = QLabel(self)
        self.nameLabel.setText("First Name")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

        self.firstNameLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.firstNameLineEdit, 0, 1, 1, 1)

        self.lastNameLabel = QLabel(self)
        self.lastNameLabel.setText("Last Name")

        self.gridLayout.addWidget(self.lastNameLabel, 1, 0, 1, 1)

        self.lastNameLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.addAuthorFunc)
        self.buttonBox.rejected.connect(self.reject)

    def addAuthorFunc(self):
        # Add code to validate and add author to db
        self.accept()


class AddPublisher(QDialog):
    def __init__(self, parent, cursor) -> None:
        super().__init__(parent)
        self.cursor = cursor
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle("Add Publisher")
        self.resize(400, 150)

        self.gridLayout = QGridLayout(self)

        self.publisherNameLabel = QLabel(self)
        self.publisherNameLabel.setText("Publisher Name")

        self.gridLayout.addWidget(self.publisherNameLabel, 0, 0, 1, 1)

        self.publisherNameLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.publisherNameLineEdit, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.addPublisherFunc)
        self.buttonBox.rejected.connect(self.reject)

    def addPublisherFunc(self):
        # Add code to validate and add pbulisher to db
        self.accept()


class ScanSequence(QDialog):
    def __init__(self, parent, refernce, title, regexp, errorTitle, errorMessage) -> None:
        super().__init__(parent)
        self.title, self.regexp = title, regexp
        self.errorTitle, self.errorMessage = errorTitle, errorMessage
        self.reference = refernce
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle(self.title)
        self.resize(400, 150)

        self.verticalLayout = QVBoxLayout(self)

        self.sequenceLineEdit = QLineEdit(self)
        self.sequenceLineEdit.setEchoMode(QLineEdit.Password)
        self.sequenceLineEdit.setValidator(QRegExpValidator(self.regexp))

        self.verticalLayout.addWidget(self.sequenceLineEdit)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.validateAndAccept)
        self.buttonBox.rejected.connect(self.reject)

    def validateAndAccept(self):
        if self.sequenceLineEdit.text() in self.reference:
            self.accept()
        else:
            QMessageBox.warning(
                self, self.errorTitle, self.errorMessage)

    def exec_(self):
        if super().exec_():
            return self.sequenceLineEdit.text()
        return 0


class ScanISBN13(ScanSequence):
    def __init__(self, parent, reference=["1" * 13], title="Scan ISBN-13", regex="^[0-9]{13}$",
                 errorTitle="Invalid ISBN-13", errorMessage="Please scan a valid ISBN-13 barcode") -> None:
        super().__init__(parent, reference, title, regex,
                         errorTitle, errorMessage)


class ScanQR(ScanSequence):
    def __init__(self, parent, reference=["1" * 36], title="Scan QR", regex="^[0-9a-f]{36}$",
                 errorTitle="Invalid QR Code", errorMessage="Please scan a valid QR code") -> None:
        super().__init__(parent, reference, title, regex,
                         errorTitle, errorMessage)


class ChangeMembership(QDialog):
    def __init__(self, parent, cursor) -> None:
        super().__init__(parent)
        self.cursor = cursor
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle("Change Membership Type")
        self.resize(400, 150)

        self.gridLayout = QGridLayout(self)

        self.membershipTypeLabel = QLabel(self)
        self.membershipTypeLabel.setText("New Membership Type")

        self.gridLayout.addWidget(self.membershipTypeLabel, 0, 0, 1, 1)

        self.membershipTypeComboBox = QComboBox(self)
        # get membership types from db

        self.gridLayout.addWidget(self.membershipTypeComboBox, 0, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 2)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.changeMembershipFunc)
        self.buttonBox.rejected.connect(self.reject)

    def changeMembershipFunc(self):
        # change membership type and set exp date 1 year from now
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ScanQR(None)
    print(win.exec_())
