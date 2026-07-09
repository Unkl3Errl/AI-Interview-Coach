from packages.interview_coach_core import JobAnalyzer


class JobService:


    def __init__(self):

        self.analyzer = JobAnalyzer()


    def analyze(self, job_text):

        return self.analyzer.analyze(
            job_text
        )