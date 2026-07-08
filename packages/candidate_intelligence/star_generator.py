class STARGenerator:


    def generate(
        self,
        experience,
        question
    ):

        return f"""

Situation:
During my work as {experience.role}
at {experience.company}, I encountered a
technical challenge related to the project.

Task:
I was responsible for analyzing the problem,
developing a solution, and ensuring successful delivery.

Action:
I applied my technical experience,
worked with stakeholders, and implemented
a structured approach.

Result:
The solution improved reliability,
accuracy, and business outcomes.

Question:
{question}

"""