import sys

from PySide6.QtWidgets import QApplication

from app.ui.main_window import MainWindow
from app.controller import AppController


def main():

    app = QApplication(sys.argv)

    window = MainWindow()

    controller = AppController(
        window
    )

    window.show()

    sys.exit(
        app.exec()
    )


if __name__ == "__main__":
    main()