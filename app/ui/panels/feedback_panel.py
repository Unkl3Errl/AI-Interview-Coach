from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit
)


class FeedbackPanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()


    def _build_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Interview Feedback")

        self.feedback_display = QTextEdit()
        self.feedback_display.setReadOnly(True)

        self.feedback_display.setPlaceholderText(
            "AI feedback will appear here after your interview..."
        )

        layout.addWidget(title)
        layout.addWidget(self.feedback_display)

        self.setLayout(layout)


    def set_feedback(self, feedback_text: str):

        self.feedback_display.setPlainText(
            feedback_text
        )


    def clear_feedback(self):

        self.feedback_display.clear()