class AppState:

    def __init__(self):

        self.resume = None

        self.job_description = None

        self.current_question = None

        self.questions = []

        self.answers = []

        self.feedback = None

        self.score = None


    def clear_interview(self):

        self.current_question = None

        self.questions.clear()

        self.answers.clear()

        self.feedback = None

        self.score = None