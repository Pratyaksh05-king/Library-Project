import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from dialogs import AddAuthor, AddPublisher


class Dashboard(QWidget):
    def __init__(self, cursor, staffManageBooks, staffManageIssues, staffManageMembers, staffManageStaff) -> None:
        super().__init__()
        self.cursor = cursor
        self.title = "Dashboard"
        self.setupUi(staffManageBooks, staffManageIssues,
                     staffManageMembers, staffManageStaff)
        self.connectUi()

    def setupUi(self, staffManageBooks, staffManageIssues, staffManageMembers, staffManageStaff):
        self.gridLayout = QGridLayout(self)

        self.addAuthor = QPushButton(self)
        self.addAuthor.setText("Add Author")

        self.gridLayout.addWidget(self.addAuthor, 3, 3, 1, 1)

        self.addPublishers = QPushButton(self)
        self.addPublishers.setText("Add Publishers")

        self.gridLayout.addWidget(self.addPublishers, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 3, 4, 1, 1)

        self.manageIssues = QPushButton(self)
        self.manageIssues.setText("Manage Issues")
        if not staffManageIssues:
            self.manageIssues.setEnabled(False)

        self.gridLayout.addWidget(self.manageIssues, 4, 3, 1, 1)

        self.manageStaff = QPushButton(self)
        self.manageStaff.setText("Manage Staff")
        if not staffManageStaff:
            self.manageStaff.setEnabled(False)

        self.gridLayout.addWidget(self.manageStaff, 4, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 2, 1, 1)

        self.headerLabel = QLabel(self)
        self.headerLabel.setAlignment(Qt.AlignCenter)
        self.headerLabel.setText("XYZ Library")

        self.gridLayout.addWidget(self.headerLabel, 1, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.manageMembers = QPushButton(self)
        self.manageMembers.setText("Manage Members")
        if not staffManageMembers:
            self.manageMembers.setEnabled(False)

        self.gridLayout.addWidget(self.manageMembers, 3, 2, 1, 1)

        self.manageBooks = QPushButton(self)
        self.manageBooks.setText("Manage Books")
        if not staffManageBooks:
            self.manageBooks.setEnabled(False)

        self.gridLayout.addWidget(self.manageBooks, 4, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 2, 1, 1)

        self.logout = QPushButton(self)
        self.logout.setText("Logout")

        self.gridLayout.addWidget(self.logout, 5, 2, 1, 1)

    def connectUi(self):
        self.addAuthor.clicked.connect(AddAuthor(self, self.cursor).exec_)
        self.addPublishers.clicked.connect(
            AddPublisher(self, self.cursor).exec_)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = Dashboard(None)
    w.show()
    sys.exit(app.exec_())
