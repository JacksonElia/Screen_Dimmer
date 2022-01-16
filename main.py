from WindowApp import *
from PyQt5.QtWidgets import QApplication

# Launches application
app = QApplication([])
tray = TrayApp()
app.exec_()
