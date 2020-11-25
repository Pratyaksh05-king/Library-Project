import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from addStaff import AddStaff
from dialogs import ScanQR


class ManageStaff(QWidget):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor
        self.title = "Manage Staff"
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

        self.gridLayout = QGridLayout(self.searchGroupBox)

        self.nameLabel = QLabel(self.searchGroupBox)
        self.nameLabel.setText("Name")

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 3)

        self.nameLineEdit = QLineEdit(self.searchGroupBox)

        self.gridLayout.addWidget(self.nameLineEdit, 0, 1, 1, 3)

        self.joinedAfterLabel = QLabel(self.searchGroupBox)
        self.joinedAfterLabel.setText("Joined After")

        self.gridLayout.addWidget(self.joinedAfterLabel, 1, 0, 1, 1)

        self.joinedAfterDateEdit = QDateEdit(self.searchGroupBox)
        self.joinedAfterDateEdit.setCalendarPopup(True)
        self.joinedAfterDateEdit.setMaximumDate(QDate.currentDate())

        self.gridLayout.addWidget(self.joinedAfterDateEdit, 1, 1, 1, 1)

        self.joinedBeforeLabel = QLabel(self.searchGroupBox)
        self.joinedBeforeLabel.setText("Before")

        self.gridLayout.addWidget(self.joinedBeforeLabel, 1, 2, 1, 1)

        self.joinedBeforeDateEdit = QDateEdit(self.searchGroupBox)
        self.joinedBeforeDateEdit.setCalendarPopup(True)
        self.joinedBeforeDateEdit.setMaximumDate(QDate.currentDate())
        self.joinedBeforeDateEdit.setDate(QDate.currentDate())

        self.gridLayout.addWidget(self.joinedBeforeDateEdit, 1, 3, 1, 1)

        self.jobTitleLabel = QLabel(self.searchGroupBox)
        self.jobTitleLabel.setText("Job Title")

        self.gridLayout.addWidget(self.jobTitleLabel, 2, 0, 1, 1)

        self.jobTitleComboBox = QComboBox(self.searchGroupBox)
        # Add code to add jobs titles from db

        self.gridLayout.addWidget(self.jobTitleComboBox, 2, 1, 1, 3)

        self.search = QPushButton(self.searchGroupBox)
        self.search.setText("Search")

        self.gridLayout.addWidget(self.search, 3, 1, 1, 3)

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

        self.scanQR = QPushButton(self)
        self.scanQR.setText("Scan QR Code")

        self.optionsHorizontalLayout.addWidget(self.scanQR)

        self.addNewStaff = QPushButton(self)
        self.addNewStaff.setText("Add New Staff")

        self.optionsHorizontalLayout.addWidget(self.addNewStaff)

        self.removeStaff = QPushButton(self)
        self.removeStaff.setText("Remove Staff")

        self.optionsHorizontalLayout.addWidget(self.removeStaff)

        self.verticalLayout.addLayout(self.optionsHorizontalLayout)

    def connectUi(self):
        self.search.clicked.connect(self.searchFunc)
        self.scanQR.clicked.connect(self.scanQRFunc)
        self.addNewStaff.clicked.connect(AddStaff(self, self.cursor).exec_)
        self.removeStaff.clicked.connect(self.removeStaffFunc)
        self.joinedAfterDateEdit.dateChanged.connect(
            lambda date: self.joinedBeforeDateEdit.setMinimumDate(date))
        self.joinedBeforeDateEdit.dateChanged.connect(
            lambda date: self.joinedAfterDateEdit.setMaximumDate(date))

    def searchFunc(self):
        # Validate inputs. If failed show QMessageBox.warning(self, "Title", "Error Message")
        # Generate SQL from inputs
        # Add data from db using addDataToTable
        pass

    def scanQRFunc(self):
        # get all staff UUIDs from db (reference)
        reference = ["1" * 36]
        staffQR = ScanQR(self, reference).exec_()
        # use primary key to search staff table and use addDatatoTable(if staff exists else error message)

    def removeStaffFunc(self):
        # get all staff UUIDs from db (reference)
        reference = ["1" * 36]
        staffQR = ScanQR(self, reference).exec_()
        # remove staff if exists else error message


if __name__ == "__main__":
    app = QApplication([])
    win = ManageStaff(None)
    win.show()
    sys.exit(app.exec_())
