from .conversation_memory import ConversationMemory
from .prompt_builder import PromptBuilder
from .interviewer import Interviewer


class InterviewSessionEngine:

    def __init__(
        self,
        candidate,
        job
    ):

        self.candidate = candidate

        self.job = job

        self.memory = ConversationMemory()

        self.builder = PromptBuilder()

        self.interviewer = Interviewer()


    def next_question(self):

        prompt = self.builder.build(
            self.candidate,
            self.job,
            self.memory
        )

        question = self.interviewer.ask(
            prompt
        )

        self.memory.add(
            "Interviewer",
            question
        )

        return question


    def submit_answer(
        self,
        answer
    ):

        self.memory.add(
            "Candidate",
            answer
        )