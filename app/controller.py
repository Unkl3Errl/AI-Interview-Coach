from app.state.app_state import AppState


class AppController:

    def __init__(self, window):

        self.window = window

        self.state = AppState()

        self._connect_signals()


    def _connect_signals(self):

        #
        # Resume events
        #
        if hasattr(
            self.window.resume_panel,
            "resume_loaded"
        ):
            self.window.resume_panel.resume_loaded.connect(
                self.handle_resume_loaded
            )


        #
        # Job description events
        #
        if hasattr(
            self.window.job_panel,
            "job_loaded"
        ):
            self.window.job_panel.job_loaded.connect(
                self.handle_job_loaded
            )


        #
        # Interview events
        #
        if hasattr(
            self.window.interview_panel,
            "start_interview"
        ):
            self.window.interview_panel.start_interview.connect(
                self.start_interview
            )


    #
    # Resume handling
    #

    def handle_resume_loaded(self, resume_data):

        self.state.resume = resume_data

        print(
            "Resume stored in application state."
        )

        print(
            self.state.resume
        )


    #
    # Job description handling
    #

    def handle_job_loaded(self, job_data):

        self.state.job_description = job_data

        print(
            "Job description stored in application state."
        )


        print(
            self.state.job_description
        )


    #
    # Interview workflow
    #

    def start_interview(self):

        self.state.clear_interview()

        print(
            "Interview session started."
        )


        self.window.feedback_panel.set_feedback(
            "Interview started. Preparing first question..."
        )


    #
    # AI feedback placeholder
    #
    # This will be replaced after Ollama integration
    #

    def generate_feedback(self, transcript):

        feedback = (
            "AI feedback placeholder."
        )


        self.state.feedback = feedback


        self.window.feedback_panel.set_feedback(
            feedback
        )