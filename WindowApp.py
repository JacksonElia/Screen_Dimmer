from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMainWindow


class WindowApp(QMainWindow):

    def __init__(self):
        super(WindowApp, self).__init__()

    def set_up_gui(self):
        self.setWindowIcon(QIcon("Screen_Dimmer_Logo.png"))
