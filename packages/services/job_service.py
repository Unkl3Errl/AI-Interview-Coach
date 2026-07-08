from interview_coach_core import JobAnalyzer


class JobService:

    def __init__(self):
        self.analyzer = JobAnalyzer()

    def analyze(self, text):
        return self.analyzer.analyze(text)