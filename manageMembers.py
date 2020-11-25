import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from addMember import AddMember
from dialogs import ScanQR


class ManageMembers(QWidget):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor
        self.title = "Manage Members"
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

        self.gridLayout.addWidget(self.nameLabel, 0, 0, 1, 1)

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

        self.membershipTypeLabel = QLabel(self.searchGroupBox)
        self.membershipTypeLabel.setText("Membership Type")

        self.gridLayout.addWidget(self.membershipTypeLabel, 4, 0, 1, 1)

        self.membershipTypeComboBox = QComboBox(self.searchGroupBox)
        # Add code to add Membership types from db

        self.gridLayout.addWidget(self.membershipTypeComboBox, 4, 1, 1, 3)

        self.search = QPushButton(self.searchGroupBox)
        self.search.setText("Search")

        self.gridLayout.addWidget(self.search, 5, 1, 1, 3)

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

        self.addNewMember = QPushButton(self)
        self.addNewMember.setText("Add New Member")

        self.optionsHorizontalLayout.addWidget(self.addNewMember)

        self.renewMembership = QPushButton(self)
        self.renewMembership.setText("Renew Membership")

        self.optionsHorizontalLayout.addWidget(self.renewMembership)

        self.changeMembershipPlan = QPushButton(self)
        self.changeMembershipPlan.setText("Change Membership Plan")

        self.optionsHorizontalLayout.addWidget(self.changeMembershipPlan)

        self.removeMember = QPushButton(self)
        self.removeMember.setText("Remove Member")

        self.optionsHorizontalLayout.addWidget(self.removeMember)

        self.verticalLayout.addLayout(self.optionsHorizontalLayout)

    def connectUi(self):
        self.search.clicked.connect(self.searchFunc)
        self.scanQR.clicked.connect(self.scanQRFunc)
        self.addNewMember.clicked.connect(AddMember(self, self.cursor).exec_)
        self.renewMembership.clicked.connect(self.renewMembershipFunc)
        self.changeMembershipPlan.clicked.connect(
            self.changeMembershipPlanFunc)
        self.removeMember.clicked.connect(self.removeMemberFunc)
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
        # get all member UUIDs from db (reference)
        reference = ["1" * 36]
        memberQR = ScanQR(self, reference).exec_()
        # use primary key to search member table and use addDatatoTable(if member exists else error message)

    def renewMembershipFunc(self):
        # get all member UUIDs from db (reference)
        reference = ["1" * 36]
        memberQR = ScanQR(self, reference).exec_()
        # change exp date to 1 year from now(if member exists else error message)

    def changeMembershipPlanFunc(self):
        # get all member UUIDs from db (reference)
        reference = ["1" * 36]
        memberQR = ScanQR(self, reference).exec_()
        # change membership plan(if member exists else error message) and set exp date to 1 year from now

    def removeMemberFunc(self):
        # get all member UUIDs from db (reference)
        reference = ["1" * 36]
        memberQR = ScanQR(self, reference).exec_()
        # remove member if exists, else error message


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ManageMembers(None)
    win.show()
    sys.exit(app.exec_())
