from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout
)

from app.ui.panels.resume_panel import ResumePanel
from app.ui.panels.job_panel import JobPanel
from app.ui.panels.interview_panel import InterviewPanel
from app.ui.panels.feedback_panel import FeedbackPanel
from app.ui.panels.score_panel import ScorePanel


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle(
            "AI Interview Coach"
        )

        self.resize(
            1200,
            800
        )

        self._build_ui()


    def _build_ui(self):

        central_widget = QWidget()

        main_layout = QHBoxLayout()


        #
        # Left side - Input panels
        #
        left_layout = QVBoxLayout()

        self.resume_panel = ResumePanel()

        self.job_panel = JobPanel()

        self.interview_panel = InterviewPanel()


        left_layout.addWidget(
            self.resume_panel
        )

        left_layout.addWidget(
            self.job_panel
        )

        left_layout.addWidget(
            self.interview_panel
        )


        #
        # Right side - AI output
        #
        right_layout = QVBoxLayout()

        self.feedback_panel = FeedbackPanel()

        self.score_panel = ScorePanel()


        right_layout.addWidget(
            self.feedback_panel
        )

        right_layout.addWidget(
            self.score_panel
        )


        #
        # Assemble window
        #
        main_layout.addLayout(
            left_layout,
            2
        )

        main_layout.addLayout(
            right_layout,
            1
        )


        central_widget.setLayout(
            main_layout
        )

        self.setCentralWidget(
            central_widget
        )