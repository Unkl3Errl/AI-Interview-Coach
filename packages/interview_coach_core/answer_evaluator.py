class AnswerEvaluator:

    def evaluate(self, answer):

        score = 0

        if len(answer.response.split()) > 50:
            score += 30

        if "example" in answer.response.lower():
            score += 20

        if "result" in answer.response.lower():
            score += 20

        if "challenge" in answer.response.lower():
            score += 20

        answer.score = min(score,100)

        answer.feedback = (
            f"Answer scored {answer.score}/100. "
            "Improve with specific metrics and outcomes."
        )

        return answer