from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QTextEdit,
    QPushButton
)


class JobPanel(QWidget):

    job_loaded = Signal(str)


    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()


    def _build_ui(self):

        layout = QVBoxLayout()


        title = QLabel(
            "Job Description"
        )


        self.job_text = QTextEdit()

        self.job_text.setPlaceholderText(
            "Paste job description here..."
        )


        self.load_button = QPushButton(
            "Submit Job Description"
        )

        self.load_button.clicked.connect(
            self.submit_job
        )


        layout.addWidget(
            title
        )

        layout.addWidget(
            self.job_text
        )

        layout.addWidget(
            self.load_button
        )


        self.setLayout(
            layout
        )


    def submit_job(self):

        text = self.job_text.toPlainText()


        if text.strip():

            self.job_loaded.emit(
                text
            )