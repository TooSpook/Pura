from PyQt6.QtCore import Qt, QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QWidget, QListWidget, QGridLayout, QVBoxLayout, QCheckBox 
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV cleaner")
        self.setMinimumSize(QSize(768, 384))
        self.setWindowIcon(QIcon("resources/app_icon.png"))
        self.file_list = QListWidget()

        select_button = QPushButton("SELECT")
        select_button.setStyleSheet("padding: 2px 6px; font-size: 14px;")
        select_button.clicked.connect(self.file_selection)

        clean_button = QPushButton("Start Cleaning")
        clean_button.setStyleSheet("padding: 8px 28px; font-size: 14px;")

        dupe_check = QCheckBox(text="Remove Duplicates")
        missing_check = QCheckBox(text="Remove Missing Values")
        outliers_check = QCheckBox(text="Remove Outliers")
        noise_check = QCheckBox(text="Remove Noise")

        checkbox_layout = QVBoxLayout()
        checkbox_layout.setSpacing(5)
        checkbox_layout.addWidget(dupe_check)
        checkbox_layout.addWidget(missing_check)
        checkbox_layout.addWidget(outliers_check)
        checkbox_layout.addWidget(noise_check)

        checkbox_container = QWidget()
        checkbox_container.setLayout(checkbox_layout)

        layout = QGridLayout()
        layout.addWidget(self.file_list, 0, 0, 5, 1)
        layout.addWidget(select_button, 5, 0)
        layout.addWidget(checkbox_container, 0, 1, 5, 1, alignment=Qt.AlignmentFlag.AlignVCenter)
        layout.addWidget(clean_button, 5, 1) 

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