from PyQt5 import QtGui, QtWidgets


class SystemTrayApp(QtWidgets.QSystemTrayIcon):

    def __init__(self):
        super().__init__()

    def set_up_gui(self):
        self.setIcon(QtGui.QIcon("Screen_Dimmer_Logo.png"))
        self.setToolTip("Screen Dimmer - Made By Jackson Elia")
