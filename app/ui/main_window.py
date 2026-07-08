from PySide6.QtGui import QAction
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QTextEdit,
    QVBoxLayout,
    QWidget,
    QToolBar,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Interview Coach")
        self.resize(1000, 700)

        self._build_ui()
        self.create_menu()
        self.create_toolbar()
        self.apply_style()

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
    def create_menu(self):

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu("File")

        load_resume_action = QAction(
            "Load Resume",
            self
        )

        save_session_action = QAction(
            "Save Session",
            self
        )

        exit_action = QAction(
            "Exit",
            self
        )

        exit_action.triggered.connect(
            self.close
        )

        file_menu.addAction(
            load_resume_action
        )

        file_menu.addAction(
            save_session_action
        )

        file_menu.addSeparator()

        file_menu.addAction(
            exit_action
        )


        interview_menu = menu_bar.addMenu(
            "Interview"
        )

        start_action = QAction(
            "Start Interview",
            self
        )

        restart_action = QAction(
            "Restart Interview",
            self
        )

        interview_menu.addAction(
            start_action
        )

        interview_menu.addAction(
            restart_action
        )


        help_menu = menu_bar.addMenu(
            "Help"
        )

        about_action = QAction(
            "About",
            self
        )

        help_menu.addAction(
            about_action
        )
    def create_toolbar(self):

        toolbar = QToolBar(
            "Main Toolbar"
        )

        self.addToolBar(toolbar)


        toolbar.addAction(
            QAction(
                "📄 Resume",
                self
            )
        )

        toolbar.addAction(
            QAction(
                "📋 Job",
                self
            )
        )

        toolbar.addAction(
            QAction(
                "▶ Start",
                self
            )
        )

        toolbar.addAction(
            QAction(
                "💾 Save",
                self
            )
        )   
    def apply_style(self):

        self.setStyleSheet(
            """

            QWidget {
                font-family: Arial;
                font-size: 12px;
            }

            QGroupBox {
                font-weight: bold;
                border: 1px solid #888;
                border-radius: 5px;
                margin-top: 10px;
            }


            QPushButton {
                padding: 8px;
                border-radius: 5px;
            }


            QTextEdit,
            QPlainTextEdit {

                border-radius: 5px;
                padding: 5px;
            }

            """
        )