from PyQt5.QtWidgets import QMainWindow
from messengerPy.server.ui.server_monitor import Ui_ServerWindow as server_ui_class


class ServerMonitorWindow(QMainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = server_ui_class()
        self.ui.setupUi(self)
