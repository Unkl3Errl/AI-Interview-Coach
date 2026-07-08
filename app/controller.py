from PySide6.QtWidgets import QFileDialog

from packages.services.resume_service import ResumeService
from packages.services.job_service import JobService
from packages.services.interview_service import InterviewService


class AppController:

    def __init__(self, window):

        self.window = window

        # Services
        self.resume_service = ResumeService()
        self.job_service = JobService()
        self.interview_service = InterviewService()

        # Application state
        self.candidate = None
        self.job = None
        self.session = None

        self.connect_events()


    ####################################################
    # Connect UI Events
    ####################################################

    def connect_events(self):

        # Buttons
        self.window.load_resume_button.clicked.connect(
            self.load_resume
        )

        self.window.start_button.clicked.connect(
            self.start_interview
        )

        self.window.submit_button.clicked.connect(
            self.submit_answer
        )


    ####################################################
    # Resume Loading
    ####################################################

    def load_resume(self):

        filename, _ = QFileDialog.getOpenFileName(
            self.window,
            "Open Resume",
            "",
            "Resume Files (*.docx *.txt)"
        )


        if not filename:
            return


        try:

            self.candidate = (
                self.resume_service.load_resume(
                    filename
                )
            )


            summary = []

            summary.append(
                f"Candidate: {self.candidate.name}"
            )

            summary.append("")
            summary.append(
                "Skills:"
            )

            summary.append(
                "--------------------"
            )


            for skill in self.candidate.skills:

                summary.append(
                    f"• {skill}"
                )


            self.window.resume_summary.setPlainText(
                "\n".join(summary)
            )


            self.window.statusBar().showMessage(
                "Resume loaded successfully"
            )


        except Exception as e:

            self.window.statusBar().showMessage(
                f"Resume error: {e}"
            )


    ####################################################
    # Start Interview
    ####################################################

    def start_interview(self):

        if not self.candidate:

            self.window.statusBar().showMessage(
                "Please load a resume first"
            )

            return


        job_text = (
            self.window
            .job_description
            .toPlainText()
            .strip()
        )


        if not job_text:

            self.window.statusBar().showMessage(
                "Please enter a job description"
            )

            return


        try:

            self.job = (
                self.job_service.analyze(
                    job_text
                )
            )


            self.session = (
                self.interview_service
                .create_session(
                    self.candidate,
                    self.job
                )
            )


            question = (
                self.session
                .next_question()
            )


            self.add_interviewer_message(
                question
            )


            self.window.statusBar().showMessage(
                "Interview started"
            )


        except Exception as e:

            self.window.statusBar().showMessage(
                f"Interview error: {e}"
            )


    ####################################################
    # Submit Answer
    ####################################################

    def submit_answer(self):

        if not self.session:

            self.window.statusBar().showMessage(
                "No active interview"
            )

            return


        answer = (
            self.window.answer_box
            .toPlainText()
            .strip()
        )


        if not answer:

            return


        self.add_candidate_message(
            answer
        )


        self.session.submit_answer(
            answer
        )


        self.window.answer_box.clear()


        next_question = (
            self.session
            .next_question()
        )


        self.add_interviewer_message(
            next_question
        )


        self.window.statusBar().showMessage(
            "Answer submitted"


        )


    ####################################################
    # UI Helper Methods
    ####################################################

    def add_interviewer_message(
        self,
        message
    ):

        self.window.chat_window.append(
            "<b>🎤 Interviewer:</b>"
        )

        self.window.chat_window.append(
            message
        )

        self.window.chat_window.append(
            ""
        )


    def add_candidate_message(
        self,
        message
    ):

        self.window.chat_window.append(
            "<b>🙂 You:</b>"
        )

        self.window.chat_window.append(
            message
        )

        self.window.chat_window.append(
            ""
        )