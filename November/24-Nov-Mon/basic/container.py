from PySide6.QtWidgets import QMainWindow,QApplication,QWidget,QGridLayout,QLabel,QPushButton
from PySide6.QtCore import Qt

class MainApplication (QMainWindow):
    def __init__ (self):
        super().__init__()

        self.setWindowTitle("Container")
        container=QWidget()
        self.setCentralWidget(container)

        layout=QGridLayout(container)

        label1=QLabel("One")
        label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label2=QLabel("Two")
        label2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label3=QLabel("One")
        label3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label4=QPushButton("Click Me")
        # label4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout.addWidget(label1, 0, 0)
        layout.addWidget(label2, 0, 1)
        layout.addWidget(label3, 1, 0)
        layout.addWidget(label4, 1, 1)
    
app=QApplication()
window = MainApplication()
window.show()
app.exec()