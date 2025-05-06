import sys
from PyQt5.QtWidgets import *

class CustomDialog(QDialog):
    def __init__(self, items, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Choose from List")
        self.layout = QVBoxLayout()
        self.combo = QComboBox()
        self.combo.addItems(items)
        self.layout.addWidget(QLabel("Select a programming language:"))
        self.layout.addWidget(self.combo)

        self.buttons = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        self.buttonBox = QDialogButtonBox(self.buttons)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)

        self.setLayout(self.layout)

    def selectedItem(self):
        return self.combo.currentText()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tugas Week-9 Input Dialog")
        self.setGeometry(100, 100, 500, 200)
        main_layout = QVBoxLayout()

        row1 = QHBoxLayout()
        choose_button = QPushButton("Choose from list")
        choose_button.clicked.connect(self.choose_from_list)
        self.choose_input = QLineEdit()
        row1.addWidget(choose_button)
        row1.addWidget(self.choose_input)

        row2 = QHBoxLayout()
        name_button = QPushButton("Get name")
        name_button.clicked.connect(self.get_name)
        self.name_input = QLineEdit()
        row2.addWidget(name_button)
        row2.addWidget(self.name_input)

        row3 = QHBoxLayout()
        int_button = QPushButton("Enter an integer")
        int_button.clicked.connect(self.get_integer)
        self.int_input = QLineEdit()
        row3.addWidget(int_button)
        row3.addWidget(self.int_input)

        identitas = QVBoxLayout()
        identitas.addWidget(QLabel("<span style='font-weight: bold; color: #000; font-size:10pt;'>Nama: Raizul Furkon</span>"))
        identitas.addWidget(QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>NIM: F1D022024</span>"))
        identitas.addWidget(QLabel("<span style='font-weight: bold; color: #000; font-size:10pt'>Kelas: C</span>"))

        main_layout.addLayout(row1)
        main_layout.addLayout(row2)
        main_layout.addLayout(row3)
        main_layout.addLayout(identitas)

        self.setLayout(main_layout)

    def choose_from_list(self):
        langs = ["C++", "Python", "Java", "JavaScript", "Go"]
        dialog = CustomDialog(langs, self)
        if dialog.exec_() == QDialog.Accepted:
            selected = dialog.selectedItem()
            self.choose_input.setText(selected)

    def get_name(self):
        name, ok = QInputDialog.getText(self, "Get Name", "Enter your name:")
        if ok and name.strip():
            self.name_input.setText(name)

    def get_integer(self):
        value, ok = QInputDialog.getInt(self, "Enter an Integer", "Enter a number:")
        if ok:
            self.int_input.setText(str(value))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())