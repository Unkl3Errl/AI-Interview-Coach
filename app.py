from PySide6.QtWidgets import QApplication, QLabel, QWidget
import sys


class InterviewCoach(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("InterviewCoach AI")
        self.resize(900, 600)

        label = QLabel(
            "InterviewCoach AI\n\nSystem Ready",
            self
        )

        label.move(50, 50)


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = InterviewCoach()
    window.show()

    sys.exit(app.exec())