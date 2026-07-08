class FollowUpGenerator:

    def generate(
        self,
        answer
    ):

        if len(answer.split()) < 30:

            return (
                "Can you expand on that?"
            )

        if "team" not in answer.lower():

            return (
                "What role did your team play?"
            )

        return (
            "What was the final outcome?"
        )