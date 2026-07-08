class InterviewScoring:

    def calculate(
        self,
        scores
    ):

        if not scores:

            return 0

        return round(
            sum(scores) / len(scores),
            1
        )