from PySide6.QtWidgets import QApplication,QMainWindow,QLabel
from PySide6.QtCore import Qt
class MainApplication(QMainWindow):
    def __init__ (self):
        super(). __init__ ()
    
        self.setWindowTitle("Hello World!!!")
        label=QLabel("Hello World!!!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setCentralWidget(label)
app=QApplication()
window=MainApplication()
window.show()

app.exec()