from WindowApp import *
from PyQt5.QtWidgets import QApplication

# Launches application
app = QApplication([])
app.setQuitOnLastWindowClosed(False)
tray = TrayApp()
app.exec_()
