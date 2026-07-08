from .interview_session import InterviewSessionEngine


class InterviewManager:

    def create(
        self,
        candidate,
        job
    ):

        return InterviewSessionEngine(
            candidate,
            job
        )