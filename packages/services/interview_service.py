from interview_engine import InterviewManager


class InterviewService:

    def __init__(self):
        self.manager = InterviewManager()

    def create_session(
        self,
        candidate,
        job
    ):

        return self.manager.create(
            candidate,
            job
        )