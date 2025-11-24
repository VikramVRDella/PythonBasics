from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QVBoxLayout,QLabel,QHBoxLayout
from PySide6.QtWidgets import QLineEdit,QTextEdit,QPushButton,QComboBox,QCheckBox,QRadioButton,QListWidget,QSlider
from PySide6.QtCore import Qt

class MainApplication(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widgets")
        container=QWidget()
        layout=QVBoxLayout(container)

        label1=QLabel("Name : ")
        label1_input=QLineEdit()
        label2=QLabel("Age  : ")
        label2_input=QLineEdit()
        label3=QTextEdit()
        label3.setPlaceholderText("Write Your Comments....")
        label4=QComboBox()
        label4_label=QLabel("Select the Value :")
        label4.addItems(["one","two","three"])
        label5=QListWidget()
        label5.addItems(["one","two","three"])

        inner=QWidget()
        inner_layout=QHBoxLayout(inner)
        cButton1=QCheckBox("one")
        cButton2=QCheckBox("two")
        cButton3=QCheckBox("three")
        inner_layout.addWidget(cButton1)
        inner_layout.addWidget(cButton2)
        inner_layout.addWidget(cButton3)

        inner1=QWidget()
        inner_layout_1=QVBoxLayout(inner1)
        cButton4=QRadioButton("one")
        cButton5=QRadioButton("two")
        cButton6=QRadioButton("three")
        inner_layout_1.addWidget(cButton4)
        inner_layout_1.addWidget(cButton5)
        inner_layout_1.addWidget(cButton6)
        slider=QSlider(Qt.Horizontal)
        slider.setRange(1,100)
        Button=QPushButton("ClickMe")
        Button.clicked.connect(lambda: print("Button Clicked..."))

        layout.addWidget(label1)
        layout.addWidget(label1_input)
        layout.addWidget(label2)
        layout.addWidget(label2_input)
        layout.addWidget(label3)
        layout.addWidget(label4_label)
        layout.addWidget(label4)
        layout.addWidget(label5)
        layout.addWidget(inner)
        layout.addWidget(inner1)
        layout.addWidget(slider)
        layout.addWidget(Button)

        self.setCentralWidget(container)

app=QApplication()
window=MainApplication()
window.show()
app.exec()