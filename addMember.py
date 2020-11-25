import sys
from uuid import uuid4

import qrcode
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from utils import createQrId


class AddMember(QDialog):
    def __init__(self, parent, cursor) -> None:
        super().__init__(parent)
        self.cursor = cursor
        self.setupUi()
        self.connectUi()

    def setupUi(self):
        self.setWindowTitle("Add Member")
        self.resize(720, 360)
        self.setModal(True)

        self.gridLayout = QGridLayout(self)

        self.firstNameLabel = QLabel(self)
        self.firstNameLabel.setText("First Name")

        self.gridLayout.addWidget(self.firstNameLabel, 0, 0, 1, 1)

        self.firstNameLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.firstNameLineEdit, 0, 1, 1, 1)

        self.lastNameLabel = QLabel(self)
        self.lastNameLabel.setText("Last Name")

        self.gridLayout.addWidget(self.lastNameLabel, 1, 0, 1, 1)

        self.lastNameLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.lastNameLineEdit, 1, 1, 1, 1)

        self.genderLabel = QLabel(self)
        self.genderLabel.setText("Gender")

        self.gridLayout.addWidget(self.genderLabel, 2, 0, 1, 1)

        self.genderComboBox = QComboBox(self)
        self.genderComboBox.addItem("Male")
        self.genderComboBox.addItem("Female")

        self.gridLayout.addWidget(self.genderComboBox, 2, 1, 1, 1)

        self.dateOfBirthLabel = QLabel(self)
        self.dateOfBirthLabel.setText("Date Of Birth")

        self.gridLayout.addWidget(self.dateOfBirthLabel, 3, 0, 1, 1)

        self.dateOfBirthDateEdit = QDateEdit(self)
        self.dateOfBirthDateEdit.setCalendarPopup(True)
        self.dateOfBirthDateEdit.setMaximumDate(QDate.currentDate())

        self.gridLayout.addWidget(self.dateOfBirthDateEdit, 3, 1, 1, 1)

        self.emailLabel = QLabel(self)
        self.emailLabel.setText("Email")

        self.gridLayout.addWidget(self.emailLabel, 4, 0, 1, 1)

        self.emailLineEdit = QLineEdit(self)

        self.gridLayout.addWidget(self.emailLineEdit, 4, 1, 1, 1)

        self.membershipPlanLabel = QLabel(self)
        self.membershipPlanLabel.setText("Membership Plan")

        self.gridLayout.addWidget(self.membershipPlanLabel, 5, 0, 1, 1)

        self.membershipPlanComboBox = QComboBox(self)

        self.gridLayout.addWidget(self.membershipPlanComboBox, 5, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 6, 0, 1, 2)

    def connectUi(self):
        self.buttonBox.accepted.connect(self.addMemberFunc)
        self.buttonBox.rejected.connect(self.reject)

    def addMemberFunc(self):
        # Validate inputs. If failed show QMessageBox.critical(self, "Title", "Error Message"), return
        uuid = str(uuid4())
        name = f"{self.firstNameLineEdit.text()} {self.lastNameLineEdit.text()} \
            {self.membershipPlanComboBox.currentText()}"
        filePath, _ = QFileDialog.getSaveFileName(
            self, "Save ID as", f"{name}.png", "PNG Image")
        if filePath:
            data = {"First Name": "Monish"}  # Change to actual data
            createQrId(uuid, data).save(filePath)
        self.accept()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = AddMember(None, None)
    win.show()
    sys.exit(app.exec_())
