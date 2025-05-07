from PySide6.QtWidgets import QApplication, QMainWindow
from CMainWindow import CMainWindow

app = QApplication()
widget = CMainWindow() 
widget.show()
app.exec()
   