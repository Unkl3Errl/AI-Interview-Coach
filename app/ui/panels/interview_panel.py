from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)


class InterviewPanel(QWidget):

    start_interview = Signal()


    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()


    def _build_ui(self):

        layout = QVBoxLayout()


        title = QLabel(
            "Interview Session"
        )


        self.question_display = QTextEdit()

        self.question_display.setReadOnly(
            True
        )


        self.answer_input = QTextEdit()

        self.answer_input.setPlaceholderText(
            "Enter your answer..."
        )


        self.start_button = QPushButton(
            "Start Interview"
        )

        self.start_button.clicked.connect(
            self.begin_interview
        )


        layout.addWidget(
            title
        )

        layout.addWidget(
            self.question_display
        )

        layout.addWidget(
            self.answer_input
        )

        layout.addWidget(
            self.start_button
        )


        self.setLayout(
            layout
        )


    def begin_interview(self):

        self.start_interview.emit()