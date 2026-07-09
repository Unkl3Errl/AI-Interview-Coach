from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QFileDialog
)


class ResumePanel(QWidget):

    resume_loaded = Signal(dict)


    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()


    def _build_ui(self):

        layout = QVBoxLayout()

        title = QLabel(
            "Resume"
        )

        self.load_button = QPushButton(
            "Load Resume"
        )

        self.load_button.clicked.connect(
            self.load_resume
        )


        layout.addWidget(
            title
        )

        layout.addWidget(
            self.load_button
        )

        self.setLayout(
            layout
        )


    def load_resume(self):

        filename, _ = QFileDialog.getOpenFileName(
            self,
            "Select Resume",
            "",
            "Documents (*.docx *.pdf *.txt)"
        )


        if filename:

            resume_data = {
                "file": filename
            }


            self.resume_loaded.emit(
                resume_data
            )