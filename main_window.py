from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QWidget, QListWidget, QGridLayout, QCheckBox 
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV cleaner")
        self.setMinimumSize(QSize(512, 384))
        self.setWindowIcon(QIcon("resources/app_icon.png"))
        self.file_list = QListWidget()

        select_button = QPushButton("SELECT")
        select_button.setStyleSheet("padding: 2px 6px; font-size: 14px;")
        select_button.clicked.connect(self.file_selection)

        clean_button = QPushButton("Start Cleaning")
        clean_button.setStyleSheet("padding: 6px 12px; font-size: 14px;")

        dupe_check = QCheckBox(text="Remove Duplicates")

        layout = QGridLayout()
        layout.addWidget(self.file_list, 0, 0)
        layout.addWidget(select_button, 1, 0)
        layout.addWidget(dupe_check, 0, 1)
        layout.addWidget(clean_button, 1, 1) 

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def file_selection(self) -> str:
        path, _ = QFileDialog.getOpenFileName(
            self, "Open CSV file", "", "CSV Files (*.csv);;All Files (*)"
        )

        if not path:
            return
        
        self.file_list.addItem(path)