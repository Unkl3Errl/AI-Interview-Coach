from packages.interview_coach_core import LLMClient


class Interviewer:

    def __init__(self):

        self.llm = LLMClient()


    def ask(self, prompt):

        return self.llm.ask(prompt)