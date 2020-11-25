import sys

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from dashboard import Dashboard
from dialogs import ScanQR
from manageBooks import ManageBooks
from manageIssues import ManageIssues
from manageMembers import ManageMembers
from manageStaff import ManageStaff


class StackedWidget(QStackedWidget):
    def __init__(self, cursor) -> None:
        super().__init__()
        self.cursor = cursor

        self.initUi()
        self.handleLogin()

        self.setCurrentWidget(self.dashboard)
        self.setWindowTitle("Dashboard")

    def initUi(self):
        self.setWindowIcon(QIcon("images/icon.ico"))
        self.resize(1280, 720)

    def initWidgets(self):
        count = self.count()
        for i in range(count):
            self.removeWidget(self.widget(i))
            count = self.count
        self.dashboard = Dashboard(self.cursor, self.staffManageBooks, self.staffManageIssues,
                                   self.staffManageMember, self.staffManageStaff)
        self.addWidget(self.dashboard)
        self.manageStaff = ManageStaff(self.cursor)
        self.addWidget(self.manageStaff)
        self.manageIssues = ManageIssues(self.cursor)
        self.addWidget(self.manageIssues)
        self.manageBooks = ManageBooks(self.cursor)
        self.addWidget(self.manageBooks)
        self.manageMembers = ManageMembers(self.cursor)
        self.addWidget(self.manageMembers)

        self.connectUi()

    def connectUi(self):
        self.currentChanged.connect(
            lambda x: self.setWindowTitle(self.widget(x).title))
        self.dashboard.manageStaff.clicked.connect(
            lambda: self.setCurrentWidget(self.manageStaff))
        self.manageStaff.back.clicked.connect(
            lambda: self.setCurrentWidget(self.dashboard))
        self.dashboard.manageIssues.clicked.connect(
            lambda: self.setCurrentWidget(self.manageIssues))
        self.manageIssues.back.clicked.connect(
            lambda: self.setCurrentWidget(self.dashboard))
        self.dashboard.manageBooks.clicked.connect(
            lambda: self.setCurrentWidget(self.manageBooks))
        self.manageBooks.back.clicked.connect(
            lambda: self.setCurrentWidget(self.dashboard))
        self.dashboard.manageMembers.clicked.connect(
            lambda: self.setCurrentWidget(self.manageMembers))
        self.manageMembers.back.clicked.connect(
            lambda: self.setCurrentWidget(self.dashboard))
        self.dashboard.logout.clicked.connect(self.handleLogin)

    def handleLogin(self):
        # get all staff UUIDs from db (reference)
        reference = ["1" * 36]
        staffQR = ScanQR(
            self, reference, title="Scan QR code in staff ID to login").exec_()  # dummy regex
        if staffQR:
            # set staff access levels
            self.staffManageMember = True
            self.staffManageStaff = True
            self.staffManageBooks = True
            self.staffManageIssues = True
            self.initWidgets()
        else:
            sys.exit()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # create the mysql cursor and pass it to stacked widget
    mainWindow = StackedWidget(None)
    mainWindow.show()
    sys.exit(app.exec_())
