from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QMainWindow, QPushButton, QFileDialog, QVBoxLayout, QWidget, QListWidget
from PyQt6.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("CSV cleaner")
        self.setMinimumSize(QSize(512, 384))
        self.setWindowIcon(QIcon("resources/app_icon.png"))
        self.file_list = QListWidget()

        button = QPushButton("SELECT")
        button.setMinimumSize(120, 40)
        button.setMaximumSize(200, 50)
        button.setStyleSheet("padding: 12px 24px; font-size: 14px;")
        button.clicked.connect(self.file_selection)

        layout = QVBoxLayout()
        layout.addWidget(self.file_list)
        layout.addWidget(button)

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