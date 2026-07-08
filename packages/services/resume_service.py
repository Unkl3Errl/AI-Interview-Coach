from interview_coach_core import ResumeParser
from candidate_intelligence import ProfileBuilder


class ResumeService:

    def __init__(self):
        self.parser = ResumeParser()
        self.builder = ProfileBuilder()

    def load_resume(self, filename):

        text = self.parser.extract_text(filename)

        profile = self.builder.build(text)

        return profile