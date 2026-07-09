from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QProgressBar
)


class ScorePanel(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        self._build_ui()


    def _build_ui(self):

        layout = QVBoxLayout()

        title = QLabel("Interview Score")

        self.score_label = QLabel(
            "Overall Score: --"
        )

        self.score_bar = QProgressBar()
        self.score_bar.setRange(
            0,
            100
        )

        layout.addWidget(title)
        layout.addWidget(self.score_label)
        layout.addWidget(self.score_bar)

        self.setLayout(layout)


    def set_score(self, score: int):

        self.score_bar.setValue(
            score
        )

        self.score_label.setText(
            f"Overall Score: {score}/100"
        )


    def reset_score(self):

        self.score_bar.setValue(
            0
        )

        self.score_label.setText(
            "Overall Score: --"
        )