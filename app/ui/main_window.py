from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Interview Coach")
        self.resize(1000, 700)

        self._build_ui()

    def _build_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        title = QLabel("AI Interview Coach")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet(
            """
            font-size: 24px;
            font-weight: bold;
            padding: 10px;
            """
        )

        self.job_description = QTextEdit()
        self.job_description.setPlaceholderText(
            "Paste the job description here..."
        )

        self.resume_summary = QTextEdit()
        self.resume_summary.setPlaceholderText(
            "Resume summary will appear here..."
        )
        self.resume_summary.setReadOnly(True)

        self.start_button = QPushButton("Start Interview")

        layout.addWidget(title)
        layout.addWidget(self.job_description)
        layout.addWidget(self.resume_summary)
        layout.addWidget(self.start_button)