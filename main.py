import ctypes
from main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

#ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("csvcleaner.pre-alpha.1.7")

def main():
    app = QApplication([]) 
    app.setWindowIcon(QIcon("resources/app_icon.png"))
    window = MainWindow()   
    window.show()
    app.exec()

if __name__ == '__main__':
    main()