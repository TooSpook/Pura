import sys
import ctypes
from main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from PyQt6.QtGui import QIcon

if sys.platform == "win32":
    import ctypes
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(
        "pura.alpha.1.0"
    )

def main():
    app = QApplication([]) 
    app.setWindowIcon(QIcon("resources/app_icon.png"))
    window = MainWindow()   
    window.show()
    app.exec()

if __name__ == '__main__':
    main()